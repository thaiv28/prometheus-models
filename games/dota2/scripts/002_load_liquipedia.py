"""Build SQLite from the offline Liquipedia cache, isolating errors by page."""

import argparse
import hashlib
import sqlite3
import sys
import time
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from promdota.liquipedia import cache
from promdota.liquipedia.parse import (
    bracket_ids,
    fold,
    match_page_key,
    parse_infobox,
    parse_matches,
    roster_cards,
    section,
)
from promdota.liquipedia.regions import INTERNATIONAL_COUNTRIES, region


def stable_id(text):
    return int(hashlib.sha1(text.encode()).hexdigest()[:12], 16)


def insert(conn, table, rows):
    if not rows:
        return
    columns = ", ".join(f'"{k}"' for k in rows[0])
    placeholders = ", ".join("?" for _ in rows[0])
    conn.executemany(
        f"INSERT INTO {table} ({columns}) VALUES ({placeholders})",
        [list(row.values()) for row in rows],
    )


def ancestry(title):
    while title:
        yield title
        title = title.rpartition("/")[0]


def match_card(cards, key):
    key = fold(key)
    if key in cards:
        return cards[key]
    hits = [
        card
        for name, card in cards.items()
        if min(len(name), len(key)) >= 3 and (name in key or key in name)
    ]
    return hits[0] if len(hits) == 1 else None


