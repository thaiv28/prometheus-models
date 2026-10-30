"""Offline raw-cache and Kaggle-to-Liquipedia roster linking checks."""

import csv
import io
import sqlite3
import zipfile
from datetime import date
from pathlib import Path

import pytest
from typer.testing import CliRunner

from promcs.kaggle import URL, fetch, latest_zip, load_latest, load_stats
from promcs.main import app

ROOT = Path(__file__).resolve().parents[1]


def test_fetch_bytes_cache_and_order(tmp_path):
    calls = []

    def get(url):
        calls.append(url)
        return b"unchanged\x00zip\xff"

    old = fetch(tmp_path, get=get, today=date(2026, 9, 30))
    newest = fetch(tmp_path, get=get, today=date(2026, 10, 29))
    assert newest.read_bytes() == b"unchanged\x00zip\xff"
    assert (
        fetch(
            tmp_path,
            get=lambda _: pytest.fail("fetched twice"),
            today=date(2026, 10, 29),
        )
        == newest
    )
    assert calls == [URL, URL]
    assert latest_zip(tmp_path) == newest
    assert old < newest
    assert not list(newest.parent.glob("*.tmp"))
    assert latest_zip(tmp_path / "absent") is None


def test_fetch_cli_cached(tmp_path, monkeypatch):
    monkeypatch.setenv("PROMCS_DATA", str(tmp_path))
    path = fetch(tmp_path, get=lambda _: b"raw")
    result = CliRunner().invoke(app, ["kaggle", "fetch"])
    assert result.exit_code == 0
    assert str(path) in result.stdout and "bytes=3" in result.stdout


@pytest.fixture
def db():
    with sqlite3.connect(":memory:") as conn:
        for script in ("001_create_tables.sql", "005_create_player_stats.sql"):
            conn.executescript((ROOT / "scripts" / script).read_text())
        # Built by 004_link_kalshi.py in setup_db.
        conn.execute(
            "CREATE TABLE team_aliases (competitor_id TEXT PRIMARY KEY, kalshi_name TEXT,"
            " kalshi_code TEXT, liquipedia_team_id INTEGER, liquipedia_name TEXT, events INTEGER)"
        )
        conn.execute(
            "INSERT INTO events(event_id,title,section,international,excluded) VALUES (1,'event','tier1',1,0)"
        )
        conn.executemany(
            "INSERT INTO teams VALUES (?, ?, ?)",
            [(1, "alpha", "Alpha"), (2, "beta", "Beta")],
        )
        conn.executemany(
            "INSERT INTO players VALUES (?, ?, ?)",
            [(i, f"p{i}", f"Name{i}") for i in range(1, 11)],
        )
        add_map(conn, 1)
        yield conn


def add_map(conn, gid, start="2026-01-01T00:00:00Z", scores=(13, 9)):
    conn.execute(
        "INSERT INTO matches(match_id,event_id,page,ordinal,start_utc,time_known,team1_id,team2_id,score1,score2) VALUES (?,1,'page',1,?,1,1,2,1,0)",
        (gid, start),
    )
    conn.execute(
        "INSERT INTO maps(game_id,match_id,\"order\",map,score1,score2,ot1,ot2) VALUES (?,?,1,'Dust II',?,?,0,0)",
        (gid, gid, *scores),
    )
    conn.executemany(
        "INSERT INTO player_maps VALUES (?, ?, ?)",
        [(gid, i, 1 if i <= 5 else 2) for i in range(1, 11)],
    )


def game(kid=101, overlap=10, **changes):
    row = {
        "game_id": kid,
        "is_total": "False",
        "datetime": "2026-01-01 03:00:00",
        "team1": "Unknown A",
        "team2": "Unknown B",
        "score1_game": "13.0",
        "score2_game": "9.0",
        "map_name": "Dust2",
    }
    for side in (1, 2):
        for i in range(1, 6):
            player = (side - 1) * 5 + i
            prefix = f"team{side}_player{i}"
            row[prefix] = (
                f"p{player} (Full Name), PL" if player <= overlap else "standin"
            )
            for stat, value in zip(
                ("kills", "deaths", "assists", "adr", "kast"),
                ("20.0", "12.0", "6.0", "80.5", "NaN"),
            ):
                row[f"{prefix}_{stat}"] = value
    return row | changes


