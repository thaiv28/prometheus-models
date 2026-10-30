"""Offline-cache aware monthly and single-match fetching."""

import sqlite3
from collections import Counter
from datetime import UTC, datetime, timedelta

from promdota.opendota import cache
from promdota.opendota.http import BudgetExhausted, Fetcher


def stamp(now):
    return now.isoformat().replace("+00:00", "Z")


def month_start(value):
    return datetime.strptime(value, "%Y-%m").replace(tzinfo=UTC)


def next_month(value):
    return (
        value.replace(year=value.year + 1, month=1)
        if value.month == 12
        else value.replace(month=value.month + 1)
    )


def bulk(fetcher=None, start="2019-01", end=None, now=None):
    now = now or datetime.now(UTC)
    fetcher = fetcher or Fetcher()
    month, stop = month_start(start), month_start(end or now.strftime("%Y-%m"))
    counts = Counter()
    while month <= stop:
        following = next_month(month)
        lower, upper = int(month.timestamp()), int(following.timestamp())
        queries = {
            "matches": f"SELECT match_id, start_time, leagueid, series_id, series_type, radiant_team_id, dire_team_id, radiant_win, duration FROM matches WHERE start_time >= {lower} AND start_time < {upper} ORDER BY match_id",
            "players": f"SELECT pm.match_id, pm.account_id, pm.player_slot, pm.hero_id, pm.kills, pm.deaths, pm.assists, pm.gold_per_min, pm.xp_per_min FROM player_matches pm JOIN matches m USING(match_id) WHERE m.start_time >= {lower} AND m.start_time < {upper} ORDER BY pm.match_id, pm.player_slot",
        }
        for kind, sql in queries.items():
            path = (
                cache.data_dir()
                / "explorer"
                / kind
                / (month.strftime("%Y-%m") + ".json.gz")
            )
            old = cache.read(path)
            if old and datetime.fromisoformat(
                old["fetched_at"].replace("Z", "+00:00")
            ) > following + timedelta(days=45):
                counts["cached"] += 1
                continue
            try:
                payload = fetcher.query("/explorer", sql=sql)
            except BudgetExhausted:
                counts["limited"] += 1
                return counts
            except (RuntimeError, OSError):
                counts["errors"] += 1
                continue
            if payload.get("err") is not None or not isinstance(
                payload.get("rows"), list
            ):
                counts["errors"] += 1
                continue
            cache.save(path, {"rows": payload["rows"], "fetched_at": stamp(now)})
            counts["saved"] += 1
        month = following
    return counts


def games(db, fetcher=None, now=None):
    now = now or datetime.now(UTC)
    fetcher = fetcher or Fetcher()
    root = cache.data_dir()
    missing = cache.read(root / "missing.json", {})
    index = cache.read(root / "index.json", {})
    records = cache.load_records()
    with sqlite3.connect(db) as conn:
        rows = conn.execute(
            'SELECT g.dota_match_id FROM games g JOIN matches m USING(match_id) WHERE g.dota_match_id IS NOT NULL ORDER BY m.start_utc DESC, g."order" DESC'
        ).fetchall()
    counts = Counter()
    seen = set()
    for (match_id,) in rows:
        key = str(match_id)
        if match_id in seen or match_id in records:
            continue
        seen.add(match_id)
        if key in missing and now - datetime.fromisoformat(
            missing[key].replace("Z", "+00:00")
        ) < timedelta(days=7):
            continue
        try:
            payload = fetcher.query(f"/matches/{match_id}")
        except BudgetExhausted:
            counts["limited"] += 1
            break
        except (RuntimeError, OSError):
            counts["errors"] += 1
            continue
        counts["attempted"] += 1
        if (
            payload.get("match_id") == match_id
            and payload.get("radiant_win") is not None
            and len(payload.get("players", [])) == 10
        ):
            record = cache.project(payload)
            record["fetched_at"] = stamp(now)
            cache.save(cache.game_file(match_id), record)
            index[key] = stamp(now)
            missing.pop(key, None)
            counts["saved"] += 1
        else:
            missing[key] = stamp(now)
            counts["missing"] += 1
        if counts["attempted"] % 50 == 0:
            cache.save(root / "index.json", index)
            cache.save(root / "missing.json", missing)
    cache.save(root / "index.json", index)
    cache.save(root / "missing.json", missing)
    return counts
