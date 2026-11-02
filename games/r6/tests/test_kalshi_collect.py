"""Offline R6 catalogs, immutable histories, retries and command checks."""

import gzip
import json
from datetime import UTC, datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlsplit

import pytest
from typer.testing import CliRunner

from promr6.kalshi.api import API, Client
from promr6.kalshi.cli import app
from promr6.kalshi.collect import SERIES, collect, data_dir, snapshot_books

FIXTURES = Path(__file__).parent / "fixtures" / "kalshi"
NOW = datetime(2026, 11, 2, tzinfo=UTC)


class Clock:
    def __init__(self):
        self.time = 0
        self.sleeps = []

    def __call__(self):
        return self.time

    def sleep(self, seconds):
        self.sleeps.append(seconds)
        self.time += seconds


class FakeGet:
    def __init__(self):
        self.catalog = json.loads((FIXTURES / "markets_sample.json").read_text())
        self.calls = []
        self.fail_catalog = None
        self.fail_trade = None
        self.empty_trade = None
        self.empty_candles = None
        self.fail_book = None
        for market in self.catalog[SERIES[1]]:
            market["status"] = "active"

    def __call__(self, url):
        split = urlsplit(url)
        path = split.path.removeprefix("/trade-api/v2")
        query = {key: value[0] for key, value in parse_qs(split.query).items()}
        self.calls.append((path, query))
        if path in ("/markets", "/historical/markets"):
            source = query["series_ticker"]
            if source == self.fail_catalog:
                raise ValueError("catalog unavailable")
            markets = self.catalog[source]
            if query.get("status"):
                return {"markets": [m for m in markets if m["status"] == "active"]}
            if path == "/historical/markets":
                return {"markets": markets[:2] if source == SERIES[0] else []}
            if "cursor" in query:
                return {"markets": markets[2:], "cursor": ""}
            return {"markets": markets[:2], "cursor": "next"}
        if path in ("/markets/trades", "/historical/trades"):
            ticker = query["ticker"]
            if ticker == self.fail_trade:
                raise ValueError("trade unavailable")
            if ticker == self.empty_trade or query.get("cursor"):
                return {"trades": []}
            return {
                "trades": [
                    {"trade_id": "b", "created_time": "2026-01-02T00:00:00Z"},
                    {"trade_id": "a", "created_time": "2026-01-01T00:00:00Z"},
                ],
                "cursor": "next",
            }
        if path.endswith("/candlesticks"):
            assert query["period_interval"] == "60"
            assert int(query["start_ts"]) < int(query["end_ts"])
            return {
                "candlesticks": []
                if self.empty_candles and self.empty_candles in path
                else [{"end_period_ts": 1}]
            }
        if path.endswith("/orderbook"):
            if self.fail_book and self.fail_book in path:
                raise ValueError("book unavailable")
            return {"orderbook_fp": {"yes_dollars": [["0.5", "10"]], "no_dollars": []}}
        raise AssertionError(url)


@pytest.fixture
def setup(tmp_path, monkeypatch):
    monkeypatch.setenv("PROMR6_DATA", str(tmp_path))
    fake, clock = FakeGet(), Clock()
    return fake, Client(get=fake, sleep=clock.sleep, clock=clock), tmp_path / "kalshi"


def test_collection_pagination_raw_catalog_and_immutable_histories(setup):
    fake, client, root = setup
    summary = collect(client, now=lambda: NOW)
    assert not summary.errors
    assert summary.series[SERIES[0]].markets == 8
    assert summary.series[SERIES[0]].new_trade_files == 8
    assert summary.series[SERIES[0]].new_candle_files == 8
    assert summary.series[SERIES[1]].book_snapshots == 4
    catalog = json.loads((root / "markets" / f"{SERIES[0]}.json").read_text())
    assert catalog == sorted(fake.catalog[SERIES[0]], key=lambda m: m["ticker"])
    assert any(q.get("cursor") == "next" for _, q in fake.calls)
    for path in (root / "trades").iterdir():
        with gzip.open(path, "rt") as handle:
            assert [json.loads(line)["trade_id"] for line in handle] == ["a", "b"]
    saved = {
        p: (p.read_bytes(), p.stat().st_mtime_ns)
        for kind in ("trades", "candles")
        for p in (root / kind).iterdir()
    }
    fake.calls.clear()
    assert not collect(client, now=lambda: NOW).errors
    assert all(
        (p.read_bytes(), p.stat().st_mtime_ns) == old for p, old in saved.items()
    )
    assert all(
        p in ("/markets", "/historical/markets") or p.endswith("/orderbook")
        for p, _ in fake.calls
    )
    assert len(list((root / "books").rglob("*.jsonl.gz"))) == 2
    assert not list(root.rglob("*.tmp"))