def archive(tmp_path, rows):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=rows[0])
    writer.writeheader()
    writer.writerows(rows)
    path = tmp_path / "synthetic.zip"
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("cs2_all_tiers_games.csv", output.getvalue())
        z.writestr("cs2_tier1_games.csv", "should never read")
    return path


def test_shift_alias_name_key_stats_and_swapped(db, tmp_path):
    # Thirteen hours in Kaggle's naive clock is ten hours in UTC: inside the window.
    row = game(datetime="2026-01-01 13:00:00", score1_game="9", score2_game="13")
    for i in range(1, 6):
        row[f"team1_player{i}"] = f"Name{i + 5} (Person), FR"
        row[f"team2_player{i}"] = f"p{i}"
    row["team2_player5"] = "standin"
    summary = load_stats(db, archive(tmp_path, [row, game(102, is_total="True")]))
    assert db.execute("SELECT * FROM kaggle_links").fetchall() == [(101, 1, 1, 9)]
    assert db.execute("SELECT * FROM player_stats WHERE player_id=6").fetchone() == (
        1,
        6,
        2,
        20,
        12,
        6,
        80.5,
        None,
    )
    assert db.execute(
        "SELECT COUNT(*) FROM player_stats WHERE player_id=5"
    ).fetchone() == (0,)
    assert "map_rows=1 linked=1" in summary and ">=4/side=1/1 (100.0%)" in summary
    # Repeat load replaces derived data deterministically.
    assert load_stats(db, archive(tmp_path, [row])) == summary


@pytest.mark.parametrize(
    "overlap,teams,accepted",
    [(5, False, False), (6, False, False), (8, False, True), (0, True, True)],
)
def test_overlap_or_exact_teams(db, tmp_path, overlap, teams, accepted):
    row = game(overlap=overlap)
    if teams:
        row.update(team1="Alpha", team2="Beta")
    load_stats(db, archive(tmp_path, [row]))
    assert db.execute("SELECT COUNT(*) FROM kaggle_links").fetchone()[0] == int(
        accepted
    )


@pytest.mark.parametrize("alias", [False, True])
def test_side_without_roster_needs_name(db, tmp_path, alias):
    db.execute("DELETE FROM player_maps WHERE team = 2")
    if alias:
        db.execute(
            "INSERT INTO team_aliases VALUES ('c', 'Natus Vincere', 'NAVI', 2, 'beta', 1)"
        )
    load_stats(db, archive(tmp_path, [game(overlap=5, team2="Natus Vincere")]))
    assert db.execute("SELECT COUNT(*) FROM kaggle_links").fetchone() == (int(alias),)
    assert db.execute("SELECT COUNT(*) FROM player_stats").fetchone() == (5 * alias,)


def test_ambiguous_games_drop_tie(db, tmp_path):
    add_map(db, 2)
    load_stats(db, archive(tmp_path, [game()]))
    assert db.execute("SELECT COUNT(*) FROM kaggle_links").fetchone() == (0,)


@pytest.mark.parametrize(
    "overlaps,expected",
    [((6, 9), [(102, 1, 0, 9)]), ((9, 9), []), ((9, 9, 10), [(103, 1, 0, 10)])],
)
def test_one_link_per_game(db, tmp_path, overlaps, expected):
    load_stats(
        db,
        archive(tmp_path, [game(101 + i, overlap=n) for i, n in enumerate(overlaps)]),
    )
    assert db.execute("SELECT * FROM kaggle_links").fetchall() == expected


