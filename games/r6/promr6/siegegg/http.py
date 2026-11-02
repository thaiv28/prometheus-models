"""Polite urllib transport; redirects and retries share the request clock."""

import os
import time
from http.client import HTTPException
from threading import Lock
from urllib.error import HTTPError
from urllib.request import HTTPRedirectHandler, Request, build_opener

BASE = "https://siege.gg"
USER_AGENT = "r6-model/0.1 (+https://github.com/thaiv28/prometheus-models)"


class _Redirect(HTTPRedirectHandler):
    def __init__(self, pace):
        self.pace = pace

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        request = super().redirect_request(req, fp, code, msg, headers, newurl)
        if request is not None:
            self.pace()
        return request


class Client:
    def __init__(self, open=None, sleep=time.sleep, clock=time.monotonic):
        self.sleep, self.clock = sleep, clock
        self._last = None
        self._lock = Lock()
        self.open = open or build_opener(_Redirect(self._pace)).open

    def _pace(self):
        if self._last is not None:
            self.sleep(max(0, self._last + 2.0 - self.clock()))
        self._last = self.clock()

    def get(self, url):
        with self._lock:
            return self._get(url)

    def _get(self, url):
        contact = os.environ.get("SIEGEGG_CONTACT", "").strip()
        agent = USER_AGENT + (f" {contact}" if contact else "")
        failures, rate_limited = 0, False
        while True:
            self._pace()
            try:
                request = Request(url, headers={"User-Agent": agent})
                try:
                    response = self.open(request, timeout=60)
                except HTTPError as exc:
                    response = exc
                with response:
                    status, final_url = response.code, response.geturl()
                    body = response.read()
                if status == 429:
                    if rate_limited:
                        raise RuntimeError("siege.gg HTTP 429 after retry")
                    rate_limited = True
                    self.sleep(60)
                    continue
                if 500 <= status < 600:
                    raise OSError(f"siege.gg HTTP {status}")
                if status not in (200, 404):
                    raise RuntimeError(f"siege.gg HTTP {status}")
                return status, final_url, body
            except (OSError, HTTPException):
                failures += 1
                if failures >= 3:
                    raise
                self.sleep(2 ** (failures - 1))


_client = Client()


def get(url):
    """Return status, final redirect URL and unchanged response body bytes."""
    return _client.get(url)
