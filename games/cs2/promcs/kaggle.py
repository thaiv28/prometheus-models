"""Raw Kaggle archives and offline links to Liquipedia map rosters.

Source: ektarr/counter-strike-pro-matches on Kaggle, CC BY-SA 4.0.
"""

import csv
import io
import os
import tempfile
import urllib.request
import zipfile
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from datetime import UTC, datetime, timedelta
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


def nickname(value):
    return fold((value or "").split(" (", 1)[0])


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

    conn.execute("DELETE FROM player_stats")
    conn.execute("DELETE FROM kaggle_links")
    linked = Counter()
    stats_count = covered = 0
    for gid, options in claims.items():
        options.sort(key=lambda item: item[0], reverse=True)
        if len(options) > 1 and options[0][0] == options[1][0]:
            continue
        overlap, swapped, row, year = options[0]
        conn.execute(
            "INSERT INTO kaggle_links VALUES (?, ?, ?, ?)",
            (int(row["game_id"]), gid, swapped, overlap),
        )
        linked[year] += 1
        inserted = {}
        for side in (1, 2):
            lp_side = (side - 1) ^ swapped
            for i in range(1, 6):
                prefix = f"team{side}_player{i}"
                matches = rosters[gid][lp_side].get(nickname(row.get(prefix)), set())
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
    return f"kaggle: map_rows={total} linked={count} ({count / total if total else 0:.1%}); by_year=[{yearly}]; player_stats={stats_count}; >=4/side={covered}/{count} ({covered / count if count else 0:.1%})"


def load_latest(conn, root):
    """Load the newest local archive, or report an optional missing dataset."""
    path = latest_zip(root)
    return "kaggle: no dataset, skipped" if path is None else load_stats(conn, path)