def test_historical_and_current_endpoint_selection(setup):
    fake, client, _ = setup
    # Keep one historical-only market; current catalog copies otherwise win.
    historic = fake.catalog[SERIES[0]][0]
    original = fake.__call__

    def get(url):
        response = original(url)
        path = urlsplit(url).path
        if path.endswith("/markets") and "/historical/" not in path:
            response["markets"] = [
                m for m in response["markets"] if m["ticker"] != historic["ticker"]
            ]
        return response

    client.get = get
    assert not collect(client, books=False).errors
    assert any(
        p == "/historical/trades" and q["ticker"] == historic["ticker"]
        for p, q in fake.calls
    )
    assert any(
        p == f"/historical/markets/{historic['ticker']}/candlesticks"
        for p, _ in fake.calls
    )
    assert any(p == "/markets/trades" for p, _ in fake.calls)


@pytest.mark.parametrize("kind", ["fail_trade", "empty_trade", "empty_candles"])
def test_failed_histories_retry_and_manifest(setup, kind):
    fake, client, root = setup
    ticker = fake.catalog[SERIES[0]][0]["ticker"]
    setattr(fake, kind, ticker)
    summary = collect(client, books=False)
    assert len(summary.errors) == 1
    suffix = "trades" if kind != "empty_candles" else "candles"
    manifest = json.loads((root / "manifest.json").read_text())
    assert ticker not in manifest[suffix]
    setattr(fake, kind, None)
    assert not collect(client, books=False).errors
    assert ticker in json.loads((root / "manifest.json").read_text())[suffix]


def test_limit_catalog_failure_and_snapshot_errors(setup):
    fake, client, root = setup
    summary = collect(client, books=False, limit=1)
    assert (
        sum(s.new_trade_files + s.new_candle_files for s in summary.series.values())
        == 1
    )
    assert not (root / "books").exists()
    fake.fail_catalog = SERIES[0]
    fake.fail_book = fake.catalog[SERIES[1]][0]["ticker"]
    summary = collect(client, limit=0)
    assert summary.catalog_errors == [SERIES[0]]
    count = snapshot_books(client, now=lambda: NOW)
    assert count == 3 and len(count.errors) == 2
    with pytest.raises(ValueError):
        collect(client, limit=-1)


@pytest.mark.parametrize("error", [429, 500, 503, "url", "timeout"])
def test_retries_pacing(error):
    clock, calls = Clock(), []

    def get(url):
        calls.append((url, clock()))
        if len(calls) == 1:
            if error == "url":
                raise URLError("offline")
            if error == "timeout":
                raise TimeoutError("offline")
            raise HTTPError(url, error, "retry", {}, None)
        return {"ok": True}

    client = Client(get=get, sleep=clock.sleep, clock=clock)
    assert client.json("/markets", ticker="A B", absent=None) == {"ok": True}
    client.json("/markets")
    assert calls[0][0] == f"{API}/markets?ticker=A+B"
    assert [at for _, at in calls] == pytest.approx([0, 1, 1.06])


def test_retry_exhaustion_and_nonretryable():
    clock, calls = Clock(), []

    def get(url):
        calls.append(url)
        raise HTTPError(url, 503, "unavailable", {}, None)

    with pytest.raises(HTTPError):
        Client(get=get, sleep=clock.sleep, clock=clock).json("/markets")
    assert len(calls) == 5 and clock.sleeps == [1, 2, 4, 8]

    def bad(url):
        raise HTTPError(url, 400, "invalid", {}, None)

    with pytest.raises(HTTPError):
        Client(get=bad).json("/markets")


def test_cli_and_manifest(setup, monkeypatch):
    fake, client, root = setup
    monkeypatch.setattr("promr6.kalshi.cli.Client", lambda: client)
    result = CliRunner().invoke(app, ["collect", "--no-books", "--limit", "0"])
    assert result.exit_code == 0 and "errors=0" in result.output
    fake.fail_catalog = SERIES[0]
    assert CliRunner().invoke(app, ["collect", "--limit", "0"]).exit_code == 1
    result = CliRunner().invoke(app, ["manifest"])
    assert result.exit_code == 0 and "trades=0 candles=0" in result.output
    assert json.loads((root / "manifest.json").read_text())["version"] == 1
    assert CliRunner().invoke(app, ["books", "--every", "0"]).exit_code == 2
    assert CliRunner().invoke(app, ["books", "--minutes", "0"]).exit_code == 0


def test_default_data_root(monkeypatch):
    monkeypatch.delenv("PROMR6_DATA", raising=False)
    assert data_dir() == Path(__file__).resolve().parents[1] / "data" / "kalshi"
