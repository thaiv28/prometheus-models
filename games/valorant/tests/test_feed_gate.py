"""Offline checks for the stdlib pre-install feed gate."""

import gzip
import importlib.util
import json
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "feed_gate", Path(__file__).resolve().parents[1] / "scripts/feed_gate.py"
)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
NOW = datetime(2026, 10, 30, 12, tzinfo=UTC)


def state():
    return (
        {
            "last_export_at": (NOW - timedelta(minutes=10)).isoformat(),
            "event_tickers": ["E"],
            "state_etag": "tag",
        },
        {
            "matches": [
                {"start": (NOW + timedelta(hours=1)).isoformat(), "status": "upcoming"}
            ]
        },
    )


def fake(url, params):
    assert url == gate.KALSHI_API
    assert params["series_ticker"] in gate.SERIES
    assert params["status"] == "open"
    return {"events": [{"event_ticker": "E"}]}


@pytest.mark.parametrize(
    "change",
    [
        None,
        "missing",
        "age",
        "future",
        "etag",
        "missing_etag",
        "event",
        "live",
        "start",
        "failure",
        "bad_snapshot",
    ],
)
def test_probe(change):
    previous, snapshot = state()
    if change == "missing":
        previous = {}
    if change == "age":
        previous["last_export_at"] = (NOW - timedelta(hours=2)).isoformat()
    if change == "future":
        previous["last_export_at"] = (NOW + timedelta(minutes=1)).isoformat()
    if change == "etag":
        previous["state_etag"] = "old"
    if change == "missing_etag":
        previous.pop("state_etag")
    if change == "live":
        snapshot["matches"][0]["status"] = "live"
    if change == "start":
        snapshot["matches"][0]["start"] = NOW.isoformat()
    if change == "bad_snapshot":
        snapshot = {}

    def get(url, params):
        if change == "failure":
            raise OSError("offline")
        result = fake(url, params)
        if change == "event":
            result["events"].append({"event_ticker": "NEW"})
        return result

    run, result = gate.probe(previous, snapshot, state_etag="tag", get=get, now=NOW)
    assert run is (change is not None)
    assert result.get("last_export_at") == previous.get("last_export_at")
    assert result.get("state_etag") == previous.get("state_etag")


@pytest.mark.parametrize(
    "offset,expected", [(-11, False), (-10, False), (-1, True), (0, True), (1, False)]
)
def test_start_interval(offset, expected):
    previous, snapshot = state()
    snapshot["matches"][0]["start"] = (NOW + timedelta(minutes=offset)).isoformat()
    assert (
        gate.probe(previous, snapshot, state_etag="tag", get=fake, now=NOW)[0]
        is expected
    )


def test_pagination_for_every_priced_series():
    previous, snapshot = state()
    calls = []

    def get(url, params):
        calls.append(params.copy())
        return {
            "events": [{"event_ticker": "E"}],
            "cursor": "next" if "cursor" not in params else "",
        }

    assert not gate.probe(previous, snapshot, state_etag="tag", get=get, now=NOW)[0]
    assert [(p["series_ticker"], p.get("cursor")) for p in calls] == [
        (s, c) for s in gate.SERIES for c in (None, "next")
    ]


def test_cli_missing_inputs_and_export_marker(tmp_path, monkeypatch):
    path, snapshot, output = (
        tmp_path / name for name in ("gate.json", "snapshot.gz", "output")
    )
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "feed_gate.py",
            "--gate",
            str(path),
            "--snapshot",
            str(snapshot),
            "--state-etag",
            "new-tag",
        ],
    )
    gate.main()
    assert output.read_text() == "run=true\n"
    previous, cached = state()
    path.write_text(json.dumps(previous))
    with gzip.open(snapshot, "wt") as handle:
        json.dump(cached, handle)
    monkeypatch.setattr(sys, "argv", sys.argv + ["--mark-export"])
    gate.main()
    marked = json.loads(path.read_text())
    assert marked["state_etag"] == "new-tag"
    assert marked["event_tickers"] == previous["event_tickers"]
    assert gate.instant(marked["last_export_at"]) >= NOW


@pytest.mark.parametrize("raw", [b"\x1f\x8b", b"not gzip"])
def test_broken_snapshot_is_missing(tmp_path, raw):
    path = tmp_path / "snapshot.gz"
    path.write_bytes(raw)
    assert gate.read(path, compressed=True) == {}


def test_unchanged_cli_keeps_gate_bytes(tmp_path, monkeypatch):
    import gzip
    import json
    import sys

    previous, snapshot = state()
    path, cached, output = (
        tmp_path / n for n in ("gate.json", "snapshot.gz", "output")
    )
    path.write_text(json.dumps(previous, sort_keys=True) + "\n")
    with gzip.open(cached, "wt") as handle:
        json.dump(snapshot, handle)
    original = path.read_bytes()
    probe = gate.probe
    monkeypatch.setattr(
        gate, "probe", lambda p, s, **kw: probe(p, s, get=fake, now=NOW, **kw)
    )
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "feed_gate.py",
            "--gate",
            str(path),
            "--snapshot",
            str(cached),
            "--state-etag",
            previous["state_etag"],
        ],
    )
    gate.main()
    assert output.read_text() == "run=false\n"
    assert path.read_bytes() == original
