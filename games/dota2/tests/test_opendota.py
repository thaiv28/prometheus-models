"""OpenDota uses injected transports and temporary caches exclusively."""

import importlib.util
import json
import sqlite3
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

from promdota.opendota import cache, fetch
from promdota.opendota.http import BudgetExhausted, Fetcher

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/fixtures"


@pytest.fixture(autouse=True)
def isolated_cache(tmp_path, monkeypatch):
    monkeypatch.setenv("PROMDOTA_DATA", str(tmp_path / "raw"))


def fixture(name):
    return json.loads((FIXTURES / name).read_text())


def transport(payload, limit=1800):
    return Fetcher(
        get=lambda url, params: (200, payload), sleep=lambda n: None, limit=limit
    )


def test_bulk_finality_and_err():
    now = datetime(2026, 10, 29, tzinfo=UTC)
    client = transport(fixture("od_explorer_matches.json"))
    assert fetch.bulk(client, "2026-01", "2026-01", now)["saved"] == 2
    assert client.requests == 2
    assert fetch.bulk(client, "2026-01", "2026-01", now)["cached"] == 2
    assert client.requests == 2
    # A recent month stays mutable even if today's wall clock is much later.
    assert fetch.bulk(client, "2026-10", "2026-10", now)["saved"] == 2
    assert fetch.bulk(client, "2026-10", "2026-10", now)["saved"] == 2
    errors = fetch.bulk(
        transport(fixture("od_explorer_error.json")), "2026-09", "2026-09", now
    )
    assert errors["errors"] == 2
    assert not (cache.data_dir() / "explorer/matches/2026-09.json.gz").exists()


def test_budget_retry_and_spacing():
    starts, sleeps = [], []
    client = Fetcher(
        get=lambda url, params: (starts.append(url) or 429, {}),
        sleep=sleeps.append,
        clock=lambda: 0,
        limit=3,
    )
    with pytest.raises(BudgetExhausted):
        client.query("/matches/1")
    assert len(starts) == 3
    assert sleeps.count(1.1) == 2
    assert (
        fetch.bulk(transport({"rows": []}, limit=1), "2020-01", "2020-02")["limited"]
        == 1
    )


def test_four_attempts():
    client = Fetcher(get=lambda url, params: (503, {}), sleep=lambda n: None)
    with pytest.raises(RuntimeError, match="503"):
        client.query("/matches/1")
    assert client.requests == 4


def make_db(path):
    conn = sqlite3.connect(path)
    conn.executescript((ROOT / "scripts/001_create_tables.sql").read_text())
    conn.execute(
        "INSERT INTO events(event_id,title,section,international,excluded) VALUES(1,'test','tier1',1,0)"
    )
    conn.executemany(
        "INSERT INTO teams VALUES(?,?,?)",
        [(1, "og", "OG"), (2, "vici gaming", "Vici Gaming")],
    )
    conn.execute(
        "INSERT INTO matches(match_id,event_id,page,ordinal,start_utc,time_known,best_of,team1_id,team2_id,score1,score2) VALUES(1,1,'test',1,'2026-10-01T00:00:00Z',1,3,1,2,0,0)"
    )
    conn.execute(
        "INSERT INTO games(game_id,match_id,\"order\",dota_match_id,team1_side) VALUES(11,1,1,8719042091,'dire')"
    )
    conn.commit()
    return conn


def test_single_projection_missing_retry_and_limit(tmp_path):
    db = tmp_path / "test.db"
    conn = make_db(db)
    conn.close()
    now = datetime(2026, 10, 29, tzinfo=UTC)
    missing = transport(fixture("od_match_missing.json"))
    assert fetch.games(db, missing, now)["missing"] == 1
    assert not fetch.games(db, missing, now + timedelta(days=6))
    assert missing.requests == 1
    assert fetch.games(db, missing, now + timedelta(days=7))["missing"] == 1
    assert (
        fetch.games(db, transport({}, limit=0), now + timedelta(days=14))["limited"]
        == 1
    )
    payload = fixture("od_match_8719042091.json") | {"large_unused_field": "discard"}
    assert fetch.games(db, transport(payload), now + timedelta(days=14))["saved"] == 1
    record = cache.read(cache.game_file(8719042091))
    assert record["fetch_version"] == 1
    assert "large_unused_field" not in record
    assert set(record["players"][0]) == set(cache.PLAYER_FIELDS)
    assert cache.read(cache.data_dir() / "missing.json") == {}
    assert not fetch.games(db, transport({}), now + timedelta(days=15))


