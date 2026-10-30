"""Offline Liquipedia collection with an injectable API and clock."""

import gzip
import itertools
import json
from datetime import UTC, datetime
from http.client import RemoteDisconnected
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlsplit

import pytest
from typer.testing import CliRunner

from promdota.liquipedia import cache, cli, http
from promdota.liquipedia.crawl import (
    CATEGORY,
    contents,
    crawl,
    list_category,
    revisions,
    subpage_links,
)
from promdota.main import app

NOW = datetime(2026, 10, 29, tzinfo=UTC)


class FakeClock:
    def __init__(self):
        self.time = 0.0
        self.sleeps = []

    def __call__(self):
        return self.time

    def sleep(self, seconds):
        self.sleeps.append(seconds)
        self.time += seconds


class FakeGet:
    def __init__(self, pages=None, category=None):
        self.pages = pages if pages is not None else {"Root": (1, ""), "Other": (2, "")}
        self.category = list(self.pages) if category is None else category
        self.calls = []
        self.normalized = {}
        self.listed = []  # main-namespace titles returned by list=allpages

    def __call__(self, params):
        self.calls.append(params)
        assert params["action"] == "query"
        assert "redirects" not in params
        if params.get("list") == "categorymembers":
            assert params["cmnamespace"] == 0
            assert params["cmlimit"] == 500
            assert params["cmprop"] == "title"
            if not params.get("cmcontinue") and len(self.category) > 1:
                return {
                    "query": {"categorymembers": [{"title": self.category[0]}]},
                    "continue": {"cmcontinue": "next", "continue": "-||"},
                }
            members = self.category[1:] if params.get("cmcontinue") else self.category
            return {
                "query": {"categorymembers": [{"title": title} for title in members]}
            }
        if params.get("list") == "allpages":
            assert params["apnamespace"] == 0
            assert params["apfilterredir"] == "nonredirects"
            return {
                "query": {
                    "allpages": [
                        {"title": t} for t in self.listed if not t.startswith("Match:")
                    ]
                }
            }
        if params.get("generator") == "allpages":
            assert params["gapnamespace"] == 130
            assert params["gaplimit"] == 500
            assert params["prop"] == "info"
            titles = [t for t in self.pages if t.startswith("Match:")]
            selected = titles[1:] if params.get("gapcontinue") else titles[:1]
            out = {
                "query": {
                    "pages": {
                        str(i): {
                            "pageid": i + 50,
                            "title": t,
                            "lastrevid": self.pages[t][0],
                        }
                        for i, t in enumerate(selected)
                    }
                }
            }
            if len(titles) > 1 and not params.get("gapcontinue"):
                out["continue"] = {
                    "gapcontinue": titles[1],
                    "continue": "gapcontinue||",
                }
            return out
        result = {}
        for i, title in enumerate(params["titles"].split("|")):
            title = self.normalized.get(title, title)
            if title not in self.pages:
                result[str(i)] = {"title": title, "missing": ""}
                continue
            revid, wikitext = self.pages[title]
            revision = {"revid": revid, "timestamp": "2026-10-28T00:00:00Z"}
            if "content" in params["rvprop"]:
                assert params["rvslots"] == "main"
                revision["slots"] = {"main": {"*": wikitext}}
            result[str(i)] = {"title": title, "pageid": i + 1, "revisions": [revision]}
        return {
            "query": {
                "pages": result,
                "normalized": [
                    {"from": key, "to": value} for key, value in self.normalized.items()
                ],
            }
        }

    def content_titles(self):
        return [
            title
            for call in self.calls
            if "content" in call.get("rvprop", "")
            for title in call["titles"].split("|")
        ]


def fetcher(get):
    clock = FakeClock()
    return http.Fetcher(get=get, sleep=clock.sleep, clock=clock)


@pytest.fixture(autouse=True)
def isolated_cache(monkeypatch, tmp_path):
    monkeypatch.setenv("PROMDOTA_DATA", str(tmp_path))


def test_user_agent(monkeypatch):
    monkeypatch.delenv("LIQUIPEDIA_CONTACT", raising=False)
    assert http.user_agent() == http.USER_AGENT[:-1] + "; " + http.CONTACT + ")"
    monkeypatch.setenv("LIQUIPEDIA_CONTACT", "research@example.com")
    assert http.user_agent() == http.USER_AGENT[:-1] + "; research@example.com)"