def test_best_other_game_and_orientation(db, tmp_path):
    add_map(db, 2)
    db.execute("DELETE FROM player_maps WHERE game_id=2 AND player_id IN (4,5)")
    load_stats(db, archive(tmp_path, [game()]))
    assert db.execute("SELECT game_id FROM kaggle_links").fetchall() == [(1,)]
    # Equal scores must consider swapped orientation too.
    db.execute("UPDATE maps SET score1=13, score2=13")
    db.execute("DELETE FROM player_maps WHERE game_id=2")
    row = game(score1_game="13", score2_game="13")
    for i in range(1, 6):
        row[f"team1_player{i}"] = f"p{i + 5}"
        row[f"team2_player{i}"] = f"p{i}"
    load_stats(db, archive(tmp_path, [row]))
    assert db.execute("SELECT game_id, swapped FROM kaggle_links").fetchall() == [
        (1, 1)
    ]


@pytest.mark.parametrize(
    "changes",
    [{"datetime": "2026-01-01 15:00:01"}, {"score2_game": "8"}, {"map_name": "Mirage"}],
)
def test_ineligible_candidates(db, tmp_path, changes):
    load_stats(db, archive(tmp_path, [game(**changes)]))
    assert db.execute("SELECT COUNT(*) FROM kaggle_links").fetchone() == (0,)


def test_missing_zip_skips(db, tmp_path):
    assert load_latest(db, tmp_path) == "kaggle: no dataset, skipped"


def full_game(kid=101, **changes):
    row = game(kid, **changes)
    for side in (1, 2):
        for i in range(1, 6):
            row[f"team{side}_player{i}_id"] = str((side - 1) * 5 + i)
    return row


def lineup(db, gid=1, side=1):
    return {
        r[0]
        for r in db.execute(
            "SELECT player_id FROM player_maps WHERE game_id=? AND team=?", (gid, side)
        )
    }


def test_learned_mapping_reuses_player_across_maps(db, tmp_path):
    add_map(db, 2, start="2026-01-02T00:00:00Z")
    row = full_game(102, datetime="2026-01-02 03:00:00", team1_player1="renamed")
    summary = load_stats(db, archive(tmp_path, [full_game(), row]))
    assert lineup(db, 2) == set(range(1, 6))
    assert db.execute(
        "SELECT player_id FROM player_stats WHERE game_id=2 ORDER BY player_id"
    ).fetchall() == [(i,) for i in range(1, 11)]
    assert "learned_mappings=10" in summary and "new_kaggle_players=0" in summary


def test_standin_replaces_roster_and_gets_stats(db, tmp_path):
    from promcs.kaggle import stable_id

    row = full_game(team1_player5="NewGuy (Full Name), GB")
    row["team1_player5_id"] = "999.0"
    summary = load_stats(db, archive(tmp_path, [row]))
    pid = stable_id("player:kaggle:999")
    assert lineup(db) == {1, 2, 3, 4, pid}
    assert db.execute(
        "SELECT key, name FROM players WHERE player_id=?", (pid,)
    ).fetchone() == ("kaggle:999", "NewGuy")
    assert db.execute("SELECT count(*) FROM player_stats").fetchone() == (10,)
    assert db.execute(
        "SELECT count(*) FROM player_stats WHERE player_id=5"
    ).fetchone() == (0,)
    assert "sides_replaced=2; lineups_changed=1; new_kaggle_players=1" in summary
    assert db.execute("PRAGMA foreign_key_check").fetchall() == []


def test_conflicting_lineups_leave_sides_unchanged(db, tmp_path):
    # Learn id 6 as LP player 6 on the other map, then try to put it on both sides.
    add_map(db, 2, start="2026-01-02T00:00:00Z")
    row = full_game(team1_player5="unknown")
    row["team1_player5_id"] = "6"
    summary = load_stats(
        db, archive(tmp_path, [row, full_game(102, datetime="2026-01-02 03:00:00")])
    )
    assert lineup(db) == set(range(1, 6))
    assert lineup(db, side=2) == set(range(6, 11))
    assert "sides_replaced=2; lineups_changed=0" in summary
    assert db.execute("PRAGMA foreign_key_check").fetchall() == []


