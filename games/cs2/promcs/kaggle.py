"""Raw Kaggle archives and offline links to Liquipedia map rosters.

Source: ektarr/counter-strike-pro-matches on Kaggle, CC BY-SA 4.0.
"""

import csv
import hashlib
import io
import os
import re
import tempfile
import urllib.request
import zipfile
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from datetime import UTC, datetime, timedelta
from difflib import SequenceMatcher
from math import isfinite
from pathlib import Path

import typer

from promcs.link import normalize
from promcs.liquipedia.http import USER_AGENT
from promcs.liquipedia.parse import fold

URL = (
    "https://www.kaggle.com/api/v1/datasets/download/ektarr/counter-strike-pro-matches"
)
app = typer.Typer(no_args_is_help=True)


def stable_id(text):
    """Stable SQLite identity: first twelve SHA-1 hex digits."""
    return int(hashlib.sha1(text.encode()).hexdigest()[:12], 16)


def data_root():
    return Path(
        os.environ.get("PROMCS_DATA", Path(__file__).resolve().parents[1] / "data")
    )


def _get(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()


def fetch(root, get=None, today=None) -> Path:
    """Save today's unchanged archive once, using UTC dates."""
    date = today if today is not None else datetime.now(UTC).date()
    if isinstance(date, datetime):
        date = date.astimezone(UTC).date()
    path = Path(root) / "kaggle/counter-strike-pro-matches" / f"{date.isoformat()}.zip"
    if path.exists():
        return path
    raw = (get or _get)(URL)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(raw)
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)
    return path


def latest_zip(root) -> Path | None:
    """Find the lexicographically newest cached archive."""
    return max(
        (Path(root) / "kaggle/counter-strike-pro-matches").glob("*.zip"), default=None
    )


@app.command("fetch")
def fetch_command():
    """Cache today's raw Kaggle dataset archive."""
    path = fetch(data_root())
    typer.echo(f"kaggle: {path} bytes={path.stat().st_size}")


def map_key(name):
    key = fold(name or "")
    return {"dustii": "dust2", "dust2": "dust2"}.get(key, key)


def display_name(value):
    """Nickname without the real name or a trailing ", RU" country code."""
    return re.sub(r",\s*[A-Z]{2}$", "", (value or "").split(" (", 1)[0].strip())


def nickname(value):
    return fold(display_name(value))


def similar(a, b):
    """Spelling variants such as dev1ce/device or jottAAA/jottA."""
    short = min(a, b, key=len)
    if len(short) >= 3 and (a in b or b in a):
        return True
    return SequenceMatcher(None, a, b).ratio() >= 0.6


def leftover(roster, names):
    """The one roster player and Kaggle slot left after exact name matches."""
    pids = {pid for found in roster.values() for pid in found}
    hit = {next(iter(roster[n])) for n in names if len(roster.get(n, ())) == 1}
    missing = [i for i, n in enumerate(names) if len(roster.get(n, ())) != 1]
    rest = pids - hit
    if len(missing) != 1 or len(rest) != 1:
        return None
    pid = next(iter(rest))
    known = [n for n, found in roster.items() if pid in found]
    if any(similar(names[missing[0]], n) for n in known):
        return missing[0], pid
    return None


def same_team(name, candidates):
    """Match normalized tokens, initials, or folded containment against any alias."""
    tokens = normalize(name or "")
    folded = fold(name or "")
    initials = "".join(t[0] for t in tokens)
    for other in candidates:
        other_tokens, other_folded = normalize(other), fold(other)
        if tokens and tokens == other_tokens:
            return True
        if len(other_folded) >= 2 and other_folded == initials:
            return True
        short = min(folded, other_folded, key=len)
        if len(short) >= 3 and (folded in other_folded or other_folded in folded):
            return True
    return False


def number(value):
    try:
        result = float(value)
    except (ValueError, TypeError):
        return None
    return result if isfinite(result) else None


def player_key(value):
    """Normalize CSV numeric player IDs (including pandas' .0 spelling)."""
    value = number(value)
    return str(int(value)) if value is not None and value.is_integer() else None


