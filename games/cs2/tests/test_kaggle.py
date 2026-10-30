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