@pytest.mark.parametrize("missing", ["team1_player5_id", "team1_player5"])
def test_incomplete_lineup_keeps_liquipedia(db, tmp_path, missing):
    row = full_game(team1_player4="standin")
    row[missing] = ""
    summary = load_stats(db, archive(tmp_path, [row]))
    assert lineup(db) == set(range(1, 6))
    assert "sides_replaced=1; lineups_changed=0; new_kaggle_players=0" in summary


def test_duplicate_resolved_players_keep_side(db, tmp_path):
    row = full_game(team1_player5="p4")
    summary = load_stats(db, archive(tmp_path, [row]))
    assert lineup(db) == set(range(1, 6))
    assert "sides_replaced=1" in summary


def test_full_lineup_populates_cardless_side(db, tmp_path):
    db.execute("DELETE FROM player_maps WHERE team=2")
    summary = load_stats(db, archive(tmp_path, [full_game(team2="Beta")]))
    assert len(lineup(db, side=2)) == 5
    assert db.execute("SELECT count(*) FROM player_stats").fetchone() == (10,)
    assert "lineups_changed=1; new_kaggle_players=0" in summary
    assert db.execute("PRAGMA foreign_key_check").fetchall() == []


def test_full_swapped_lineup_stats_keep_liquipedia_side(db, tmp_path):
    row = full_game(score1_game="9", score2_game="13")
    for i in range(1, 6):
        row[f"team1_player{i}"] = f"p{i + 5}"
        row[f"team1_player{i}_id"] = str(i + 5)
        row[f"team2_player{i}"] = f"p{i}"
        row[f"team2_player{i}_id"] = str(i)
    summary = load_stats(db, archive(tmp_path, [row]))
    assert lineup(db) == set(range(1, 6))
    assert db.execute(
        "SELECT count(*) FROM player_stats WHERE team=2 AND player_id>5"
    ).fetchone() == (5,)
    assert "sides_replaced=2; lineups_changed=0" in summary


def test_display_name_and_spelling_variants():
    from promcs.kaggle import assign_pairs, display_name, similar

    assert display_name("tex1y, RU") == "tex1y"
    assert display_name("OLIMP (Patryk  Woźniak ), PL") == "OLIMP"
    assert similar("device", "dev1ce") and similar("jotta", "jottaaa")
    assert similar("baz", "baaaazzz") and similar("ivz", "ivanzinho")
    assert not similar("zywoo", "apex")
    roster = {
        n: {i} for i, n in enumerate(["dev1ce", "staehr", "stavn", "hooxi", "jabbi"])
    }
    assert assign_pairs(roster, ["device", "staehr", "stavn", "hooxi", "jabbi"]) == {
        0: 0
    }
    assert assign_pairs(roster, ["stand1n", "staehr", "stavn", "hooxi", "jabbi"]) == {}


def test_two_unmatched_pairs_learn_and_resolve(db, tmp_path):
    db.execute("UPDATE players SET key='dev1ce', name='dev1ce' WHERE player_id=4")
    db.execute("UPDATE players SET key='jottaaa', name='jottAAA' WHERE player_id=5")
    row = full_game(team1_player4="device", team1_player5="jotta")
    summary = load_stats(db, archive(tmp_path, [row]))
    assert lineup(db) == set(range(1, 6))
    assert "pairs_assigned=2" in summary
    assert "learned_mappings=10" in summary
    assert "new_kaggle_players=0" in summary


def test_pair_assignment_ties_stop():
    from promcs.kaggle import assign_pairs

    assert assign_pairs({"abcd": {1}, "abce": {2}}, ["abcf", "abcg"]) == {}
    # Aliases do not cast multiple votes for the same person.
    assert assign_pairs({"abcd": {1}, "abcde": {1}}, ["abcdf", "zzz"]) == {0: 1}


