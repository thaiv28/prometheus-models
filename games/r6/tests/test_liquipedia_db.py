"""Build the R6 database entirely from fixture caches."""

import importlib.util
import json
import os
import sqlite3
import subprocess
from pathlib import Path

import pytest

from promr6.liquipedia import cache

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
    pages = {}
    for path in sorted((ROOT / "tests/fixtures/liquipedia").glob("page*.json")):
        raw = json.loads(path.read_text())
        for page in raw["query"]["pages"].values():
            revision = page["revisions"][0]
            pages[page["title"]] = {
                "title": page["title"],
                "pageid": page["pageid"],
                "revid": revision["revid"],
                "wikitext": revision["slots"]["main"]["*"],
            }
    return pages


def record(title, pid, text):
    return {"title": title, "pageid": pid, "revid": 1, "wikitext": text}


def match():
    return (
        "{{Match|opponent1={{TeamOpponent|Alpha}}|opponent2={{TeamOpponent|Beta}}"
        "|date=2026-01-01 10:00 {{Abbr/UTC}}|finished=true|siegegg=123"
        "|map1={{Map|map=Villa|finished=true|score1=7|score2=3}}}}"
    )


def test_fixture_build(conn):
    counts, errors = loader.build(conn, fixture_pages())
    assert errors == []
    assert counts["events"] == 8
    assert counts["matches"] > 45
    assert counts["maps"] > counts["matches"]
    assert counts["walkovers"] > 0
    assert conn.execute("PRAGMA foreign_key_check").fetchall() == []
    assert conn.execute("SELECT count(*) FROM player_maps").fetchone() == (0,)
    assert (
        conn.execute("SELECT count(*) FROM rosters WHERE complete=0").fetchone()[0] > 0
    )
    row = conn.execute(
        "SELECT score1,score2,m.winner,map_name,rounds1,rounds2,p.winner "
        "FROM matches m JOIN maps p USING(match_id) WHERE siegegg_id=6168"
    ).fetchone()
    assert row == (0, 1, 2, "Villa", 3, 7, 2)
    assert conn.execute(
        "SELECT side,player_in,player_out FROM match_substitutions "
        "JOIN matches USING(match_id) WHERE siegegg_id=6168"
    ).fetchone() == (1, "Koshi", "J9O")
    assert conn.execute(
        "SELECT count(*) FROM matches WHERE walkover=1 AND winner IS NOT NULL"
    ).fetchone() == (0,)
    assert conn.execute(
        "SELECT tier,parent_title FROM events WHERE title LIKE '%Stage 2/Group Stage' "
        "AND title LIKE 'North America%'"
    ).fetchone() == ("tier2", "North America League/2026/Stage 2")


