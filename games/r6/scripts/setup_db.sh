#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PROMR6_DB="${PROMR6_DB:-$PWD/db/r6.db}"
mkdir -p "$(dirname "$PROMR6_DB")"
rm -f "$PROMR6_DB"
uv run --no-sync python - <<'PY'
import os
import sqlite3
from pathlib import Path
with sqlite3.connect(os.environ['PROMR6_DB']) as conn:
    conn.executescript(Path('scripts/001_create_tables.sql').read_text())
PY
for script in scripts/002_load_liquipedia.py scripts/003_load_kalshi.py scripts/004_load_lineups.py scripts/005_link_kalshi.py; do
    uv run --no-sync python "$script"
done
