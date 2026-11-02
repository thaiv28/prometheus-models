"""Atomic unchanged HTML cache and fetch metadata."""

import gzip
import json
import os
import tempfile
from pathlib import Path


def data_dir():
    return Path(os.environ.get("PROMR6_DATA", "data")) / "siegegg"


def match_file(match_id):
    return data_dir() / "matches" / f"{int(match_id)}.html.gz"


def read_match(match_id):
    path = match_file(match_id)
    return gzip.decompress(path.read_bytes()) if path.exists() else None


def read_index():
    path = data_dir() / "index.json"
    return json.loads(path.read_bytes()) if path.exists() else {}


def _atomic_write(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(body)
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def save_match(match_id, body):
    _atomic_write(match_file(match_id), gzip.compress(body, mtime=0))


def save_index(index):
    _atomic_write(data_dir() / "index.json", json.dumps(index, indent=2).encode())
