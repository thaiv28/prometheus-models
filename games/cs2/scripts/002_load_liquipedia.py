"""Build SQLite from the offline Liquipedia cache, isolating errors by page."""

import argparse
import sqlite3
import sys
import time
from bisect import bisect_left
from collections import Counter, defaultdict
from dataclasses import asdict
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from promcs.kaggle import stable_id
from promcs.liquipedia import cache
from promcs.liquipedia.parse import (
    fold,
    parse_infobox,
    parse_matches,
    roster_cards,
    section,
)
from promcs.liquipedia.regions import INTERNATIONAL_COUNTRIES, region


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


def confident_choices(votes, minimum=2):
    """Resolve only repeated, dominant evidence; ties cannot reach 80%."""
    result = {}
    for key, counts in votes.items():
        identity, count = counts.most_common(1)[0]
        if count >= minimum and count / counts.total() >= 0.8:
            result[key] = identity
    return result


def alias_votes(cards, keys):
    """One vote per page for unique unmatched, same-initial subsequences."""
    keys = set(keys)
    matched = {key: match_card(cards, key) for key in keys}
    used = {fold(card[0]) for card in matched.values() if card is not None}
    votes = {}
    for key in sorted(keys):
        if matched[key] is not None:
            continue
        folded = fold(key)
        hits = []
        for name in cards.keys() - used:
            letters = iter(name)
            if (
                folded
                and name.startswith(folded[0])
                and all(char in letters for char in folded)
            ):
                hits.append(name)
        if len(hits) == 1:
            votes[key] = Counter({hits[0]: 1})
    return votes


def resolved_card(cards, key, aliases):
    card = match_card(cards, key)
    return card if card is not None else cards.get(aliases.get(key))


def team_resolution(page_inputs):
    """Learn aliases, then card identities and canonical match keys."""
    votes = defaultdict(Counter)
    for cards, matches in page_inputs.values():
        keys = [key for m in matches for key in (m.team1_key, m.team2_key)]
        for key, counts in alias_votes(cards, keys).items():
            votes[key].update(counts)
    aliases = confident_choices(votes)
    identities, frequency = defaultdict(Counter), Counter()
    for cards, matches in page_inputs.values():
        for m in matches:
            for key in (m.team1_key, m.team2_key):
                frequency[key] += 1
                card = resolved_card(cards, key, aliases)
                if card is not None:
                    identities[key][fold(card[0])] += 1
    groups = defaultdict(list)
    for key, identity in confident_choices(identities).items():
        # "legacy (american team)" shares a card name with "legacy" but is not it.
        qualifier = key.partition("(")[2]
        groups[identity, qualifier].append(key)
    canonical = {}
    for members in groups.values():
        winner = min(members, key=lambda key: (-frequency[key], key))
        canonical.update((key, winner) for key in members)
    merged = [members for members in groups.values() if len(members) > 1]
    return aliases, canonical, sum(map(len, merged)), len(merged)