@pytest.mark.parametrize("mode", ["team", "global", "ambiguous", "outside"])
def test_existing_player_fallback(db, tmp_path, mode):
    from promcs.kaggle import stable_id

    db.execute("INSERT INTO players VALUES (11,'unique (player)','Unique')")
    if mode == "global":
        # Only the key base matches: neither the name nor the full key does.
        db.execute("UPDATE players SET name='Different' WHERE player_id=11")
    if mode != "global":
        db.execute("INSERT INTO players VALUES (12,'unique (other player)','Unique')")
    if mode in ("team", "outside"):
        start = "2024-01-01T00:00:00Z" if mode == "outside" else "2026-01-02T00:00:00Z"
        add_map(db, 2, start=start)
        db.execute(
            "UPDATE player_maps SET player_id=11 WHERE game_id=2 AND player_id=5"
        )
    row = full_game(team1_player5="Unique")
    summary = load_stats(db, archive(tmp_path, [row]))
    expected = 11 if mode in ("team", "global") else stable_id("player:kaggle:5")
    assert lineup(db) == {1, 2, 3, 4, expected}
    assert f"fallback_resolved={int(expected == 11)}" in summary


def test_kid_unification_prefers_disambiguated(db, tmp_path):
    add_map(db, 2, start="2026-01-02T00:00:00Z")
    add_map(db, 3, start="2026-01-03T00:00:00Z")
    db.execute("INSERT INTO players VALUES (11,'p5 (french player)','p5')")
    db.execute("UPDATE player_maps SET player_id=11 WHERE game_id=2 AND player_id=5")
    rows = [
        full_game(),
        full_game(102, datetime="2026-01-02 03:00:00"),
        full_game(103, datetime="2026-01-03 03:00:00"),
    ]
    summary = load_stats(db, archive(tmp_path, rows))
    for gid in (1, 2, 3):
        assert lineup(db, gid) == {1, 2, 3, 4, 11}
    assert "kid_unified=1; kid_split_ids=0" in summary
    assert db.execute("PRAGMA foreign_key_check").fetchall() == []


@pytest.mark.parametrize("extra_maps,expected", [(False, 11), (True, 5)])
def test_kid_unification_frequency_and_map_count_tie(
    db, tmp_path, extra_maps, expected
):
    add_map(db, 2, start="2026-01-02T00:00:00Z")
    db.execute("INSERT INTO players VALUES (11,'alias','Alias')")
    db.execute("UPDATE player_maps SET player_id=11 WHERE game_id=2 AND player_id=5")
    add_map(db, 3, start="2026-01-03T00:00:00Z")
    db.execute("UPDATE player_maps SET player_id=11 WHERE game_id=3 AND player_id=5")
    rows = [
        full_game(),
        full_game(102, datetime="2026-01-02 03:00:00", team1_player5="Alias"),
    ]
    if extra_maps:
        rows.append(full_game(103, datetime="2026-01-03 03:00:00", team1_player5="p5"))
        # p5's exact key appears on map 4; it wins two slot votes to one.
        add_map(db, 4, start="2026-01-04T00:00:00Z")
        rows.append(full_game(104, datetime="2026-01-04 03:00:00"))
    summary = load_stats(db, archive(tmp_path, rows))
    assert lineup(db) == {1, 2, 3, 4, expected}
    assert "kid_unified=1; kid_split_ids=0" in summary


def test_unified_identity_conflict_restores_liquipedia(db, tmp_path):
    add_map(db, 2, start="2026-01-02T00:00:00Z")
    db.execute("INSERT INTO players VALUES (11,'p5 (french player)','p5')")
    db.execute("UPDATE player_maps SET player_id=11 WHERE game_id=2 AND player_id=5")
    db.execute("UPDATE player_maps SET player_id=11 WHERE game_id=1 AND player_id=6")
    rows = [
        full_game(team2_player1="p5"),
        full_game(102, datetime="2026-01-02 03:00:00"),
    ]
    load_stats(db, archive(tmp_path, rows))
    assert lineup(db) == set(range(1, 6))
    assert lineup(db, side=2) == {7, 8, 9, 10, 11}
    assert db.execute("PRAGMA foreign_key_check").fetchall() == []