def build(conn, pages: dict):
    """Load records into an empty schema; return counters and per-page errors."""
    conn.execute("PRAGMA foreign_keys = ON")
    counts, errors = Counter(pages=len(pages)), []
    parsed = {}
    for title, record in sorted(pages.items()):
        try:
            text = record["wikitext"]
            local = Counter()
            parsed[title] = (
                parse_infobox(text),
                roster_cards(text),
                parse_matches(title, text, counts=local),
            )
            # Validate identity before loading any rows for this page.
            int(record["pageid"])
            counts.update(local)
        except Exception as exc:
            parsed.pop(title, None)
            errors.append(f"{title}: {type(exc).__name__}: {exc}".replace("\n", " "))
    owners = {}
    for title in parsed:
        if not match_page_key(title):
            for position, bracket in enumerate(bracket_ids(pages[title]["wikitext"])):
                owners.setdefault(bracket, (title, position))
    match_keys = defaultdict(list)
    for title in parsed:
        if key := match_page_key(title):
            match_keys[key[0]].append(key[1])
    events = {}
    for title, (info, _, _) in parsed.items():
        if match_page_key(title):
            continue
        ancestors = [p for p in ancestry(title) if p in parsed]
        inherited = {
            k: next(
                (parsed[p][0][k] for p in ancestors if parsed[p][0][k] is not None),
                None,
            )
            for k in info
        }
        tier, country = inherited["tier"], inherited["country"]
        events[title] = {
            "event_id": int(pages[title]["pageid"]),
            "title": title,
            "parent_title": next(iter(ancestors[1:]), None),
            "name": inherited["name"],
            "tier": tier,
            "tier_type": inherited["tier_type"],
            "section": section(tier),
            "country": country,
            "region": region(country),
            "international": int(tier == "tier1" or country in INTERNATIONAL_COUNTRIES),
            "online": int(inherited["type"] == "Online"),
            "start_date": inherited["sdate"],
            "end_date": inherited["edate"],
            "mode": inherited["mode"],
            "prize_usd": inherited["prize_usd"],
            "excluded": int(
                (inherited["tier_type"] or "").lower() == "showmatch"
                or inherited["mode"] not in (None, "", "team")
            ),
            "revid": pages[title].get("revid"),
            "leagueid": inherited["leagueid"],
        }
    insert(conn, "events", list(events.values()))
    teams, players, rosters, names = {}, {}, {}, defaultdict(Counter)
    seen_ids, seen_games = set(), set()
    for title, (_, _, matches) in parsed.items():
        owner = title
        if key := match_page_key(title):
            if key[0] not in owners:
                counts["orphan_match_pages"] += 1
                continue
            owner, position = owners[key[0]]
            for m in matches:
                m.ordinal = position * 1000 + sorted(match_keys[key[0]]).index(key[1])
        event = events[owner]
        if event["excluded"]:
            continue
        source = next(
            (p for p in ancestry(owner) if p in parsed and parsed[p][1]), None
        )
        cards = parsed[source][1] if source else {}
        # A savepoint makes DB errors skip the entire page, including its matches.
        page_ids, page_games = set(), set()
        page_teams, page_players, page_rosters = {}, {}, {}
        page_names, page_counts = defaultdict(Counter), Counter()
        try:
            conn.execute("SAVEPOINT page")
            for m in matches:
                utc = m.start_utc.isoformat().replace("+00:00", "Z")
                keys = (m.team1_key, m.team2_key)
                mid = stable_id(f"match:{title}|{keys[0]}|{keys[1]}|{utc}|{m.ordinal}")
                # Normalize team orientation while retaining each game's identity.
                scores = tuple(
                    sorted(
                        (
                            (
                                g.dota_match_id,
                                g.winner
                                if keys[0] <= keys[1]
                                else (3 - g.winner if g.winner else None),
                            )
                            for g in m.games
                        ),
                        key=lambda item: str(item),
                    )
                )
                signature = (tuple(sorted(keys)), utc, scores)
                if (
                    mid in seen_ids
                    or mid in page_ids
                    or signature in seen_games
                    or signature in page_games
                ):
                    page_counts["duplicates"] += 1
                    continue
                lineups = []
                for key in keys:
                    tid = stable_id("team:" + key)
                    page_teams[tid] = {"team_id": tid, "key": key, "name": key}
                    card = match_card(cards, key)
                    lineups.append(card[1] if card else ())
                    if card:
                        page_names[key][card[0]] += 1
                        for slot, player in enumerate(card[1], 1):
                            pid = stable_id("player:" + player.key)
                            page_players[pid] = {
                                "player_id": pid,
                                "key": player.key,
                                "name": player.name,
                            }
                            eid = events[source]["event_id"]
                            page_rosters[eid, tid, slot] = {
                                "event_id": eid,
                                "team_id": tid,
                                "slot": slot,
                                "player_id": pid,
                            }
                # Insert dimensions first so all foreign keys are checked immediately.
                for table, existing, candidates in (
                    ("teams", teams, page_teams),
                    ("players", players, page_players),
                ):
                    id_column = "team_id" if table == "teams" else "player_id"
                    for row in candidates.values():
                        if row[id_column] not in existing:
                            conn.execute(
                                f"INSERT OR IGNORE INTO {table} VALUES (?, ?, ?)",
                                tuple(row.values()),
                            )
                wins1 = sum(g.winner == 1 for g in m.games)
                insert(
                    conn,
                    "matches",
                    [
                        {
                            "match_id": mid,
                            "event_id": event["event_id"],
                            "page": title,
                            "ordinal": m.ordinal,
                            "start_utc": utc,
                            "time_known": m.time_known,
                            "best_of": m.best_of,
                            "team1_id": stable_id("team:" + keys[0]),
                            "team2_id": stable_id("team:" + keys[1]),
                            "score1": wins1,
                            "score2": sum(g.winner == 2 for g in m.games),
                            "winner": m.winner,
                        }
                    ],
                )
                for game in m.games:
                    gid = mid * 10 + game.order
                    insert(
                        conn,
                        "games",
                        [
                            dict(
                                game_id=gid,
                                match_id=mid,
                                **asdict(game),
                                winner_source="liquipedia" if game.winner else None,
                            )
                        ],
                    )
                page_ids.add(mid)
                page_games.add(signature)
                page_counts["both_rosters"] += int(all(lineups))
            conn.execute("RELEASE page")
        except Exception as exc:
            conn.execute("ROLLBACK TO page")
            conn.execute("RELEASE page")
            errors.append(f"{title}: {type(exc).__name__}: {exc}".replace("\n", " "))
            continue
        teams.update(page_teams)
        players.update(page_players)
        rosters.update(page_rosters)
        for key, votes in page_names.items():
            names[key].update(votes)
        seen_ids.update(page_ids)
        seen_games.update(page_games)
        counts.update(page_counts)
    insert(conn, "rosters", list(rosters.values()))
    for row in teams.values():
        votes = names[row["key"]]
        if votes:
            conn.execute(
                "UPDATE teams SET name=? WHERE team_id=?",
                (votes.most_common(1)[0][0], row["team_id"]),
            )
    for table in ("events", "matches", "games"):
        counts[table] = conn.execute(f"SELECT count(*) FROM {table}").fetchone()[0]
    counts["excluded"] = sum(e["excluded"] for e in events.values())
    counts["parse_errors"] = len(errors)
    return counts, errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=REPO / "db/dota2.db")
    args = parser.parse_args(argv)
    start = time.monotonic()
    pages, read_errors = {}, []
    for title in sorted(cache.load_index()):
        try:
            record = cache.read_page(title)
            if record is None:
                raise ValueError("cached page missing")
            pages[title] = record
        except Exception as exc:
            read_errors.append(f"{title}: {type(exc).__name__}: {exc}")
    args.db.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(args.db) as conn:
        if not conn.execute(
            "SELECT 1 FROM sqlite_master WHERE name='events'"
        ).fetchone():
            conn.executescript((REPO / "scripts/001_create_tables.sql").read_text())
        counts, errors = build(conn, pages)
    errors = read_errors + errors
    (args.db.parent / "parse_errors.txt").write_text("".join(e + "\n" for e in errors))
    with sqlite3.connect(args.db) as conn:
        winners = conn.execute(
            "SELECT count(*) FROM games WHERE winner_source='liquipedia'"
        ).fetchone()[0]
    print(
        f"events={counts['events']} matches={counts['matches']} games={counts['games']} liquipedia_winners={winners} opendota_winners=0 games_with_players=0 orphan_match_pages={counts['orphan_match_pages']} winner_conflicts=0 parse_errors={len(errors)} seconds={time.monotonic() - start:.2f}"
    )


if __name__ == "__main__":
    main()