def load_builder():
    spec = importlib.util.spec_from_file_location(
        "load_opendota", ROOT / "scripts/003_load_opendota.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.build


def test_loader_reversed_conflict_and_slots(tmp_path):
    conn = make_db(tmp_path / "db")
    data = fixture("od_match_8719042091.json")
    assert data["radiant_win"] is True
    assert data["radiant_team_id"] == 726228
    counts = load_builder()(conn, {8719042091: data})
    assert counts["winners_opendota"] == 1
    assert tuple(
        conn.execute("SELECT winner,winner_source,team1_side FROM games").fetchone()
    ) == (2, "opendota", "dire")
    assert tuple(
        conn.execute("SELECT score1,score2,winner FROM matches").fetchone()
    ) == (0, 1, 2)
    for player in data["players"]:
        team = conn.execute(
            "SELECT team FROM player_games JOIN players USING(player_id) WHERE key=?",
            (f"steam:{player['account_id']}",),
        ).fetchone()[0]
        assert team == (2 if player["player_slot"] < 128 else 1)
    assert counts["games_with_players"] == 1
    conn.execute("UPDATE games SET winner=1,winner_source='liquipedia'")
    assert load_builder()(conn, {8719042091: data})["winner_conflicts"] == 1
    assert conn.execute("SELECT winner FROM games").fetchone()[0] == 1


def test_loader_unknown_side_and_keep_unresolved(tmp_path):
    conn = make_db(tmp_path / "db")
    conn.execute("UPDATE games SET team1_side=NULL")
    conn.execute("INSERT INTO opendota_teams VALUES(726228,2,3)")
    data = fixture("od_match_8719042091.json")
    load_builder()(conn, {8719042091: data})
    assert conn.execute("SELECT team1_side FROM games").fetchone()[0] == "dire"
    conn.execute("UPDATE games SET winner=NULL,team1_side=NULL")
    conn.execute("DELETE FROM opendota_teams")
    counts = load_builder()(conn, {8719042091: data})
    assert counts["unresolved_matches"] == 1
    assert counts["matches"] == 1
    assert conn.execute("SELECT winner FROM matches").fetchone()[0] is None


def test_http_404_and_wrong_id_enter_missing(tmp_path):
    db = tmp_path / "db"
    make_db(db).close()
    now = datetime(2026, 10, 29, tzinfo=UTC)
    client = Fetcher(get=lambda url, params: (404, {}), sleep=lambda n: None)
    assert fetch.games(db, client, now)["missing"] == 1
    wrong = fixture("od_match_8719042091.json") | {"match_id": 999}
    assert fetch.games(db, transport(wrong), now + timedelta(days=7))["missing"] == 1
    assert not cache.game_file(8719042091).exists()


def test_explorer_cache_loads_players_and_skips_single(tmp_path):
    db = tmp_path / "db"
    conn = make_db(db)
    game = fixture("od_match_8719042091.json")
    match_row = {key: game[key] for key in cache.MATCH_FIELDS}
    player_payload = fixture("od_explorer_players.json")
    responses = iter([{"rows": [match_row]}, player_payload])
    client = Fetcher(
        get=lambda url, params: (200, next(responses)), sleep=lambda n: None
    )
    assert fetch.bulk(client, "2026-03", "2026-03")["saved"] == 2
    records = cache.load_records()
    assert len(records[8719042091]["players"]) == len(player_payload["rows"])
    no_requests = transport({}, limit=0)
    assert not fetch.games(db, no_requests)
    assert no_requests.requests == 0
    assert load_builder()(conn)["games_with_players"] == 1
    assert conn.execute("SELECT winner FROM games").fetchone()[0] == 2


def test_api_key_is_sent_lifts_the_daily_cap_and_spaces_less(monkeypatch):
    monkeypatch.setenv("OPENDOTA_API_KEY", "secret")
    seen, waits = [], []
    client = Fetcher(
        get=lambda url, params: seen.append(params) or (200, {"rows": []}),
        sleep=waits.append,
        clock=lambda: 0.0,
    )
    assert client.limit == 100_000 and Fetcher(limit=5000).limit == 5000
    client.query("/explorer", sql="x")
    client.query("/explorer", sql="y")
    assert seen == [
        {"sql": "x", "api_key": "secret"},
        {"sql": "y", "api_key": "secret"},
    ]
    assert waits == [0.1]
    monkeypatch.delenv("OPENDOTA_API_KEY")
    assert Fetcher().limit == 1800 and Fetcher(limit=5000).limit == 1800
