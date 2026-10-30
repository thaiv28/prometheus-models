"""Polite, injectable OpenDota HTTP client with a per-run request budget."""

import gzip
import json
import time
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = "https://api.opendota.com/api"
USER_AGENT = "dota2-model/0.1 (+https://github.com/thaiv28/dota2-model)"
DAILY_BUDGET = 1800


class BudgetExhausted(Exception):
    """No requests remain in this run."""


def http_get(url, params):
    request = Request(
        url + ("?" + urlencode(params) if params else ""),
        headers={"User-Agent": USER_AGENT, "Accept-Encoding": "gzip"},
    )
    try:
        with urlopen(request, timeout=60) as response:
            raw = response.read()
            if response.headers.get("Content-Encoding") == "gzip":
                raw = gzip.decompress(raw)
            return response.status, json.loads(raw)
    except HTTPError as exc:
        if exc.code == 404:
            return exc.code, {"error": "Not Found"}
        return exc.code, {}


class Fetcher:
    def __init__(
        self, get=http_get, sleep=time.sleep, clock=time.monotonic, limit=DAILY_BUDGET
    ):
        self.get, self.sleep, self.clock = get, sleep, clock
        self.limit = min(max(0, limit), DAILY_BUDGET)
        self.requests = 0
        self._last = None

    def query(self, path, **params):
        for attempt in range(4):
            if self.requests >= self.limit:
                raise BudgetExhausted
            if self._last is not None:
                self.sleep(max(0, self._last + 1.1 - self.clock()))
            self._last = self.clock()
            self.requests += 1
            status, payload = self.get(BASE + path, params)
            if status == 429 or 500 <= status < 600:
                if attempt < 3:
                    self.sleep(2**attempt)
                    continue
            if status == 404 and path.startswith("/matches/"):
                return {"error": "Not Found"}
            if status != 200:
                raise RuntimeError(f"OpenDota HTTP {status}")
            return payload
        raise AssertionError("unreachable")
