#!/usr/bin/env python3
"""Cheap, fail-open feed probe. Deliberately stdlib-only for system Python 3.12."""

import argparse
import gzip
import json
import os
import time
from datetime import UTC, datetime, timedelta
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

LP_API = "https://liquipedia.net/dota2/api.php"
KALSHI_API = "https://api.elections.kalshi.com/trade-api/v2/events"


def instant(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)


def fetch(url, params):
    contact = os.environ.get("LIQUIPEDIA_CONTACT") or "thaivillaluna@gmail.com"
    request = Request(
        url + "?" + urlencode(params),
        headers={
            "User-Agent": f"dota2-model/0.1 (+https://github.com/thaiv28/dota2-model; {contact})",
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


def probe(
    previous, snapshot, *, get=fetch, now=None, sleep=time.sleep, clock=time.monotonic
):
    """Return (run, gate); retain export time until export actually succeeds."""
    now = now or datetime.now(UTC)
    gate = dict(previous)
    try:
        if snapshot.get("version") != 2 or not snapshot.get("pages"):
            return True, gate
        titles = sorted(snapshot["pages"])
        ids, last = {}, None
        for offset in range(0, len(titles), 50):
            if last is not None:
                sleep(max(0, last + 2.2 - clock()))
            last = clock()
            result = get(
                LP_API,
                {
                    "action": "query",
                    "format": "json",
                    "prop": "revisions",
                    "rvprop": "ids|timestamp",
                    "titles": "|".join(titles[offset : offset + 50]),
                },
            )
            query = result["query"]
            pages = query["pages"]
            pages = list(pages.values()) if isinstance(pages, dict) else pages
            by_title = {p["title"]: p for p in pages}
            normalized = {n["from"]: n["to"] for n in query.get("normalized", [])}
            for title in titles[offset : offset + 50]:
                page = by_title[normalized.get(title, title)]
                ids[title] = (
                    None if "missing" in page else page["revisions"][0]["revid"]
                )
        tickers, cursor = set(), ""
        while True:
            params = {"series_ticker": "KXDOTA2GAME", "status": "open"}
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
            or ids != previous.get("revids")
            or ids != {t: p["revid"] for t, p in snapshot["pages"].items()}
            or sorted(tickers) != previous.get("event_tickers")
            or any(
                exported < instant(start) <= now for start in snapshot.get("starts", [])
            )
        )
        gate.update(revids=ids, event_tickers=sorted(tickers))
        return run, gate
    except Exception as exc:
        print(f"Gate requests/state failed; exporting: {type(exc).__name__}")
        return True, gate


def read(path, compressed=False):
    try:
        with gzip.open(path, "rt") if compressed else path.open() as handle:
            value = json.load(handle)
            return value if isinstance(value, dict) else {}
    except (OSError, ValueError, EOFError):
        return {}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gate", type=Path, required=True)
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--mark-export", action="store_true")
    args = parser.parse_args()
    previous, snapshot = read(args.gate), read(args.snapshot, True)
    if args.mark_export:
        gate = previous | {
            "last_export_at": datetime.now(UTC).isoformat(),
            "revids": {t: p["revid"] for t, p in snapshot["pages"].items()},
        }
    else:
        run, gate = probe(previous, snapshot)
        with open(os.environ["GITHUB_OUTPUT"], "a") as output:
            output.write(f"run={str(run).lower()}\n")
    args.gate.parent.mkdir(parents=True, exist_ok=True)
    args.gate.write_text(json.dumps(gate, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
