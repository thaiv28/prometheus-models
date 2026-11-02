"""Atomic projected single-game and unchanged Explorer row caches."""

import gzip
import json
import os
from pathlib import Path

from promdota.liquipedia.cache import _atomic_write

FETCH_VERSION = 1
MATCH_FIELDS = (
    "match_id",
    "start_time",
    "duration",
    "radiant_win",
    "leagueid",
    "series_id",
    "series_type",
    "radiant_team_id",
    "dire_team_id",
)
PLAYER_FIELDS = (
    "account_id",
    "player_slot",
    "hero_id",
    "kills",
    "deaths",
    "assists",
    "gold_per_min",
    "xp_per_min",
)


def data_dir():
    return (
        Path(
            os.environ.get(
                "PROMDOTA_DATA", Path(__file__).resolve().parents[2] / "data"
            )
        )
        / "opendota"
    )


def read(path, default=None):
    if not path.exists():
        return default
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


def game_file(match_id):
    return (
        data_dir() / "matches" / f"{int(match_id) % 1000:03d}" / f"{match_id}.json.gz"
    )


def project(record):
    result = {key: record.get(key) for key in MATCH_FIELDS}
    result["players"] = [
        {key: p.get(key) for key in PLAYER_FIELDS} for p in record.get("players", [])
    ]
    result["fetch_version"] = FETCH_VERSION
    return result


def cached(folder, pattern):
    """Cache files, skipping dot-files such as macOS `._*` tar companions."""
    return sorted(p for p in folder.glob(pattern) if not p.name.startswith("."))


def load_records():
    """Return match id → data, merging bulk player rows and single projections."""
    records = {}
    for path in cached(data_dir() / "explorer/matches", "*.json.gz"):
        for row in read(path)["rows"]:
            records[int(row["match_id"])] = dict(row, players=[])
    for path in cached(data_dir() / "explorer/players", "*.json.gz"):
        for row in read(path)["rows"]:
            if int(row["match_id"]) in records:
                records[int(row["match_id"])]["players"].append(row)
    for path in cached(data_dir() / "matches", "*/*.json.gz"):
        record = read(path)
        records[int(record["match_id"])] = record
    return records


def save(path, record):
    _atomic_write(path, record)