@pytest.mark.parametrize("compressed", [False, True])
def test_http_get(monkeypatch, compressed):
    class Response:
        headers = {"Content-Encoding": "gzip"} if compressed else {}

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def read(self):
            raw = b'{"query": {}}'
            return gzip.compress(raw) if compressed else raw

    def urlopen(request, timeout):
        assert timeout == 60
        assert request.get_header("Accept-encoding") == "gzip"
        assert request.get_header("User-agent") == http.user_agent()
        assert request.full_url.startswith(http.API + "?")
        assert parse_qs(urlsplit(request.full_url).query) == {
            "action": ["query"],
            "format": ["json"],
            "titles": ["A B/é"],
        }
        return Response()

    monkeypatch.setattr(http, "urlopen", urlopen)
    assert http.http_get({"action": "query", "titles": "A B/é", "format": "xml"}) == {
        "query": {}
    }


def test_query_only_and_spacing():
    clock = FakeClock()
    calls = []
    client = http.Fetcher(
        get=lambda params: calls.append(clock()) or {},
        clock=clock,
        sleep=clock.sleep,
        min_interval=2.2,
    )
    for action in [None, "parse", "edit"]:
        with pytest.raises(ValueError):
            client.query(action=action)
    assert calls == []
    for _ in range(4):
        client.query(action="query")
    assert all(b - a >= 2.2 - 1e-9 for a, b in itertools.pairwise(calls))


@pytest.mark.parametrize(
    "error",
    [
        HTTPError("url", 429, "limit", {}, None),
        HTTPError("url", 503, "server", {}, None),
        URLError("offline"),
        TimeoutError(),
        RemoteDisconnected("closed"),
        ConnectionResetError(),
    ],
)
def test_retry(error):
    clock = FakeClock()
    calls = []

    def get(params):
        calls.append(clock())
        if len(calls) == 1:
            raise error
        return {}

    client = http.Fetcher(get=get, clock=clock, sleep=clock.sleep)
    assert client.query(action="query") == {}
    assert calls == [0, 5]


def test_retry_exhausted():
    clock = FakeClock()
    calls = []

    def get(params):
        calls.append(clock())
        raise TimeoutError()

    with pytest.raises(TimeoutError):
        http.Fetcher(get=get, clock=clock, sleep=clock.sleep).query(action="query")
    assert calls == [0, 5, 15, 35, 75]


@pytest.mark.parametrize(
    "error",
    [HTTPError("url", 404, "missing", {}, None), {"error": {"code": "badvalue"}}],
)
def test_no_retry(error):
    calls = []

    def get(params):
        calls.append(params)
        if isinstance(error, Exception):
            raise error
        return error

    with pytest.raises(HTTPError if isinstance(error, Exception) else RuntimeError):
        fetcher(get).query(action="query")
    assert len(calls) == 1


def test_category_and_normalized_titles():
    get = FakeGet({"A B": (7, "text"), "Other": (9, "")}, ["A_B", "Other", "Missing"])
    get.normalized = {"A_B": "A B"}
    client = fetcher(get)
    assert list_category(client, CATEGORY) == ["A_B", "Other", "Missing"]
    assert revisions(client, ["A_B", "Missing"]) == {
        "A_B": (1, 7, "2026-10-28T00:00:00Z")
    }
    assert contents(client, ["A_B"])[0]["title"] == "A_B"
    assert contents(client, ["A_B"])[0]["wikitext"] == "text"


def test_content_key():
    def get(params):
        return {
            "query": {
                "pages": {
                    "1": {
                        "title": "Root",
                        "pageid": 1,
                        "revisions": [
                            {
                                "revid": 1,
                                "timestamp": "now",
                                "slots": {"main": {"content": "raw"}},
                            }
                        ],
                    }
                }
            }
        }

    assert contents(fetcher(get), ["Root"])[0]["wikitext"] == "raw"


def test_incremental_and_full():
    get = FakeGet()
    client = fetcher(get)
    first = crawl(client, now=lambda: NOW)
    assert (first.listed, first.new, first.fetched, first.missing) == (2, 2, 2, 0)
    assert get.content_titles() == ["Root", "Other"]
    get.calls.clear()
    second = crawl(client)
    assert (second.fetched, second.unchanged) == (0, 2)
    assert get.content_titles() == []
    get.pages["Root"] = (3, "updated")
    third = crawl(client)
    assert (third.changed, third.new, third.fetched) == (1, 0, 1)
    assert get.content_titles() == ["Root"]
    assert cache.read_page("Root")["wikitext"] == "updated"
    assert crawl(client, full=True).fetched == 2


