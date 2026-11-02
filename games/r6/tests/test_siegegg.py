"""Offline fixture parsing and injected HTTP clients with temporary raw caches."""

import gzip
import io
import json
from dataclasses import asdict
from email.message import Message
from http.client import RemoteDisconnected
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import HTTPSHandler, build_opener
from urllib.response import addinfourl

import pytest
from bs4 import BeautifulSoup
from typer.testing import CliRunner

from promr6.main import app
from promr6.siegegg import cache, fetch, http
from promr6.siegegg.parse import PARSER_VERSION, parse_match

FIXTURES = Path(__file__).parent / "fixtures/siegegg"


@pytest.fixture(autouse=True)
def isolated_cache(tmp_path, monkeypatch):
    monkeypatch.setenv("PROMR6_DATA", str(tmp_path / "raw"))

    def no_network(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(http._client, "open", no_network)


def fixture(match_id=6168):
    return gzip.decompress((FIXTURES / f"match_{match_id}.html.gz").read_bytes())


def test_recent_rosters_scores_and_ids():
    match = parse_match(fixture())
    assert PARSER_VERSION == 1
    assert match.team1.name == "DarkZero Esports"
    assert match.team2.name == "Wildcard"
    assert match.team1.siegegg_team_id == 465
    assert match.team2.siegegg_team_id == 725
    assert (match.team1.score, match.team2.score) == (3, 7)
    assert [(p.nickname, p.siegegg_player_id) for p in match.team1.players] == [
        ("Fultz", 1077),
        ("Nuers", 2935),
        ("njr", 1809),
        ("Kyno", 1871),
        ("Koshi", 3925),
    ]
    assert [(p.nickname, p.siegegg_player_id) for p in match.team2.players] == [
        ("Kanzen", 1805),
        ("Spiker", 3223),
        ("Bae", 3411),
        ("bbySharKK", 3667),
        ("Adrian", 3501),
    ]
    assert match.maps == (("Villa", 3, 7),)
    assert match.finished
    assert match.start_utc == "2026-09-09T18:00:00Z"
    assert match.competition == "North America League 2026 Stage 2"


@pytest.mark.parametrize(
    "match_id,names,rosters,maps",
    [
        (
            3000,
            ("ex-Chiefs Esports Club", "Four Angry Men"),
            (
                ("Jigsaw", "NAATE", "Brendo", "Wettables", "Kyro"),
                ("Gotti", "Darcly", "rockstarKa", "Lyda", "txonly"),
            ),
            (("Bank", 7, 2), ("Lair", 7, 4)),
        ),
        (
            4000,
            ("Invictus Gaming", "Ninjas In Pyjamas"),
            (
                ("LUNARMETAL", "SpeakEasy", "JRDN", "GIG", "HISTOIRE"),
                ("Psycho", "Muzi", "pino", "KAMIKAZE", "JULIO"),
            ),
            (("Bank", 3, 7),),
        ),
    ],
)
def test_older_pages(match_id, names, rosters, maps):
    match = parse_match(fixture(match_id).decode())
    assert (match.team1.name, match.team2.name) == names
    assert tuple(p.nickname for p in match.team1.players) == rosters[0]
    assert tuple(p.nickname for p in match.team2.players) == rosters[1]
    assert all(
        p.siegegg_player_id > 0 for t in (match.team1, match.team2) for p in t.players
    )
    assert match.maps == maps
    assert match.finished


def test_5800_has_only_two_recorded_maps():
    # The supplied HTML says 2–1 overall but contains only two game results.
    match = parse_match(fixture(5800))
    assert (match.team1.score, match.team2.score) == (2, 1)
    assert match.maps == (("Border", 3, 5), ("Oregon", 5, 2))
    assert len(match.team1.players) == len(match.team2.players) == 5


def test_404():
    assert parse_match(fixture(99999)) is None


def test_dedupe_optional_fields_and_finality():
    soup = BeautifulSoup(fixture(), "lxml")
    player = soup.select_one(".match__roster.team--a .roster__player")
    player.insert_after(
        BeautifulSoup(str(player), "lxml").select_one(".roster__player")
    )
    for node in soup.select('time[datetime], a[href*="/competitions/"]'):
        node.decompose()
    match = parse_match(str(soup))
    assert len(match.team1.players) == 5
    assert match.start_utc is None and match.competition is None
    soup.select_one(".match__score").string = "–"
    assert not parse_match(str(soup)).finished
    soup.select_one(".match__score").string = "0"
    assert parse_match(str(soup)).finished
    soup.select_one("#games").decompose()
    assert not parse_match(str(soup)).finished


def test_json_ld_utc_fallback():
    soup = BeautifulSoup(fixture(), "lxml")
    for node in soup.select("time[datetime]"):
        node.decompose()
    script = soup.new_tag("script", type="application/ld+json")
    script.string = json.dumps({"@graph": [{"startDate": "2026-09-09T20:00:00+02:00"}]})
    soup.append(script)
    assert parse_match(str(soup)).start_utc == "2026-09-09T18:00:00Z"
    script.string = "{invalid"
    assert parse_match(str(soup)).start_utc is None


def test_fetch_cache_finished_and_final_url():
    seen = []
    final = http.BASE + "/matches/6168-nal-2026"

    def get(url):
        seen.append(url)
        return 200, final, fixture()

    assert asdict(fetch.fetch_matches([6168, 6168], get=get)) == {
        "requested": 1,
        "cached": 0,
        "fetched": 1,
        "not_found": 0,
        "errors": 0,
    }
    assert cache.read_match(6168) == fixture()
    row = cache.read_index()["6168"]
    assert row["url"] == final and row["status"] == 200 and row["finished"]
    assert row["fetched_at"].endswith("Z")
    assert fetch.fetch_matches([6168], get=get).cached == 1
    assert fetch.fetch_matches([6168], get=get, refresh=True).cached == 1
    assert len(seen) == 1


def test_unfinished_and_404_require_refresh():
    body = fixture().replace(b">Game results<", b">Scheduled<")
    assert not parse_match(body).finished
    get = lambda url: (200, url, body)
    assert fetch.fetch_matches([6168], get=get).fetched == 1
    assert fetch.fetch_matches([6168], get=get).cached == 1
    assert fetch.fetch_matches([6168], get=get, refresh=True).fetched == 1
    missing = lambda url: (404, url, fixture(99999))
    assert fetch.fetch_matches([99999], get=missing).not_found == 1
    assert cache.read_match(99999) == fixture(99999)
    assert cache.read_index()["99999"]["status"] == 404
    assert fetch.fetch_matches([99999], get=missing).cached == 1
    assert fetch.fetch_matches([99999], get=missing, refresh=True).not_found == 1


def test_limit_errors_and_raw_before_parse():
    def failed(url):
        raise OSError("offline")

    assert fetch.fetch_matches([1, 2], get=failed, limit=1).errors == 1
    assert fetch.fetch_matches([1], get=failed, limit=0).requested == 0
    assert fetch.fetch_matches([2], get=lambda url: (503, url, b"bad")).errors == 1
    assert fetch.fetch_matches([3], get=lambda url: (200, url, b"bad")).errors == 1
    assert cache.read_match(3) == b"bad"
    assert not cache.read_index()["3"]["finished"]
    with pytest.raises(ValueError):
        fetch.fetch_matches([0], get=failed)


class Response(io.BytesIO):
    code = 200

    def geturl(self):
        return http.BASE + "/matches/6168-slug"


def test_http_ua_spacing_and_final_url(monkeypatch):
    seen, sleeps = [], []
    monkeypatch.setenv("SIEGEGG_CONTACT", "mailto:example@example.com")

    def open(request, timeout):
        seen.append((request.get_header("User-agent"), timeout))
        return Response(b"unchanged")

    client = http.Client(open=open, sleep=sleeps.append, clock=lambda: 0)
    assert client.get(http.BASE) == (
        200,
        http.BASE + "/matches/6168-slug",
        b"unchanged",
    )
    client.get(http.BASE)
    assert sleeps == [2.0]
    assert seen == [(http.USER_AGENT + " mailto:example@example.com", 60)] * 2


def test_301_redirect_is_paced():
    sleeps, urls = [], []
    client = http.Client(sleep=sleeps.append, clock=lambda: 0)

    class FakeHTTPS(HTTPSHandler):
        def https_open(self, request):
            urls.append(request.full_url)
            first = len(urls) == 1
            headers = Message()
            if first:
                headers["Location"] = http.BASE + "/matches/6168-slug"
            response = addinfourl(
                io.BytesIO(b"redirect" if first else b"raw"),
                headers,
                request.full_url,
                301 if first else 200,
            )
            response.msg = "Moved" if first else "OK"
            return response

    client.open = build_opener(FakeHTTPS(), http._Redirect(client._pace)).open
    assert client.get(http.BASE + "/matches/6168") == (
        200,
        http.BASE + "/matches/6168-slug",
        b"raw",
    )
    assert urls == [http.BASE + "/matches/6168", http.BASE + "/matches/6168-slug"]
    assert sleeps == [2.0]


@pytest.mark.parametrize("status", [404, 429, 503])
def test_http_error_statuses(status):
    sleeps, attempts = [], []

    def open(request, timeout):
        attempts.append(request.full_url)
        raise HTTPError(request.full_url, status, "test", {}, io.BytesIO(b"raw"))

    client = http.Client(open=open, sleep=sleeps.append, clock=lambda: 0)
    if status == 404:
        assert client.get(http.BASE) == (404, http.BASE, b"raw")
        assert len(attempts) == 1
    else:
        with pytest.raises((RuntimeError, OSError), match=str(status)):
            client.get(http.BASE)
        assert len(attempts) == (2 if status == 429 else 3)
        if status == 429:
            assert sleeps.count(60) == 1
        else:
            assert sleeps == [1, 2.0, 2, 2.0]


def test_429_retry_recovers():
    sleeps = []
    attempts = iter([429, 200])

    def open(request, timeout):
        if next(attempts) == 429:
            raise HTTPError(request.full_url, 429, "test", {}, io.BytesIO())
        return Response(b"ok")

    client = http.Client(open=open, sleep=sleeps.append, clock=lambda: 0)
    assert client.get(http.BASE)[2] == b"ok"
    assert sleeps == [60, 2.0]


@pytest.mark.parametrize("error", [TimeoutError, RemoteDisconnected, URLError])
def test_connection_errors_retry_three_times(error):
    calls = []

    def open(request, timeout):
        calls.append(request)
        raise error("dropped")

    client = http.Client(open=open, sleep=lambda n: None, clock=lambda: 0)
    with pytest.raises(error):
        client.get(http.BASE)
    assert len(calls) == 3


def test_cli_cached_show_status_and_from_file(tmp_path, monkeypatch):
    runner = CliRunner()
    assert runner.invoke(app, ["siegegg", "--help"]).exit_code == 0
    assert runner.invoke(app, ["siegegg", "fetch", "--help"]).exit_code == 0
    assert (
        fetch.fetch_matches([6168], get=lambda url: (200, url, fixture())).fetched == 1
    )
    shown = runner.invoke(app, ["siegegg", "show", "6168"])
    assert shown.exit_code == 0 and "Fultz" in shown.stdout
    assert runner.invoke(app, ["siegegg", "show", "1"]).exit_code == 1
    status = runner.invoke(app, ["siegegg", "status"])
    assert status.exit_code == 0 and "finished=1" in status.stdout
    file = tmp_path / "ids.txt"
    file.write_text("6168\n\n4000\n")
    received = []

    def fake(ids, **kwargs):
        received.append((ids, kwargs))
        return fetch.Summary(requested=len(ids))

    monkeypatch.setattr("promr6.siegegg.cli.fetch_matches", fake)
    result = runner.invoke(
        app,
        [
            "siegegg",
            "fetch",
            "3000",
            "--from-file",
            str(file),
            "--refresh",
            "--limit",
            "2",
        ],
    )
    assert result.exit_code == 0, result.output
    assert received == [([3000, 6168, 4000], {"refresh": True, "limit": 2})]
    assert (
        runner.invoke(app, ["siegegg", "fetch", "--from-file", str(file)]).exit_code
        == 0
    )
    assert runner.invoke(app, ["siegegg", "fetch", "-1"]).exit_code != 0


def test_cli_from_db(tmp_path, monkeypatch):
    import sqlite3

    monkeypatch.chdir(tmp_path)
    database = tmp_path / "db/r6.db"
    database.parent.mkdir()
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE matches(siegegg_id INTEGER, start_utc TEXT)")
        conn.executemany(
            "INSERT INTO matches VALUES (?, ?)",
            [(6168, "2026"), (4000, "2025"), (6168, "2024"), (None, "2027")],
        )
    received = []

    def fake(ids, **kwargs):
        received.append(ids)
        return fetch.Summary(requested=len(ids))

    monkeypatch.setattr("promr6.siegegg.cli.fetch_matches", fake)
    runner = CliRunner()
    for args, expected in [
        (["--from-db"], [6168, 4000]),
        (["3000", "--from-db"], [3000, 6168, 4000]),
    ]:
        result = runner.invoke(app, ["siegegg", "fetch", *args])
        assert result.exit_code == 0, result.output
        assert received[-1] == expected
