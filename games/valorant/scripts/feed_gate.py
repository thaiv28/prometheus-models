#!/usr/bin/env python3
"""Cheap, fail-open feed probe. Deliberately stdlib-only for system Python 3."""

import argparse
import gzip
import json
import os
import zlib
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

UTC = timezone.utc  # noqa: UP017 -- runner/local system Python may be 3.9.
KALSHI_API = "https://api.elections.kalshi.com/trade-api/v2/events"


def instant(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)


def fetch(url, params):
    contact = os.environ.get("LIQUIPEDIA_CONTACT") or "thaivillaluna@gmail.com"
    request = Request(
        url + "?" + urlencode(params),
        headers={
            "User-Agent": f"valorant-model/0.1 (+https://github.com/thaiv28/prometheus-models; {contact})",
            "Accept-Encoding": "gzip",
        },
    )
    with urlopen(request, timeout=15) as response:
        raw = response.read()
        if response.headers.get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
        value = json.loads(raw)
    if "error" in value:
        raise ValueError(value["error"])
    return value


SERIES = ("KXVALORANTGAME",)  # The series priced by promval.feed.export.


def probe(previous, snapshot, *, state_etag="", get=fetch, now=None):
    """Return (run, gate), retaining the export clock until publication succeeds."""
    now = now or datetime.now(UTC)
    gate = dict(previous)
    try:
        matches = snapshot["matches"]
        tickers = set()
        for series in SERIES:
            cursor = ""
            while True:
                params = {"series_ticker": series, "status": "open"}
                if cursor:
                    params["cursor"] = cursor
                result = get(KALSHI_API, params)
                tickers.update(e["event_ticker"] for e in result["events"])
                cursor = result.get("cursor")
                if not cursor:
                    break
        exported = (
            instant(previous["last_export_at"])
            if previous.get("last_export_at")
            else None
        )
        run = (
            exported is None
            or now - exported >= timedelta(hours=2)
            or exported > now
            or state_etag != previous.get("state_etag")
            or sorted(tickers) != previous.get("event_tickers")
            or any(match["status"] == "live" for match in matches)
            or any(exported < instant(match["start"]) <= now for match in matches)
        )
        gate.update(event_tickers=sorted(tickers))
        return run, gate
    except Exception as exc:
        print(f"Gate requests/state failed; exporting: {type(exc).__name__}")
        return True, gate


def read(path, compressed=False):
    try:
        with gzip.open(path, "rt") if compressed else path.open() as handle:
            value = json.load(handle)
            return value if isinstance(value, dict) else {}
    except (OSError, ValueError, EOFError, zlib.error):
        return {}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gate", type=Path, required=True)
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--state-etag", default="")
    parser.add_argument("--mark-export", action="store_true")
    args = parser.parse_args()
    previous, snapshot = read(args.gate), read(args.snapshot, True)
    if args.mark_export:
        gate = previous | {
            "last_export_at": datetime.now(UTC).isoformat(),
            "state_etag": args.state_etag,
            "event_tickers": previous.get("event_tickers", []),
        }
    else:
        run, gate = probe(previous, snapshot, state_etag=args.state_etag)
        with open(os.environ["GITHUB_OUTPUT"], "a") as output:
            output.write(f"run={str(run).lower()}\n")
    args.gate.parent.mkdir(parents=True, exist_ok=True)
    args.gate.write_text(json.dumps(gate, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