def test_subpage_discovery_and_cached_discovery():
    get = FakeGet(
        {
            "Root": (1, "{{Tabs|link2=Root/Playoffs}}"),
            "Root/Playoffs": (2, "|link3=Root/Finals"),
            "Root/Finals": (3, ""),
        },
        ["Root"],
    )
    client = fetcher(get)
    assert crawl(client, limit=1).fetched == 1
    assert "Root/Playoffs" not in cache.load_index()
    result = crawl(client)
    assert (result.fetched, result.subpages) == (2, 2)
    entry = cache.load_index()["Root/Playoffs"]
    assert (entry["source"], entry["parent"]) == ("subpage", "Root")
    get.calls.clear()
    assert crawl(client).fetched == 0
    assert get.content_titles() == []
    get.pages["Root/Playoffs"] = (4, "")
    assert crawl(client).changed == 1
    assert get.content_titles() == ["Root/Playoffs"]


def test_subpage_filter():
    assert subpage_links(
        "Root/Groups",
        """
    |link1=Root/Groups| link2 = Root/Play_offs
    |link3=Unrelated/Final|link4=Rootish/Final|link5=Root|link6=Root/Final
    """,
    ) == {"Root/Play offs", "Root", "Root/Final"}


@pytest.mark.parametrize("limit", [0, 1, 51])
def test_limit_and_batches(limit):
    get = FakeGet({f"Page {n}": (n, "") for n in range(105)})
    result = crawl(fetcher(get), limit=limit)
    assert result.fetched == limit
    assert len(get.content_titles()) == limit
    assert len(cache.load_index()) == limit
    assert all(
        len(call["titles"].split("|")) <= 50 for call in get.calls if "titles" in call
    )


def test_cache_roundtrip():
    assert cache.read_page("Root") is None
    record = {
        "title": "Root",
        "pageid": 1,
        "revid": 2,
        "timestamp": "2026-10-28T00:00:00Z",
        "wikitext": "{{Raw|é}}",
        "fetched_at": "2026-10-29T00:00:00Z",
    }
    cache.save_page(record)
    assert cache.read_page("Root") == record
    path = cache.data_dir() / cache.page_file("Root")
    assert len(path.parent.name) == 2
    assert json.loads(gzip.decompress(path.read_bytes())) == record
    cache.save_category(CATEGORY, ["Root"])
    category = json.loads(
        next((cache.data_dir() / "category").glob("*.json")).read_text()
    )
    assert category["titles"] == ["Root"]
    assert category["fetched_at"].endswith("Z")


def test_missing_and_three_rounds():
    get = FakeGet(
        {
            "Root": (1, "|link2=Root/1"),
            **{f"Root/{n}": (n + 1, f"|link2=Root/{n + 1}") for n in range(1, 5)},
        },
        ["Root", "Missing"],
    )
    result = crawl(fetcher(get))
    assert (result.fetched, result.missing, result.subpages) == (4, 1, 3)
    assert "Root/4" not in cache.load_index()


def test_progress_survives_later_failure():
    get = FakeGet({f"Page {n}": (n, "") for n in range(51)})

    def failing(params):
        if "content" in params.get("rvprop", "") and params["titles"] == "Page 50":
            raise RuntimeError("interrupted")
        return get(params)

    with pytest.raises(RuntimeError, match="interrupted"):
        crawl(fetcher(failing))
    assert len(cache.load_index()) == 50
    get.calls.clear()
    assert crawl(fetcher(get)).fetched == 1
    assert get.content_titles() == ["Page 50"]


def test_cli(monkeypatch):
    get = FakeGet()
    monkeypatch.setattr(cli, "Fetcher", lambda: fetcher(get))
    runner = CliRunner()
    for command in [["liquipedia", "--help"], ["liquipedia", "status"]]:
        result = runner.invoke(app, command)
        assert result.exit_code == 0, result.output
    assert "newest fetched_at=none" in result.output
    result = runner.invoke(app, ["liquipedia", "crawl", "--limit", "1"])
    assert result.exit_code == 0, result.output
    assert "fetched=1" in result.output
    assert len(result.output.splitlines()) <= 5
    result = runner.invoke(app, ["liquipedia", "status"])
    assert result.exit_code == 0, result.output
    assert "pages=1 subpages=0" in result.output
    assert "newest fetched_at=none" not in result.output


