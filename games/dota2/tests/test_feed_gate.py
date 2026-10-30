"""Offline checks for the pre-installation probe."""

import importlib.util
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
            "last_export_at": (NOW - timedelta(minutes=15)).isoformat(),
            "revids": {"P": 1},
            "event_tickers": ["E"],
        },
        {"version": 2, "pages": {"P": {"revid": 1}}, "starts": []},
    )


def fake(url, params):
    if url == gate.LP_API:
        return {"query": {"pages": {"1": {"title": "P", "revisions": [{"revid": 1}]}}}}
    return {"events": [{"event_ticker": "E"}]}


@pytest.mark.parametrize(
    "change", [None, "revision", "event", "start", "age", "failure", "missing", "old"]
)
def test_probe(change):
    previous, snapshot = state()
    if change == "start":
        snapshot["starts"] = [(NOW - timedelta(minutes=1)).isoformat()]
    if change == "age":
        previous["last_export_at"] = (NOW - timedelta(hours=2)).isoformat()
    if change == "missing":
        previous = {}
    if change == "old":
        snapshot["version"] = 1

    def get(url, params):
        if change == "failure":
            raise OSError("offline")
        value = fake(url, params)
        if change == "revision" and url == gate.LP_API:
            value["query"]["pages"]["1"]["revisions"][0]["revid"] = 2
        if change == "event" and url == gate.KALSHI_API:
            value["events"].append({"event_ticker": "NEW"})
        return value

    run, result = gate.probe(previous, snapshot, get=get, now=NOW)
    assert run is (change is not None)
    assert result.get("last_export_at") == previous.get("last_export_at")


def test_gate_batches_spacing_and_event_pagination():
    previous, snapshot = state()
    snapshot["pages"] = {f"P{i}": {"revid": i} for i in range(51)}
    previous["revids"] = {t: p["revid"] for t, p in snapshot["pages"].items()}
    calls, sleeps = [], []

    def get(url, params):
        calls.append((url, params))
        if url == gate.LP_API:
            return {
                "query": {
                    "pages": {
                        t: {"title": t, "revisions": [{"revid": int(t[1:])}]}
                        for t in params["titles"].split("|")
                    }
                }
            }
        return {
            "events": [{"event_ticker": "E"}],
            "cursor": "next" if "cursor" not in params else "",
        }

    assert not gate.probe(
        previous, snapshot, get=get, now=NOW, sleep=sleeps.append, clock=lambda: 0
    )[0]
    assert [len(p["titles"].split("|")) for u, p in calls if u == gate.LP_API] == [
        50,
        1,
    ]
    assert sleeps == [2.2]
    assert [p.get("cursor") for u, p in calls if u == gate.KALSHI_API] == [None, "next"]


def test_cli_missing_inputs_and_export_marker(tmp_path, monkeypatch):
    import gzip
    import json
    import sys

    path, snapshot, output = (
        tmp_path / name for name in ("gate.json", "latest.json.gz", "output")
    )
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    monkeypatch.setattr(
        sys, "argv", ["feed_gate.py", "--gate", str(path), "--snapshot", str(snapshot)]
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
    assert marked["event_tickers"] == previous["event_tickers"]
    assert marked["revids"] == previous["revids"]
    assert gate.instant(marked["last_export_at"]) >= NOW


@pytest.mark.parametrize("raw", [b"\x1f\x8b", b"not gzip"])
def test_broken_snapshot_is_missing(tmp_path, raw):
    path = tmp_path / "snapshot.gz"
    path.write_bytes(raw)
    assert gate.read(path, compressed=True) == {}