def test_inheritance_dedup_and_parse_errors(conn):
    pages = {
        "P": record("P", 1, "{{Infobox league|liquipediatier=2}}" + match()),
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
    assert conn.execute("SELECT tier FROM events WHERE title='P/Sub'").fetchone() == (
        "tier2",
    )


def test_unresolved_finished_match_is_counted(conn):
    text = match().replace(
        "|map1={{Map|map=Villa|finished=true|score1=7|score2=3}}", ""
    )
    counts, errors = loader.build(conn, {"P": record("P", 1, text)})
    assert not errors
    assert counts["unresolved_matches"] == 1
    assert conn.execute("SELECT score1,score2,winner FROM matches").fetchone() == (
        0,
        0,
        None,
    )


def test_sql_failure_rolls_back_only_affected_page(conn, monkeypatch):
    from dataclasses import replace

    parse = loader.parse_matches

    def invalid_map(title, text, counts):
        matches = parse(title, text, counts=counts)
        if title == "Bad":
            matches[0].maps[0] = replace(matches[0].maps[0], order=0)
        return matches

    monkeypatch.setattr(loader, "parse_matches", invalid_map)
    counts, errors = loader.build(
        conn, {"Bad": record("Bad", 1, match()), "Good": record("Good", 2, match())}
    )
    assert len(errors) == 1 and "IntegrityError" in errors[0]
    assert counts["matches"] == 1
    assert conn.execute("SELECT page FROM matches").fetchall() == [("Good",)]


def test_same_page_under_two_spellings_loads_once(conn):
    text = "{{Infobox league|name=X|liquipediatier=3}}"
    pages = {
        "Root/A  B": record("Root/A  B", 7, text),
        "Root/A B": record("Root/A B", 7, text),
        "Root#Part": record("Root#Part", 8, text),
        "Root": record("Root", 8, text),
    }
    counts, errors = loader.build(conn, pages)
    assert [r[0] for r in conn.execute("SELECT title FROM events ORDER BY title")] == [
        "Root",
        "Root/A B",
    ]
    assert counts["duplicate_pages"] == 2
    assert not errors


def test_setup_db_offline_from_fixture_cache(tmp_path, monkeypatch):
    monkeypatch.setenv("PROMR6_DATA", str(tmp_path / "raw"))
    pages = fixture_pages()
    for page in pages.values():
        cache.save_page(page)
    cache.save_index({title: {} for title in pages})
    markets = json.loads(
        (ROOT / "tests/fixtures/kalshi/markets_sample.json").read_text()
    )
    catalog = tmp_path / "raw/kalshi/markets"
    catalog.mkdir(parents=True)
    for series, rows in markets.items():
        (catalog / f"{series}.json").write_text(json.dumps(rows))
    import shutil

    from promr6.siegegg import cache as siege_cache

    siege_file = siege_cache.match_file(6168)
    siege_file.parent.mkdir(parents=True)
    shutil.copyfile(ROOT / "tests/fixtures/siegegg/match_6168.html.gz", siege_file)
    siege_cache.save_index({"6168": {"status": 200, "finished": True}})
    database = tmp_path / "db/r6.db"
    env = dict(os.environ, PROMR6_DB=str(database), UV_OFFLINE="1", UV_NO_SYNC="1")
    result = subprocess.run(
        ["bash", "scripts/setup_db.sh"],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    with sqlite3.connect(database) as connection:
        for table in ("events", "matches", "maps", "kalshi_markets"):
            assert connection.execute(f"SELECT count(*) FROM {table}").fetchone()[0] > 0
        assert connection.execute("SELECT count(*) FROM player_maps").fetchone()[0] > 0
        assert connection.execute(
            "SELECT count(*) FROM player_maps JOIN maps USING(map_id) "
            "JOIN matches USING(match_id) WHERE siegegg_id=6168 AND source='siegegg'"
        ).fetchone() == (10,)
        assert connection.execute("PRAGMA foreign_key_check").fetchall() == []
    assert (database.parent / "parse_errors.txt").read_text() == ""
    assert (database.parent / "link_report.txt").exists()


lineup_spec = importlib.util.spec_from_file_location(
    "load_lineups", ROOT / "scripts/004_load_lineups.py"
)
lineups = importlib.util.module_from_spec(lineup_spec)
lineup_spec.loader.exec_module(lineups)


@pytest.fixture
def lineup_db(conn, tmp_path, monkeypatch):
    import shutil

    from promr6.siegegg import cache as siege_cache

    monkeypatch.setenv("PROMR6_DATA", str(tmp_path / "raw"))
    loader.build(conn, fixture_pages())
    target = siege_cache.match_file(6168)
    target.parent.mkdir(parents=True)
    shutil.copyfile(ROOT / "tests/fixtures/siegegg/match_6168.html.gz", target)
    siege_cache.save_index({"6168": {"status": 200, "finished": True}})
    return conn


def test_siege_lineups_and_score_orientation(lineup_db):
    conn = lineup_db
    for swapped in (False, True):
        if swapped:
            # Unknown names force the one-map round score fallback, reversed.
            conn.execute("UPDATE teams SET name='Unknown ' || team_id")
            conn.execute(
                "UPDATE matches SET team1_id=team2_id, team2_id=team1_id, "
                "score1=score2, score2=score1 WHERE siegegg_id=6168"
            )
            conn.execute(
                "UPDATE maps SET rounds1=rounds2, rounds2=rounds1 WHERE match_id IN "
                "(SELECT match_id FROM matches WHERE siegegg_id=6168)"
            )
        counts = lineups.build(conn)
        rows = conn.execute(
            "SELECT team_side,p.key,p.name,source FROM player_maps pm "
            "JOIN players p USING(player_id) JOIN maps USING(map_id) "
            "JOIN matches USING(match_id) WHERE siegegg_id=6168"
        ).fetchall()
        assert len(rows) == 10
        assert all(r[3] == "siegegg" for r in rows)
        assert (2 if swapped else 1, "siegegg:1077", "Fultz", "siegegg") in [
            tuple(r) for r in rows
        ]
        assert counts["siegegg_lineups"] == 2
        siege = conn.execute(
            "SELECT siegegg_team_id, name FROM team_siegegg"
        ).fetchall()
        assert {(725, "Wildcard"), (465, "DarkZero Esports")} <= set(map(tuple, siege))
        assert conn.execute("PRAGMA foreign_key_check").fetchall() == []


def test_complete_card_substitution_and_identity(lineup_db):
    conn = lineup_db
    match = conn.execute("SELECT * FROM matches WHERE siegegg_id=6168")
    columns = [c[0] for c in match.description]
    match = dict(zip(columns, match.fetchone()))
    eid, tid = match["event_id"], match["team1_id"]
    conn.execute("DELETE FROM rosters WHERE event_id=? AND team_id=?", (eid, tid))
    for slot, name in enumerate(("Fultz", "Nuers", "njr", "Kyno", "J9O"), 1):
        pid = loader.stable_id("test:" + name)
        conn.execute(
            "INSERT INTO players VALUES (?, ?, ?)", (pid, "test:" + name, name)
        )
        conn.execute(
            "INSERT INTO rosters VALUES (?, ?, ?, ?, 1)", (eid, tid, slot, pid)
        )
    # A second match has no siege page and uses the inherited complete card.
    copy = dict(match, match_id=42, siegegg_id=None)
    loader.insert(conn, "matches", [copy])
    conn.execute("INSERT INTO maps(map_id,match_id,map_order) VALUES (421,42,1)")
    conn.execute("INSERT INTO match_substitutions VALUES (42,1,'Koshi','j9o')")
    lineups.build(conn)
    rows = conn.execute(
        "SELECT p.key,pm.source FROM player_maps pm JOIN players p USING(player_id) "
        "WHERE map_id=421 AND team_side=1"
    ).fetchall()
    assert {r[0] for r in rows} == {
        "siegegg:1077",
        "siegegg:2935",
        "siegegg:1809",
        "siegegg:1871",
        "siegegg:3925",
    }
    assert all(r[1] == "liquipedia" for r in rows)
    conn.execute(
        "UPDATE rosters SET complete=0 WHERE event_id=? AND team_id=?", (eid, tid)
    )
    lineups.build(conn)
    assert (
        conn.execute(
            "SELECT count(*) FROM player_maps WHERE map_id=421 AND team_side=1"
        ).fetchone()[0]
        == 0
    )


@pytest.mark.parametrize("size,short,long", [(3, 1, 0), (4, 0, 0), (6, 0, 1)])
def test_siege_side_sizes(lineup_db, monkeypatch, size, short, long):
    from dataclasses import replace

    from promr6.siegegg.parse import SiegePlayer

    parse = lineups.parse_match

    def resized(body):
        siege = parse(body)
        players = siege.team1.players + (SiegePlayer("Extra", 999999),)
        return replace(siege, team1=replace(siege.team1, players=players[:size]))

    monkeypatch.setattr(lineups, "parse_match", resized)
    lineup_db.execute("DELETE FROM rosters")
    counts = lineups.build(lineup_db)
    assert counts["short_siegegg_side"] == short
    assert counts["long_siegegg_side"] == long
    assert counts["siegegg_lineups"] == (1 if short else 2)
    assert counts["player_maps"] == (5 if short else 5 + size)


def test_orientation_names_and_ambiguity():
    from promr6.siegegg.parse import SiegeMatch, SiegeTeam

    alpha = SiegeTeam("Alpha Esports", None, 1, ())
    beta = SiegeTeam("Unknown", None, 1, ())
    siege = SiegeMatch(alpha, beta, "2026-09-09T18:00:00Z", None, (), True)
    row = {
        "name1": "Beta",
        "name2": "Alpha",
        "score1": 1,
        "score2": 1,
        "start_utc": "2026-09-10T12:00:00Z",
    }
    assert lineups.orientation(row, siege, []) == (beta, alpha)
    # A page more than 48 hours away is another match behind a wrong ID.
    assert (
        lineups.orientation({**row, "start_utc": "2026-09-12T12:00:00Z"}, siege, [])
        is None
    )
    assert (
        lineups.orientation(row, SiegeMatch(alpha, beta, None, None, (), True), [])
        is None
    )
    row["name2"] = "Other"
    assert lineups.orientation(row, siege, []) is None
