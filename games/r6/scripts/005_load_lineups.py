"""Fill map lineups from offline siege.gg pages and complete Liquipedia cards."""

import argparse
import hashlib
import os
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from promr6.link import normalize
from promr6.siegegg import cache
from promr6.siegegg.parse import parse_match


def stable_id(text):
    return int(hashlib.sha1(text.encode()).hexdigest()[:12], 16)


def fold(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


def orientation(match, siege, maps):
    """Return siege teams in database order, requiring a unique orientation."""
    teams = (siege.team1, siege.team2)

    def similar(a, b):
        a, b = "".join(normalize(a)), "".join(normalize(b))
        return bool(a and b) and (
            a == b or (min(len(a), len(b)) >= 3 and (a in b or b in a))
        )

    orders = (teams, teams[::-1])
    votes = [
        sum(similar(t.name, match[f"name{i}"]) for i, t in enumerate(order, 1))
        for order in orders
    ]
    if max(votes) > 0 and votes[0] != votes[1]:
        return orders[votes.index(max(votes))]
    scores = [(match["score1"], match["score2"])]
    if len(maps) == 1:
        scores.append((maps[0]["rounds1"], maps[0]["rounds2"]))
    candidates = [
        order
        for order in (teams, teams[::-1])
        if tuple(t.score for t in order) in scores
    ]
    return candidates[0] if len(candidates) == 1 else None


def build(conn):
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    counts = Counter()
    matches = conn.execute(
        "SELECT m.*, a.name AS name1, b.name AS name2 FROM matches m "
        "JOIN teams a ON a.team_id=m.team1_id JOIN teams b ON b.team_id=m.team2_id "
        "ORDER BY start_utc, match_id"
    ).fetchall()
    maps = defaultdict(list)
    for row in conn.execute("SELECT * FROM maps ORDER BY map_order"):
        maps[row["match_id"]].append(row)
    events = {r["event_id"]: r for r in conn.execute("SELECT * FROM events")}
    titles = {r["title"]: r["event_id"] for r in events.values()}
    cards = defaultdict(list)
    for row in conn.execute(
        "SELECT r.*, p.name FROM rosters r JOIN players p USING(player_id) ORDER BY slot"
    ):
        cards[row["event_id"], row["team_id"]].append(row)
    substitutions = defaultdict(list)
    for row in conn.execute("SELECT * FROM match_substitutions"):
        substitutions[row["match_id"], row["side"]].append(row)
    lineups, nicknames = {}, defaultdict(Counter)
    global_names, team_names = defaultdict(set), defaultdict(list)
    parsed, voted = {}, set()
    for match in matches:
        counts["matches"] += 1
        sid, mid = match["siegegg_id"], match["match_id"]
        if sid is None:
            continue
        counts["with_siegegg_id"] += 1
        if sid not in parsed:
            body = cache.read_match(sid)
            parsed[sid] = (body is not None, parse_match(body) if body else None)
        cached, siege = parsed[sid]
        counts["siegegg_cached"] += cached
        if siege is None or not siege.finished:
            continue
        oriented = orientation(match, siege, maps[mid])
        if oriented is None:
            counts["orientation_failed"] += 1
            continue
        for side, team in enumerate(oriented, 1):
            for player in team.players:
                pid, name = player.siegegg_player_id, player.nickname
                if sid not in voted:
                    nicknames[pid][name] += 1
                global_names[fold(name)].add(pid)
                team_names[match[f"team{side}_id"], fold(name)].append(
                    (datetime.fromisoformat(match["start_utc"]), pid)
                )
            if len(team.players) < 4:
                counts["short_siegegg_side"] += 1
                continue
            counts["long_siegegg_side"] += len(team.players) > 5
            lineups[mid, side] = [
                f"siegegg:{p.siegegg_player_id}" for p in team.players
            ]

        voted.add(sid)

    def player(key, name):
        pid = stable_id("player:" + key)
        conn.execute(
            "INSERT INTO players VALUES (?, ?, ?) ON CONFLICT(player_id) DO UPDATE SET name=excluded.name",
            (pid, key, name),
        )
        return pid

    for pid, names in nicknames.items():
        player(f"siegegg:{pid}", names.most_common(1)[0][0])

    def identify(name, team_id, date):
        folded = fold(name)
        local = {
            pid
            for when, pid in team_names[team_id, folded]
            if abs((date - when).total_seconds()) <= 365 * 86400
        }
        hits = local if len(local) == 1 else global_names[folded]
        if len(hits) == 1:
            return stable_id(f"player:siegegg:{next(iter(hits))}")
        return player("liquipedia:" + folded, name)

    conn.execute("DELETE FROM player_maps")
    for match in matches:
        mid = match["match_id"]
        for side in (1, 2):
            keys = lineups.get((mid, side))
            source = "siegegg" if keys else "liquipedia"
            ids = [stable_id("player:" + key) for key in keys] if keys else []
            if not keys:
                eid, tid = match["event_id"], match[f"team{side}_id"]
                card = []
                while eid is not None:
                    card = cards[eid, tid]
                    if card:
                        break
                    eid = titles.get(events[eid]["parent_title"])
                if card and all(r["complete"] for r in card):
                    names = {fold(r["name"]): r["name"] for r in card}
                    for sub in substitutions[mid, side]:
                        names.pop(fold(sub["player_out"]), None)
                        names[fold(sub["player_in"])] = sub["player_in"]
                    date = datetime.fromisoformat(match["start_utc"])
                    ids = [identify(name, tid, date) for name in names.values()]
            if ids:
                counts[source + "_lineups"] += 1
                conn.executemany(
                    "INSERT OR IGNORE INTO player_maps VALUES (?, ?, ?, ?)",
                    [
                        (m["map_id"], side, pid, source)
                        for m in maps[mid]
                        for pid in ids
                    ],
                )
            else:
                counts["no_lineup_sides"] += 1
    for table in ("player_maps", "players"):
        counts[table] = conn.execute(f"SELECT count(*) FROM {table}").fetchone()[0]
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--db", type=Path, default=Path(os.environ.get("PROMR6_DB", REPO / "db/r6.db"))
    )
    args = parser.parse_args()
    with sqlite3.connect(args.db) as conn:
        counts = build(conn)
    fields = "matches with_siegegg_id siegegg_cached siegegg_lineups liquipedia_lineups no_lineup_sides orientation_failed short_siegegg_side long_siegegg_side player_maps players"
    print(" ".join(f"{key}={counts[key]}" for key in fields.split()))


if __name__ == "__main__":
    main()
