"""Offline fixture cache builds, including the full setup script."""

import gzip
import importlib.util
import json
import os
import shutil
import sqlite3
import subprocess
from pathlib import Path

import pytest

from promdota.liquipedia import cache
from promdota.opendota import cache as od_cache

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "load_liquipedia", ROOT / "scripts/002_load_liquipedia.py"
)
loader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(loader)


@pytest.fixture
def conn():
    with sqlite3.connect(":memory:") as conn:
        conn.executescript((ROOT / "scripts/001_create_tables.sql").read_text())
        yield conn


def fixture_pages():
    records = [
        json.loads(gzip.decompress(p.read_bytes()))
        for p in (ROOT / "tests/fixtures/liquipedia").glob("*.json.gz")
    ]
    return {p["title"]: p for p in records}


def record(title, pid, text):
    return {"title": title, "pageid": pid, "revid": 1, "wikitext": text}


def match():
    return "{{Match|opponent1={{TeamOpponent|Alpha}}|opponent2={{TeamOpponent|Beta}}|date=Jan 1, 2026 - 10:00 {{Abbr/UTC}}|matchid1=123|map1={{Map|winner=1|team1side=radiant}}}}"


def test_fixture_build(conn):
    counts, errors = loader.build(conn, fixture_pages())
    assert errors == []
    assert counts["events"] == 3
    assert counts["matches"] > 8
    assert counts["games"] > counts["matches"]
    assert counts["orphan_match_pages"] == 0
    assert conn.execute("PRAGMA foreign_key_check").fetchall() == []
    assert conn.execute(
        "SELECT count(*) FROM games WHERE game_id / 10 != match_id"
    ).fetchone() == (0,)
    assert conn.execute("SELECT count(*) FROM player_games").fetchone() == (0,)
    assert conn.execute(
        "SELECT tier, section, parent_title FROM events WHERE title='PGL/Wallachia/7/Group Stage'"
    ).fetchone() == ("tier1", "tier1", "PGL/Wallachia/7")
    assert conn.execute(
        "SELECT ordinal FROM matches WHERE page LIKE 'Match:ID y9zxBDdLAA%' ORDER BY page"
    ).fetchall() == [(0,), (1,), (2,), (3,)]
    assert conn.execute(
        "SELECT team1_side,winner FROM games WHERE dota_match_id=8719042091"
    ).fetchone() == ("dire", None)


def test_ownership_multiple_brackets_and_orphan(conn):
    text = match().replace("{{Match|", "{{MatchPage|")
    pages = {
        "P": record("P", 1, "{{Bracket|id=abcdefghij}}{{Matchlist|id=0123456789}}"),
        "Match:ID 0123456789 Z": record("Match:ID 0123456789 Z", 2, text),
        "Match:ID 0123456789 A": record(
            "Match:ID 0123456789 A", 3, text.replace("Jan 1", "Jan 2")
        ),
        "Match:ID zzzzzzzzzz A": record("Match:ID zzzzzzzzzz A", 4, text),
    }
    counts, errors = loader.build(conn, pages)
    assert not errors
    assert counts["orphan_match_pages"] == 1
    assert conn.execute("SELECT ordinal FROM matches ORDER BY ordinal").fetchall() == [
        (1000,),
        (1001,),
    ]


def test_inheritance_dedup_rosters_and_errors(conn):
    cards = "{{TeamCard|team=Alpha Gaming|p1=A|p2=B|p3=C|p4=D|p5=E}}"
    pages = {
        "P": record(
            "P", 1, "{{Infobox league|liquipediatier=1|leagueid=7}}" + cards + match()
        ),
        "P/Sub": record("P/Sub", 2, match()),
        "Bad": {"pageid": 3},
    }
    counts, errors = loader.build(conn, pages)
    assert (counts["matches"], counts["duplicates"], counts["parse_errors"]) == (
        1,
        1,
        1,
    )
    assert errors[0].startswith("Bad:")
    assert conn.execute("SELECT count(*) FROM rosters").fetchone() == (5,)
    assert conn.execute("SELECT count(*) FROM player_games").fetchone() == (0,)
    assert conn.execute(
        "SELECT leagueid FROM events WHERE title='P/Sub'"
    ).fetchone() == (7,)


def test_page_sql_failure_rolls_back(conn):
    broken = match().replace("|map1=", "|map01={{Map|winner=1}}|map1=")
    counts, errors = loader.build(
        conn, {"A": record("A", 1, broken), "B": record("B", 2, match())}
    )
    assert len(errors) == 1 and "IntegrityError" in errors[0]
    assert counts["matches"] == 1
    assert conn.execute("SELECT page FROM matches").fetchall() == [("B",)]


def test_setup_db_offline_from_fixture_cache(tmp_path, monkeypatch):
    monkeypatch.setenv("PROMDOTA_DATA", str(tmp_path / "raw"))
    pages = fixture_pages()
    for p in pages.values():
        cache.save_page(p)
    cache.save_index({title: {} for title in pages})
    od_record = json.loads(
        (ROOT / "tests/fixtures/od_match_8719042091.json").read_text()
    )
    od_cache.save(od_cache.game_file(8719042091), od_record)
    markets = json.loads(
        (ROOT / "tests/fixtures/kalshi/kalshi_dota_markets.json").read_text()
    )
    catalog = tmp_path / "raw/kalshi/markets"
    catalog.mkdir(parents=True)
    for kind, ticker in (("game", "KXDOTA2GAME"), ("map", "KXDOTA2MAP")):
        (catalog / f"{ticker}.json").write_text(json.dumps(markets[kind]))
    # Copy only build inputs so setup's relative db/ is isolated as well.
    project = tmp_path / "project"
    shutil.copytree(ROOT / "scripts", project / "scripts")
    (project / "promdota").symlink_to(ROOT / "promdota", target_is_directory=True)
    env = dict(
        os.environ,
        VIRTUAL_ENV=str(ROOT / ".venv"),
        UV_NO_SYNC="1",
        PYTHONPATH=str(ROOT),
    )
    shutil.copyfile(ROOT / "pyproject.toml", project / "pyproject.toml")
    (project / ".venv").symlink_to(ROOT / ".venv", target_is_directory=True)
    result = subprocess.run(
        ["bash", "scripts/setup_db.sh"],
        cwd=project,
        env=env,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    with sqlite3.connect(project / "db/dota2.db") as conn:
        assert conn.execute("SELECT count(*) FROM matches").fetchone()[0] > 0
        assert conn.execute("PRAGMA foreign_key_check").fetchall() == []
        assert conn.execute(
            "SELECT g.winner,g.winner_source,t.key FROM games g "
            "JOIN matches m USING(match_id) JOIN teams t ON t.team_id=m.team2_id "
            "WHERE g.dota_match_id=8719042091"
        ).fetchone() == (2, "opendota", "vici gaming")
        assert conn.execute("SELECT count(*) FROM player_games").fetchone() == (10,)
        assert conn.execute("SELECT count(*) FROM kalshi_markets").fetchone() == (4,)
    assert (project / "db/parse_errors.txt").read_text() == ""
