"""Enrich Liquipedia games using only the local OpenDota cache."""

import argparse
import hashlib
import os
import sqlite3
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from promdota.opendota import cache


def stable_id(text):
    return int(hashlib.sha1(text.encode()).hexdigest()[:12], 16)


def build(conn, records=None):
    records = cache.load_records() if records is None else records
    conn.row_factory = sqlite3.Row
    counts = Counter()
    games = conn.execute(
        "SELECT g.*, m.team1_id, m.team2_id FROM games g JOIN matches m USING(match_id)"
    ).fetchall()
    # Seed identities using explicit Liquipedia sides before resolving unknown sides.
    votes = Counter()
    for game in games:
        record = records.get(game["dota_match_id"])
        if not record or game["team1_side"] is None:
            continue
        radiant = (
            game["team1_id"] if game["team1_side"] == "radiant" else game["team2_id"]
        )
        dire = game["team2_id"] if game["team1_side"] == "radiant" else game["team1_id"]
        for od_id, team_id in (
            (record.get("radiant_team_id"), radiant),
            (record.get("dire_team_id"), dire),
        ):
            if od_id:
                votes[od_id, team_id] += 1
    for od_id, team_id, n in conn.execute("SELECT * FROM opendota_teams"):
        votes[od_id, team_id] = max(votes[od_id, team_id], n)
    for game in games:
        record = records.get(game["dota_match_id"])
        if not record:
            continue
        side = game["team1_side"]
        if side is None:
            candidates = {
                team
                for (od_id, team), n in votes.items()
                if od_id == record.get("radiant_team_id")
                and n > 0
                and team in (game["team1_id"], game["team2_id"])
            }
            if len(candidates) != 1:
                continue
            side = "radiant" if candidates.pop() == game["team1_id"] else "dire"
            conn.execute(
                "UPDATE games SET team1_side=? WHERE game_id=?", (side, game["game_id"])
            )
        win = record.get("radiant_win")
        if win is not None:
            winner = 1 if bool(win) == (side == "radiant") else 2
            if game["winner"] is None:
                conn.execute(
                    "UPDATE games SET winner=?,winner_source='opendota' WHERE game_id=?",
                    (winner, game["game_id"]),
                )
            elif game["winner"] != winner and game["winner_source"] == "liquipedia":
                counts["winner_conflicts"] += 1
        if record.get("duration") is not None:
            conn.execute(
                "UPDATE games SET duration_s=COALESCE(duration_s,?) WHERE game_id=?",
                (record["duration"], game["game_id"]),
            )
        for player in record.get("players", []):
            if player.get("account_id") is None or player.get("player_slot") is None:
                continue
            key = f"steam:{player['account_id']}"
            pid = stable_id("player:" + key)
            conn.execute(
                "INSERT OR IGNORE INTO players VALUES(?,?,?)",
                (pid, key, str(player["account_id"])),
            )
            radiant = player["player_slot"] < 128
            team = 1 if radiant == (side == "radiant") else 2
            conn.execute(
                "INSERT OR REPLACE INTO player_games VALUES(?,?,?,?,?,?,?,?,?)",
                (
                    game["game_id"],
                    pid,
                    team,
                    player.get("hero_id"),
                    player.get("kills"),
                    player.get("deaths"),
                    player.get("assists"),
                    player.get("gold_per_min"),
                    player.get("xp_per_min"),
                ),
            )
    # Rebuild votes after inferred sides, counting one vote for each game/team pair.
    conn.execute("DELETE FROM opendota_teams")
    votes.clear()
    for game in conn.execute(
        "SELECT g.*,m.team1_id,m.team2_id FROM games g JOIN matches m USING(match_id)"
    ):
        record = records.get(game["dota_match_id"])
        if not record or game["team1_side"] is None:
            continue
        tids = (game["team1_id"], game["team2_id"])
        if game["team1_side"] == "dire":
            tids = tids[::-1]
        for od, tid in zip(
            (record.get("radiant_team_id"), record.get("dire_team_id")), tids
        ):
            if od:
                votes[od, tid] += 1
    conn.executemany(
        "INSERT INTO opendota_teams VALUES(?,?,?)",
        [(od, tid, n) for (od, tid), n in votes.items()],
    )
    # Unresolved matches stay (winner NULL): `promdota opendota games` reads their
    # match IDs from this DB, and Kalshi links can target them.
    empty = conn.execute(
        "SELECT count(*) FROM (SELECT match_id FROM games GROUP BY match_id HAVING count(winner)=0)"
    ).fetchone()[0]
    counts["unresolved_matches"] = empty
    for row in conn.execute(
        "SELECT match_id,sum(winner=1),sum(winner=2),count(*),count(winner) FROM games GROUP BY match_id"
    ).fetchall():
        mid, first, second, total, resolved = row
        winner = (
            (1 if first > second else 2)
            if first != second and resolved == total
            else None
        )
        conn.execute(
            "UPDATE matches SET score1=?,score2=?,winner=? WHERE match_id=?",
            (first or 0, second or 0, winner, mid),
        )
    for table in ("events", "matches", "games"):
        counts[table] = conn.execute(f"SELECT count(*) FROM {table}").fetchone()[0]
    for source, n in conn.execute(
        "SELECT winner_source,count(*) FROM games WHERE winner IS NOT NULL GROUP BY winner_source"
    ):
        counts[f"winners_{source}"] = n
    counts["games_with_players"] = conn.execute(
        "SELECT count(DISTINCT game_id) FROM player_games"
    ).fetchone()[0]
    return counts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--db",
        type=Path,
        default=Path(os.environ.get("PROMDOTA_DB", REPO / "db/dota2.db")),
    )
    args = parser.parse_args(argv)
    with sqlite3.connect(args.db) as conn:
        counts = build(conn)
    print(
        " ".join(
            f"{key}={counts[key]}"
            for key in (
                "events",
                "matches",
                "games",
                "winners_liquipedia",
                "winners_opendota",
                "games_with_players",
                "winner_conflicts",
                "unresolved_matches",
            )
        )
        + " parse_errors=0"
    )


if __name__ == "__main__":
    main()