def resolve_bare_keys(conn):
    """Resolve bare cards from a frozen snapshot of nearby sibling appearances."""
    players = dict(conn.execute("SELECT key, player_id FROM players"))
    siblings = defaultdict(set)
    for key, pid in players.items():
        base, sep, qualifier = key.partition(" (")
        if sep and qualifier.endswith(")") and base in players:
            siblings[players[base]].add(pid)
    relevant = set(siblings) | set().union(*siblings.values()) if siblings else set()
    appearances = defaultdict(set)
    map_rows, occupants = [], defaultdict(set)
    for gid, pid, team, start in conn.execute(
        "SELECT p.game_id, p.player_id, CASE p.team WHEN 1 THEN m.team1_id "
        "ELSE m.team2_id END, substr(m.start_utc,1,10) FROM player_maps p "
        "JOIN maps g USING(game_id) JOIN matches m USING(match_id)"
    ):
        if pid not in relevant:
            continue
        day = date.fromisoformat(start).toordinal()
        appearances[pid, team].add(day)
        occupants[gid].add(pid)
        if pid in siblings:
            map_rows.append((gid, pid, team, day))
    appearances = {key: sorted(days) for key, days in appearances.items()}

    def candidate(pid, team, day):
        hits = []
        for sibling in siblings[pid]:
            days = appearances.get((sibling, team), [])
            i = bisect_left(days, day - 365)
            if i < len(days) and days[i] <= day + 365:
                hits.append(sibling)
        return hits[0] if len(hits) == 1 else None

    changes, touched = [], set()
    for gid, pid, team, day in map_rows:
        target = candidate(pid, team, day)
        if target is not None and target not in occupants[gid]:
            changes.append((target, gid, pid))
            touched.add(pid)
    roster_changes = []
    roster_rows = conn.execute(
        "SELECT r.event_id, r.team_id, r.slot, r.player_id, "
        "e.start_date, first_match.start FROM rosters r "
        "JOIN events e USING(event_id) LEFT JOIN "
        "(SELECT event_id, min(substr(start_utc,1,10)) start FROM matches GROUP BY event_id) "
        "first_match USING(event_id)"
    ).fetchall()
    roster_occupants = defaultdict(set)
    for eid, team, _slot, pid, _start, _first in roster_rows:
        roster_occupants[eid, team].add(pid)
    for eid, team, slot, pid, start, first in roster_rows:
        if pid not in siblings:
            continue
        # Liquipedia also stores partial event dates such as 2024-02-??.
        day = None
        for value in (start, first):
            try:
                day = date.fromisoformat((value or "")[:10]).toordinal()
                break
            except ValueError:
                continue
        if day is None:
            continue
        target = candidate(pid, team, day)
        if target is not None and target not in roster_occupants[eid, team]:
            roster_changes.append((target, eid, team, slot))
            touched.add(pid)
    conn.executemany(
        "UPDATE player_maps SET player_id=? WHERE game_id=? AND player_id=?", changes
    )
    conn.executemany(
        "UPDATE rosters SET player_id=? WHERE event_id=? AND team_id=? AND slot=?",
        roster_changes,
    )
    resolved = len(changes) + len(roster_changes)
    print(f"bare_keys_resolved={resolved} players={len(touched)}")
    return resolved, len(touched)


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
    events = {}
    for title, (info, _, _) in parsed.items():
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
            "international": int(tier == "S" or country in INTERNATIONAL_COUNTRIES),
            "online": int(inherited["type"] == "Online"),
            "start_date": inherited["sdate"],
            "end_date": inherited["edate"],
            "mode": inherited["mode"],
            "prize_usd": inherited["prize_usd"],
            "excluded": int(
                inherited["tier_type"] == "showmatch"
                or inherited["mode"] not in (None, "", "team")
            ),
            "revid": pages[title].get("revid"),
        }
    insert(conn, "events", list(events.values()))
    page_inputs, sources = {}, {}
    for title, (_, _, matches) in parsed.items():
        if events[title]["excluded"]:
            continue
        source = next(
            (p for p in ancestry(title) if p in parsed and parsed[p][1]), None
        )
        sources[title] = source
        page_inputs[title] = (parsed[source][1] if source else {}, matches)
    aliases, canonical, merged_keys, merged_groups = team_resolution(page_inputs)
    counts.update(
        aliases_resolved=len(aliases),
        merged_keys=merged_keys,
        merged_groups=merged_groups,
    )
    teams, players, rosters, names = {}, {}, {}, defaultdict(Counter)
    seen_ids, seen_games = set(), set()
    for title, (cards, matches) in page_inputs.items():
        event, source = events[title], sources[title]
        # A savepoint makes DB errors skip the entire page, including its matches.
        page_ids, page_games = set(), set()
        page_teams, page_players, page_rosters = {}, {}, {}
        page_names, page_counts = defaultdict(Counter), Counter()
        try:
            conn.execute("SAVEPOINT page")
            for m in matches:
                utc = m.start_utc.isoformat().replace("+00:00", "Z")
                keys = (m.team1_key, m.team2_key)
                mid = (
                    stable_id(f"hltv:{m.hltv_id}")
                    if m.hltv_id
                    else stable_id(
                        f"match:{title}|{keys[0]}|{keys[1]}|{utc}|{m.ordinal}"
                    )
                )
                # Normalize scores to sorted team order, preserving team association.
                scores = tuple(
                    sorted(
                        (g.score1, g.score2)
                        if keys[0] <= keys[1]
                        else (g.score2, g.score1)
                        for g in m.maps
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
                    canonical_key = canonical.get(key, key)
                    tid = stable_id("team:" + canonical_key)
                    page_teams[tid] = {
                        "team_id": tid,
                        "key": canonical_key,
                        "name": canonical_key,
                    }
                    card = resolved_card(cards, key, aliases)
                    lineups.append(card[1] if card else ())
                    if card:
                        page_names[canonical_key][card[0]] += 1
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
                wins1 = sum(g.score1 > g.score2 for g in m.maps)
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
                            "team1_id": stable_id(
                                "team:" + canonical.get(keys[0], keys[0])
                            ),
                            "team2_id": stable_id(
                                "team:" + canonical.get(keys[1], keys[1])
                            ),
                            "score1": wins1,
                            "score2": len(m.maps) - wins1,
                            "winner": m.winner,
                            "hltv_id": m.hltv_id,
                        }
                    ],
                )
                overlap = {p.key for p in lineups[0]} & {p.key for p in lineups[1]}
                for game in m.maps:
                    gid = mid * 10 + game.order
                    insert(
                        conn, "maps", [dict(game_id=gid, match_id=mid, **asdict(game))]
                    )
                    rows = {
                        p.key: {
                            "game_id": gid,
                            "player_id": stable_id("player:" + p.key),
                            "team": side,
                        }
                        for side, lineup in enumerate(lineups, 1)
                        for p in lineup
                        if p.key not in overlap
                    }
                    insert(conn, "player_maps", list(rows.values()))
                    page_counts["players_both_sides"] += len(overlap)
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
    resolve_bare_keys(conn)
    for table in ("events", "matches", "maps"):
        counts[table] = conn.execute(f"SELECT count(*) FROM {table}").fetchone()[0]
    counts["excluded"] = sum(e["excluded"] for e in events.values())
    counts["parse_errors"] = len(errors)
    return counts, errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=REPO / "db/cs2.db")
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
    print(
        f"pages={len(pages) + len(read_errors)} events={counts['events']} excluded={counts['excluded']}"
    )
    print(
        f"matches={counts['matches']} maps={counts['maps']} duplicates={counts['duplicates']}"
    )
    pct = counts["both_rosters"] / counts["matches"] if counts["matches"] else 0
    print(
        f"aliases_resolved={counts['aliases_resolved']} teams_merged={counts['merged_keys']} keys -> {counts['merged_groups']} groups"
    )
    print(f"both_rosters={counts['both_rosters']} ({pct:.1%})")
    print(
        f"unknown_tz={counts['unknown_tz']} dateless={counts['dateless']} map_order_gt9={counts['map_order_gt9']} players_both_sides={counts['players_both_sides']}"
    )
    print(f"parse_errors={len(errors)} seconds={time.monotonic() - start:.2f}")


if __name__ == "__main__":
    main()
