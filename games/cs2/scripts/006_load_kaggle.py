"""Load the latest raw Kaggle archive without network access."""

import sqlite3
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from promcs.kaggle import data_root, load_latest


def main():
    with sqlite3.connect(REPO / "db/cs2.db") as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        print(load_latest(conn, data_root()))


if __name__ == "__main__":
    main()