def load_stats(conn, path):
    """Link a saved archive and replace the derived stats without fetching."""
    index = defaultdict(list)
    games = {}
    names = defaultdict(set)
    for team_id, *aliases in conn.execute(
        "SELECT team_id, name, key FROM teams UNION ALL "
        "SELECT liquipedia_team_id, kalshi_name, kalshi_code FROM team_aliases"
    ):
        names[team_id].update(a for a in aliases if a)
    for gid, start, name, s1, s2, id1, id2 in conn.execute(
        "SELECT g.game_id, m.start_utc, g.map, g.score1, g.score2, m.team1_id, m.team2_id "
        "FROM maps g JOIN matches m USING(match_id)"
    ):
        timestamp = datetime.fromisoformat(start.replace("Z", "+00:00")).timestamp()
        games[gid] = (s1, s2, (names[id1], names[id2]))
        index[(map_key(name), min(s1, s2), max(s1, s2))].append((timestamp, gid))
    for entries in index.values():
        entries.sort()
    rosters = defaultdict(lambda: ({}, {}))
    for gid, pid, side, name, key in conn.execute(
        "SELECT game_id, player_id, team, name, key FROM player_maps JOIN players USING(player_id)"
    ):
        for alias in (name, key):
            normalized = fold(alias or "")
            if normalized:
                rosters[gid][side - 1].setdefault(normalized, set()).add(pid)

    claims = defaultdict(list)
    totals = Counter()
    with zipfile.ZipFile(path) as archive:
        with archive.open("cs2_all_tiers_games.csv") as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig")):
                if row["is_total"] != "False":
                    continue
                utc = datetime.fromisoformat(row["datetime"]).replace(
                    tzinfo=UTC
                ) - timedelta(hours=3)
                totals[utc.year] += 1
                scores = (number(row["score1_game"]), number(row["score2_game"]))
                if None in scores:
                    continue
                entries = index.get(
                    (map_key(row["map_name"]), min(scores), max(scores)), []
                )
                timestamp = utc.timestamp()
                candidates = {}
                names = tuple(
                    [nickname(row.get(f"team{side}_player{i}")) for i in range(1, 6)]
                    for side in (1, 2)
                )
                teams = (row["team1"], row["team2"])
                for _, gid in entries[
                    bisect_left(
                        entries, (timestamp - 43200, float("-inf"))
                    ) : bisect_right(entries, (timestamp + 43200, float("inf")))
                ]:
                    s1, s2, lp_teams = games[gid]
                    for swapped in (0, 1):
                        if scores != ((s2, s1) if swapped else (s1, s2)):
                            continue
                        overlaps = [
                            sum(
                                name in rosters[gid][side ^ swapped]
                                for name in names[side]
                            )
                            for side in (0, 1)
                        ]
                        named = [
                            same_team(teams[side], lp_teams[side ^ swapped])
                            for side in (0, 1)
                        ]
                        # A side agrees on 3+ players or on its name (Kalshi aliases
                        # cover cardless template teams with no roster).
                        agree = [overlaps[side] >= 3 or named[side] for side in (0, 1)]
                        if not all(agree):
                            continue
                        overlap = sum(overlaps)
                        rank = (overlap, sum(named))
                        if gid not in candidates or rank > candidates[gid][0]:
                            candidates[gid] = (rank, swapped)
                ranked = sorted(
                    candidates.items(), key=lambda item: item[1][0], reverse=True
                )
                if not ranked:
                    continue
                gid, ((overlap, _), swapped) = ranked[0]
                if len(ranked) > 1 and ranked[1][1][0] == ranked[0][1][0]:
                    continue
                claims[gid].append((overlap, swapped, row, utc.year))

    # Decide all links before learning player identities or changing any roster.
    links = {}
    for gid, options in claims.items():
        options.sort(key=lambda item: item[0], reverse=True)
        if len(options) > 1 and options[0][0] == options[1][0]:
            continue
        links[gid] = options[0]
    votes = defaultdict(Counter)
    for gid, (_, swapped, row, _) in links.items():
        for side in (1, 2):
            roster = rosters[gid][(side - 1) ^ swapped]
            names = [nickname(row.get(f"team{side}_player{i}")) for i in range(1, 6)]
            for i in range(1, 6):
                prefix = f"team{side}_player{i}"
                kid = player_key(row.get(prefix + "_id"))
                matches = roster.get(names[i - 1], set())
                if kid is not None and len(matches) == 1:
                    votes[kid][next(iter(matches))] += 1
            # A lone unmatched slot with a similarly spelled lone roster player.
            spare = leftover(roster, names)
            kid = spare and player_key(row.get(f"team{side}_player{spare[0] + 1}_id"))
            if kid is not None:
                votes[kid][spare[1]] += 1
    learned = {}
    for kid, counts in votes.items():
        pid, count = counts.most_common(1)[0]
        if count / counts.total() >= 0.8:
            learned[kid] = pid

    conn.execute("DELETE FROM player_stats")
    conn.execute("DELETE FROM kaggle_links")
    linked = Counter()
    stats_count = covered = replaced = changed = created = 0
    for gid, (overlap, swapped, row, year) in links.items():
        conn.execute(
            "INSERT INTO kaggle_links VALUES (?, ?, ?, ?)",
            (int(row["game_id"]), gid, swapped, overlap),
        )
        linked[year] += 1
        original = [
            set().union(*roster.values()) if roster else set()
            for roster in rosters[gid]
        ]
        proposals, new_players = {}, {}
        for side in (1, 2):
            lp_side = (side - 1) ^ swapped
            lineup = []
            names = [nickname(row.get(f"team{side}_player{i}")) for i in range(1, 6)]
            spare = leftover(rosters[gid][lp_side], names)
            for i in range(1, 6):
                prefix = f"team{side}_player{i}"
                kid = player_key(row.get(prefix + "_id"))
                name = display_name(row.get(prefix))
                if kid is None or not nickname(name):
                    break
                matches = rosters[gid][lp_side].get(nickname(name), set())
                if len(matches) == 1:
                    pid = next(iter(matches))
                elif kid in learned:
                    pid = learned[kid]
                elif spare and spare[0] == i - 1:
                    pid = spare[1]
                else:
                    pid = stable_id("player:kaggle:" + kid)
                    new_players[pid] = (pid, "kaggle:" + kid, name)
                lineup.append(pid)
            if len(lineup) == 5 and len(set(lineup)) == 5:
                proposals[lp_side] = lineup
        # Reject conflicting proposals together, then recheck against any restored
        # original lineup. At most two sides can be removed from consideration.
        while proposals:
            final = [set(proposals.get(side, original[side])) for side in (0, 1)]
            conflict = final[0] & final[1]
            rejected = [side for side in proposals if set(proposals[side]) & conflict]
            if not rejected:
                break
            for side in rejected:
                del proposals[side]
        for side, lineup in proposals.items():
            replaced += 1
            changed += set(lineup) != original[side]
            for pid in lineup:
                if pid in new_players:
                    cursor = conn.execute(
                        "INSERT OR IGNORE INTO players VALUES (?, ?, ?)",
                        new_players[pid],
                    )
                    created += cursor.rowcount
        # Delete accepted sides first, allowing players to move between sides.
        for side in proposals:
            conn.execute(
                "DELETE FROM player_maps WHERE game_id=? AND team=?", (gid, side + 1)
            )
        for side, lineup in proposals.items():
            conn.executemany(
                "INSERT INTO player_maps VALUES (?, ?, ?)",
                [(gid, pid, side + 1) for pid in lineup],
            )
        inserted = {}
        for side in (1, 2):
            lp_side = (side - 1) ^ swapped
            for i in range(1, 6):
                prefix = f"team{side}_player{i}"
                if lp_side in proposals:
                    pid = proposals[lp_side][i - 1]
                else:
                    matches = rosters[gid][lp_side].get(
                        nickname(row.get(prefix)), set()
                    )
                    if len(matches) != 1:
                        continue
                    pid = next(iter(matches))
                inserted[pid] = (
                    gid,
                    pid,
                    lp_side + 1,
                    *(
                        number(row.get(f"{prefix}_{stat}"))
                        for stat in ("kills", "deaths", "assists", "adr", "kast")
                    ),
                )
        conn.executemany(
            "INSERT INTO player_stats VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            inserted.values(),
        )
        counts = Counter(record[2] for record in inserted.values())
        covered += counts[1] >= 4 and counts[2] >= 4
        stats_count += len(inserted)
    total, count = sum(totals.values()), sum(linked.values())
    yearly = ", ".join(
        f"{year}:{linked[year]}/{totals[year]} ({linked[year] / totals[year]:.1%})"
        for year in sorted(totals)
    )
    return f"kaggle: map_rows={total} linked={count} ({count / total if total else 0:.1%}); by_year=[{yearly}]; player_stats={stats_count}; >=4/side={covered}/{count} ({covered / count if count else 0:.1%}); sides_replaced={replaced}; lineups_changed={changed}; new_kaggle_players={created}; learned_mappings={len(learned)}"


def load_latest(conn, root):
    """Load the newest local archive, or report an optional missing dataset."""
    path = latest_zip(root)
    return "kaggle: no dataset, skipped" if path is None else load_stats(conn, path)