def test_match_namespace_continuation_revisions_and_combined_limit():
    get = FakeGet(
        {
            "Root": (1, ""),
            "Match:ID abcdefghij 0001": (2, "a"),
            "Match:ID abcdefghij 0002": (3, "b"),
        },
        ["Root"],
    )
    result = crawl(fetcher(get), limit=2)
    assert (result.fetched, result.match_pages) == (2, 1)
    assert get.content_titles() == ["Root", "Match:ID abcdefghij 0001"]
    get.calls.clear()
    result = crawl(fetcher(get))
    assert (result.fetched, result.unchanged, result.match_pages) == (1, 2, 2)
    assert cache.load_index()["Match:ID abcdefghij 0002"]["source"] == "match"
    get.calls.clear()
    assert crawl(fetcher(get), no_matches=True).fetched == 0
    assert not any(c.get("generator") for c in get.calls)
    get.calls.clear()
    get.pages["Match:ID abcdefghij 0001"] = (4, "new")
    assert crawl(fetcher(get)).changed == 1
    assert get.content_titles() == ["Match:ID abcdefghij 0001"]


def test_saved_namespace_info_response_skips_unchanged_revisions():
    from pathlib import Path

    response = json.loads(
        (
            Path(__file__).parent / "fixtures/liquipedia/lp_allpages_match_info.json"
        ).read_text()
    )
    cache.save_index(
        {
            p["title"]: {"revid": p["lastrevid"], "source": "match", "parent": None}
            for p in response["query"]["pages"].values()
        }
    )
    calls = []

    def get(params):
        calls.append(params)
        if params.get("list") == "categorymembers":
            return {"query": {"categorymembers": []}}
        if params.get("list") == "allpages":
            return {"query": {"allpages": []}}
        assert params["generator"] == "allpages"
        if params.get("gapcontinue"):
            assert params["gapcontinue"] == response["continue"]["gapcontinue"]
            return {"query": {"pages": {}}}
        return response

    result = crawl(fetcher(get))
    assert (result.fetched, result.match_pages, result.unchanged) == (0, 3, 3)
    assert len(calls) == 4  # category, subpage listing, two namespace pages


def test_listed_subpages_are_crawled_under_their_nearest_root():
    get = FakeGet(
        {"Root": (1, ""), "Root/Group Stage": (2, ""), "Rooted/X": (3, "")}, ["Root"]
    )
    get.listed = ["Root", "Root/Group Stage", "Rooted/X", "Other/Root"]
    result = crawl(fetcher(get))
    index = cache.load_index()
    assert index["Root/Group Stage"] == index["Root/Group Stage"] | {
        "source": "subpage",
        "parent": "Root",
    }
    assert "Rooted/X" not in index and result.subpages == 1


def test_subpage_links_drop_fragments_and_double_spaces():
    text = "|link1=Root/Chinese  Qualifier|link2=Root#Weekly Matches"
    assert subpage_links("Root/Main", text) == {"Root/Chinese Qualifier", "Root"}


@pytest.mark.parametrize("listing", ["full", "none"])
def test_listing_modes_preserve_tab_discovery(listing):
    get = FakeGet(
        {
            "Root": (1, "|link2=Root/Tabs"),
            "Root/Tabs": (2, ""),
            "Root/Unlinked": (3, ""),
            "Match:ID abcdefghij 0001": (4, ""),
        },
        ["Root"],
    )
    get.listed = ["Root/Unlinked"]
    result = crawl(fetcher(get), listing=listing)
    assert "Root/Tabs" in cache.load_index()
    full = listing == "full"
    assert ("Root/Unlinked" in cache.load_index()) is full
    assert result.match_pages == int(full)
    assert any(c.get("list") == "allpages" for c in get.calls) is full
    assert any(c.get("generator") == "allpages" for c in get.calls) is full


@pytest.mark.parametrize("listing", ["full", "none"])
def test_cli_listing_modes(monkeypatch, listing):
    get = FakeGet()
    monkeypatch.setattr(cli, "Fetcher", lambda: fetcher(get))
    result = CliRunner().invoke(app, ["liquipedia", "crawl", "--listing", listing])
    assert result.exit_code == 0, result.output
    assert any(c.get("list") == "allpages" for c in get.calls) is (listing == "full")


def test_invalid_listing_fails_before_queries():
    get = FakeGet()
    with pytest.raises(ValueError, match="listing"):
        crawl(fetcher(get), listing="unexpected")
    assert not get.calls
    result = CliRunner().invoke(app, ["liquipedia", "crawl", "--listing", "unexpected"])
    assert result.exit_code == 2
