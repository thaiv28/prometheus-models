"""Offline schedule, frozen-call lifecycle and market feed checks."""

import gzip
import hashlib
import json
import re
import sqlite3
from datetime import UTC, datetime
from pathlib import Path
from urllib.error import HTTPError

import pytest

from promdota.feed import (
    current_prices,
    export,
    join_calls,
    page_text,
    pages_in,
    probabilities,
)
from promdota.liquipedia.parse import parse_scheduled

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests/fixtures/upcoming"
NOW = datetime(2026, 10, 29, 12, tzinfo=UTC)


def response(text, title="P"):
    return {
        "query": {
            "pages": {
                "1": {
                    "title": title,
                    "pageid": 1
                    if title == "P"
                    else int(hashlib.sha1(title.encode()).hexdigest()[:8], 16),
                    "revisions": [
                        {
                            "revid": int(
                                hashlib.sha1(text.encode()).hexdigest()[:8], 16
                            ),
                            "timestamp": "2026-10-29T12:00:00Z",
                            "slots": {"main": {"content": text}},
                        }
                    ],
                }
            }
        }
    }


def scheduled(a="Alpha", b="Beta", date="Oct 30, 2026 - 12:00", bestof=3):
    return f"{{{{Match|opponent1={{{{TeamOpponent|{a}}}}}|opponent2={{{{TeamOpponent|{b}}}}}|date={date} {{{{Abbr/UTC}}}}|bestof={bestof}|map1={{{{Map}}}}}}}}"


@pytest.fixture
def database(tmp_path):
    path = tmp_path / "test.db"
    with sqlite3.connect(path) as conn:
        conn.executescript((ROOT / "scripts/001_create_tables.sql").read_text())
        conn.execute(
            "INSERT INTO events(event_id,title,name,section,international,excluded,start_date,end_date) VALUES(1,'P','Test Event','tier1',0,0,'2026-10-24','2026-10-31')"
        )
        ids = [
            int(hashlib.sha1(("team:" + key).encode()).hexdigest()[:12], 16)
            for key in ("alpha", "beta")
        ]
        for team, name in zip(ids, ("Alpha", "Beta")):
            conn.execute("INSERT INTO teams VALUES(?,?,?)", (team, name.lower(), name))
        for mid, day in enumerate((2, 3), 1):
            conn.execute(
                "INSERT INTO matches VALUES(?,1,'P',? ,?,1,3,?,?,1,0,1)",
                (mid, mid, f"2026-01-{day:02}T10:00:00Z", *ids),
            )
            conn.execute(
                'INSERT INTO games(game_id,match_id,"order",winner,duration_s) VALUES(?,?,1,1,1800)',
                (mid, mid),
            )
    return path


def run(database, tmp_path, text="", now=NOW, **kwargs):
    return export(
        db=database,
        data=tmp_path / "data",
        now=now,
        liquipedia_fetcher=lambda **kw: (
            {"query": {"allpages": []}} if "list" in kw else response(text)
        ),
        kalshi_fetcher=lambda **kw: {"markets": [], "cursor": ""},
        **kwargs,
    )


def test_scheduled_fixture():
    with gzip.open(FIXTURE / "liquipedia_ongoing.json.gz", "rt") as handle:
        pages = list(pages_in(json.load(handle)))
    matches = [m for p in pages for m in parse_scheduled(p["title"], page_text(p))]
    upcoming = next(
        m for m in matches if (m.team1_key, m.team2_key) == ("vit", "nemiga")
    )
    assert upcoming.start_utc == datetime(2026, 10, 30, 12, tzinfo=UTC)
    assert upcoming.best_of == 3 and not upcoming.maps
    completed = parse_scheduled("P", scheduled().replace("{{Map}}", "{{Map|winner=1}}"))
    assert completed[0].maps == [(1, 0)] and completed[0].finished
    assert not parse_scheduled("P", scheduled("TBD"))
    assert not parse_scheduled("P", scheduled("bye"))
    assert not parse_scheduled("P", scheduled(date=""))
    assert not parse_scheduled(pages[1]["title"], page_text(pages[1]))


def test_export_lifecycle(database, tmp_path):
    feed = run(database, tmp_path, scheduled(bestof=1))
    assert set(feed) == {
        "version",
        "game",
        "name",
        "model",
        "generated",
        "data_through",
        "source",
        "sections",
        "matches",
    }
    upcoming = next(r for r in feed["matches"] if r["status"] == "upcoming")
    assert upcoming["p_game"] == upcoming["p_series"]
    assert feed["sections"] == [{"key": "T1", "label": "Tier 1", "major": True}]
    for row in feed["matches"]:
        assert set(row) == {
            "match_id",
            "start",
            "status",
            "section",
            "event",
            "best_of",
            "name1",
            "name2",
            "p_game",
            "p_series",
            "reconstructed",
            "score1",
            "score2",
            "winner",
            "url",
            "market",
        }
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z", row["start"])
        assert isinstance(row["p_game"], float) and 0 <= row["p_game"] <= 1
        assert isinstance(row["match_id"], str)
    log = tmp_path / "data/feed/predictions.json"
    frozen = log.read_bytes()
    later = datetime(2026, 10, 30, 13, tzinfo=UTC)
    feed = run(database, tmp_path, scheduled(bestof=5), now=later)
    assert log.read_bytes() == frozen
    live = next(r for r in feed["matches"] if r["status"] == "live")
    assert live["best_of"] == 1 and not live["reconstructed"]
    assert json.loads((tmp_path / "data/feed/dota2.json").read_text()) == feed
    # Missing pages retain a started call until the seven-day expiry.
    feed = run(database, tmp_path, now=datetime(2026, 10, 30, 19, tzinfo=UTC))
    pending = next(r for r in feed["matches"] if r["match_id"] == upcoming["match_id"])
    assert pending["status"] == "final" and pending["winner"] is None
    feed = run(database, tmp_path, now=datetime(2026, 11, 8, tzinfo=UTC))
    assert upcoming["match_id"] not in {r["match_id"] for r in feed["matches"]}


def test_reversed_call_join(database, tmp_path):
    run(database, tmp_path, scheduled("Beta", "Alpha"))
    log_path = tmp_path / "data/feed/predictions.json"
    calls = json.loads(log_path.read_text())
    call = next(iter(calls.values()))
    call.update(p_game=0.7, p_series=0.8)
    log_path.write_text(json.dumps(calls))
    with sqlite3.connect(database) as conn:
        conn.execute(
            "UPDATE matches SET start_utc='2026-10-30T12:00:00Z' WHERE start_utc LIKE '2026-01-03%'"
        )
    feed = run(database, tmp_path, now=datetime(2026, 10, 30, 15, tzinfo=UTC))
    final = next(r for r in feed["matches"] if r["start"] == "2026-10-30T12:00Z")
    assert final["status"] == "final" and not final["reconstructed"]
    assert (final["p_game"], final["p_series"]) == (0.3, 0.2)
    assert sum(r["start"] == final["start"] for r in feed["matches"]) == 1


def test_no_fetch_cache_and_pruning(database, tmp_path):
    run(database, tmp_path, scheduled())

    def forbidden(**kw):
        pytest.fail("network fetch in no-fetch mode")

    feed = export(
        db=database,
        data=tmp_path / "data",
        now=NOW,
        no_fetch=True,
        liquipedia_fetcher=forbidden,
        kalshi_fetcher=forbidden,
    )
    assert any(r["status"] == "upcoming" for r in feed["matches"])
    assert (
        json.loads((tmp_path / "data/feed/candidates.json").read_text())["matches"]
        == []
    )
    run(database, tmp_path)
    assert json.loads((tmp_path / "data/feed/predictions.json").read_text()) == {}


def test_rate_limited_fetch_uses_cached_schedule(database, tmp_path, capsys):
    def limited(**kw):
        raise HTTPError("https://liquipedia.net", 429, "Too Many Requests", {}, None)

    def export_limited():
        return export(
            db=database,
            data=tmp_path / "data",
            now=NOW,
            liquipedia_fetcher=limited,
            kalshi_fetcher=lambda **kw: {"markets": [], "cursor": ""},
        )

    with pytest.raises(HTTPError):
        export_limited()
    run(database, tmp_path, scheduled())
    feed = export_limited()
    assert any(r["status"] == "upcoming" for r in feed["matches"])
    assert "liquipedia_stale=1" in capsys.readouterr().out


def test_current_market_orientation_spread_and_aliases():
    raw = json.loads(
        (FIXTURE / "kalshi_open_KXCS2GAME.json")
        .read_text()
        .replace("KXCS2GAME", "KXDOTA2GAME")
        .replace("CS2 match", "Dota 2 match")
    )["markets"]
    event = raw[0]["event_ticker"]
    pair = [dict(m) for m in raw if m["event_ticker"] == event]
    assert len(pair) == 2
    candidate = {
        "match_id": "x",
        "start_utc": "2026-10-29T18:00Z",
        "team1_id": 1,
        "team2_id": 2,
        "team1_name": "Unrelated First",
        "team2_name": "Unrelated Second",
        "team1_key": "first",
        "team2_key": "second",
    }
    aliases = {
        pair[0]["custom_strike"]["esports_competitor"]: 2,
        pair[1]["custom_strike"]["esports_competitor"]: 1,
    }
    pair[0].update(yes_bid_dollars="0.3", yes_ask_dollars="0.4")
    pair[1].update(yes_bid_dollars="0", yes_ask_dollars="0")
    price = current_prices(pair, [candidate], aliases, NOW)["x"]
    assert price["p"] == pytest.approx(0.65)
    assert price["at"] == "2026-10-29T12:00Z"
    pair[0]["yes_ask_dollars"] = "0.41"
    assert not current_prices(pair, [candidate], aliases, NOW)
    pair[1].update(yes_bid_dollars="0.6", yes_ask_dollars="0.65")
    assert current_prices(pair, [candidate], aliases, NOW)["x"]["p"] == pytest.approx(
        0.625
    )


def test_join_closest_once_and_unknown_bestof():
    calls = {"a": {"start": "2026-10-29T12:00Z", "team1_id": 1, "team2_id": 2}}
    matches = [
        {"match_id": i, "start_utc": t, "team1_id": 2, "team2_id": 1}
        for i, t in [(1, "2026-10-29T13:00Z"), (2, "2026-10-29T12:01Z")]
    ]
    assert join_calls(matches, calls, NOW) == ({"2": "a"}, {"a"})
    p = probabilities(0.7, 2, {"3": 0.83})
    assert p["best_of"] is None
    assert p["p_series"] == pytest.approx(0.784)


def test_fetch_batches_pagination_and_current_price(database, tmp_path):
    with sqlite3.connect(database) as conn:
        # More than one batch, and one event outside the date window.
        for i in range(51):
            conn.execute(
                "INSERT INTO events(event_id,title,start_date,end_date,excluded,section,international) VALUES(?,?,?,?,0,'tier1',0)",
                (i + 2, f"Event/{i}", "2026-10-24", "2026-10-31"),
            )
        conn.execute(
            "INSERT INTO events(event_id,title,start_date,end_date,excluded,section,international) VALUES(99,'Old','2020-01-01','2020-01-02',0,'tier1',0)"
        )
    lp_queries, k_queries = [], []

    def lp(**kw):
        if "list" in kw:
            return {"query": {"allpages": []}}
        lp_queries.append(kw)
        return response(scheduled()) if "P" in kw["titles"].split("|") else response("")

    def kalshi(**kw):
        k_queries.append(kw)
        side = 1 if kw["cursor"] is None else 2
        return {
            "markets": [
                {
                    "ticker": f"KXDOTA2GAME-TEST-{side}",
                    "event_ticker": "KXDOTA2GAME-TEST",
                    "yes_sub_title": "Alpha" if side == 1 else "Beta",
                    "rules_primary": f"If {'Alpha' if side == 1 else 'Beta'} wins the Test: Alpha vs Beta Dota 2 match originally scheduled for Oct 30, 2026 at 8:00 AM EDT, then Yes.",
                    "yes_bid_dollars": "0.60",
                    "yes_ask_dollars": "0.64",
                }
            ],
            "cursor": "next" if side == 1 else "",
        }

    feed = export(
        db=database,
        data=tmp_path / "data",
        now=NOW,
        liquipedia_fetcher=lp,
        kalshi_fetcher=kalshi,
    )
    assert [len(q["titles"].split("|")) for q in lp_queries] == [50, 2, 50, 2]
    assert all(
        q["action"] == "query" and q.get("rvslots", "main") == "main"
        for q in lp_queries
    )
    assert [q["cursor"] for q in k_queries] == [None, "next"]
    upcoming = next(r for r in feed["matches"] if r["status"] == "upcoming")
    assert upcoming["market"]["p"] == 0.62
    private = json.loads((tmp_path / "data/feed/candidates.json").read_text())
    saved = private["matches"][0]["execution_candidate"]
    assert saved["teams"] == ["Alpha", "Beta"]
    assert saved["start"] == "2026-10-30T12:00Z"
    assert saved["provenance"]["match_id"] == upcoming["match_id"]
    assert saved["raw"]["Alpha"] == round(saved["provenance"]["p_series"], 6)
    with gzip.open(tmp_path / "data/feed/upcoming/latest.json.gz", "rt") as handle:
        assert len(json.load(handle)["pages"]) == 52


def test_page_final_requires_prior_call_and_unrated_skips(database, tmp_path, capsys):
    # Live or final first discovered after start cannot create a call.
    played = (
        scheduled(date="Oct 28, 2026 - 12:00")
        .replace("{{Map}}", "{{Map|winner=1}}")
        .replace("|bestof=3", "|finished=true|bestof=3")
    )
    feed = run(
        database,
        tmp_path,
        played + scheduled("Unknown", "Beta") + scheduled("TBD", "Beta"),
    )
    assert not any("|" in r["match_id"] for r in feed["matches"])
    assert "skipped_unrated=1 skipped_tbd=1" in capsys.readouterr().out
    run(database, tmp_path, scheduled())
    played = (
        scheduled()
        .replace("{{Map}}", "{{Map|winner=1}}")
        .replace("|bestof=3", "|finished=true|bestof=3")
    )
    feed = run(database, tmp_path, played, now=datetime(2026, 10, 30, 14, tzinfo=UTC))
    final = next(r for r in feed["matches"] if "|" in r["match_id"])
    assert (final["status"], final["score1"], final["score2"], final["winner"]) == (
        "final",
        1,
        0,
        1,
    )


def test_closing_candle_orientation(database, tmp_path):
    root = tmp_path / "data"
    candles = root / "kalshi/candles"
    candles.mkdir(parents=True)
    with sqlite3.connect(database) as conn:
        mid, start, team2 = conn.execute(
            "SELECT match_id,start_utc,team2_id FROM matches ORDER BY start_utc DESC LIMIT 1"
        ).fetchone()
        conn.executescript("""CREATE TABLE kalshi_links(match_id INTEGER,event_ticker TEXT,kind TEXT);
            CREATE TABLE kalshi_markets(event_ticker TEXT,ticker TEXT,competitor_id TEXT);
            CREATE TABLE team_aliases(competitor_id TEXT,liquipedia_team_id INTEGER);""")
        conn.execute(
            "INSERT INTO kalshi_links VALUES(?,'KXDOTA2GAME-TEST','series')", (mid,)
        )
        conn.execute(
            "INSERT INTO kalshi_markets VALUES('KXDOTA2GAME-TEST','TEST-SECOND','beta')"
        )
        conn.execute("INSERT INTO team_aliases VALUES('beta',?)", (team2,))
    from promdota.feed import instant

    ts = int(instant(start).timestamp())

    def candle(end, bid, ask):
        return {
            "end_period_ts": end,
            "yes_bid": {"close_dollars": bid},
            "yes_ask": {"close_dollars": ask},
        }

    with gzip.open(candles / "TEST-SECOND.json.gz", "wt") as handle:
        json.dump(
            {
                "candlesticks": [
                    candle(ts - 3600, 0.2, 0.4),
                    candle(ts, 0.3, 0.5),
                    candle(ts + 3600, 0.8, 0.9),
                ]
            },
            handle,
        )
    feed = export(db=database, data=root, now=NOW, no_fetch=True)
    final = next(r for r in feed["matches"] if r["match_id"] == str(mid))
    assert final["market"]["p"] == 0.6
    assert final["market"]["at"] == "2026-01-03T10:00Z"


def test_snapshot_roundtrip_matches_database(database, tmp_path, monkeypatch):
    from promdota.feed import build_state, load_state, save_state

    root = tmp_path / "snapshot"
    with sqlite3.connect(database) as conn:
        state = build_state(conn, root)
    path = tmp_path / "state.pkl.gz"
    save_state(state, path)
    loaded = load_state(path)
    expected = run(database, tmp_path, scheduled())

    def forbidden(*args, **kwargs):
        pytest.fail("snapshot export opened a database")

    monkeypatch.setattr(sqlite3, "connect", forbidden)
    actual = export(
        loaded,
        db=tmp_path / "missing.db",
        data=root,
        now=NOW,
        liquipedia_fetcher=lambda **kw: (
            {"query": {"allpages": []}} if "list" in kw else response(scheduled())
        ),
        kalshi_fetcher=lambda **kw: {"markets": [], "cursor": ""},
    )
    assert actual == expected
    # Export must not change reusable snapshot rows.
    assert export(loaded, data=root, now=NOW, no_fetch=True) == expected
    assert loaded["rows"] == state["rows"]
    state["version"] += 1
    save_state(state, path)
    with pytest.raises(ValueError, match="Unsupported feed state version"):
        load_state(path)


def test_snapshot_cli_never_opens_db(database, tmp_path, monkeypatch):
    from typer.testing import CliRunner

    from promdota.feed import build_state, save_state
    from promdota.main import app

    with sqlite3.connect(database) as conn:
        state = build_state(conn, tmp_path)
    path = tmp_path / "state.pkl.gz"
    save_state(state, path)
    expected = export(db=database, data=tmp_path / "db-feed", no_fetch=True)
    monkeypatch.setenv("PROMDOTA_DATA", str(tmp_path / "cli-feed"))

    def forbidden(*args, **kwargs):
        pytest.fail("CLI snapshot export opened a database")

    monkeypatch.setattr(sqlite3, "connect", forbidden)
    out = tmp_path / "feed.json"
    result = CliRunner().invoke(
        app,
        [
            "export",
            "--state",
            str(path),
            "--out",
            str(out),
            "--no-fetch",
            "--candidates",
            str(tmp_path / "private.json"),
        ],
    )
    assert result.exit_code == 0, result.output
    assert json.loads((tmp_path / "private.json").read_text())["matches"] == []
    actual = json.loads(out.read_text())
    actual.pop("generated")
    expected.pop("generated")
    assert actual == expected


def test_upcoming_root_subpage_and_bracket_discovery(database, tmp_path):
    queries = []
    title = "Match:ID abcdef1234 R01_M001"

    def fetch(**kw):
        queries.append(kw)
        if kw.get("list") == "allpages":
            if kw["apnamespace"] == 130:
                assert kw["apprefix"] == "ID abcdef1234 "
                return {"query": {"allpages": [{"title": title}]}}
            assert kw["apprefix"] == "P/"
            if not kw.get("apcontinue"):
                return {
                    "query": {"allpages": [{"title": "P/Group Stage"}]},
                    "continue": {"apcontinue": "P/Next", "continue": "-||"},
                }
            return {"query": {"allpages": []}}
        texts = {
            "P": "",
            "P/Group Stage": "{{Bracket|id=abcdef1234}}",
            title: scheduled().replace("{{Match|", "{{MatchPage|"),
        }
        return {
            "query": {
                "pages": {
                    str(i): next(
                        iter(response(texts[name], name)["query"]["pages"].values())
                    )
                    for i, name in enumerate(kw["titles"].split("|"))
                }
            }
        }

    feed = export(
        db=database,
        data=tmp_path / "data",
        now=NOW,
        liquipedia_fetcher=fetch,
        kalshi_fetcher=lambda **kw: {"markets": []},
    )
    upcoming = next(r for r in feed["matches"] if r["status"] == "upcoming")
    assert upcoming["event"] == "Test Event"
    assert "Match%3AID" in upcoming["url"]
    assert all(q["action"] == "query" for q in queries)
    assert len([q for q in queries if "apprefix" in q]) == 3
    cached = export(db=database, data=tmp_path / "data", now=NOW, no_fetch=True)
    assert cached == feed
    queries.clear()
    warm = export(
        db=database,
        data=tmp_path / "data",
        now=NOW,
        liquipedia_fetcher=fetch,
        kalshi_fetcher=lambda **kw: {"markets": []},
    )
    assert warm == feed
    assert len(queries) == 1
    assert len(queries[0]["titles"].split("|")) == 3
    assert queries[0]["rvprop"] == "ids|timestamp"


def test_current_form_includes_unscored_and_null_stat_appearances(database):
    from promdota.feed import current_form
    from promdota.ratings.layers import causal_form_features
    from promdota.ratings.replay import load_lineups

    with sqlite3.connect(database) as conn:
        for player in range(1, 11):
            conn.execute(
                "INSERT INTO players VALUES(?,?,?)", (player, str(player), str(player))
            )
        for game in (1, 2):
            for player in range(1, 11):
                conn.execute(
                    "INSERT INTO player_games(game_id,player_id,team,kills,deaths,assists) VALUES(?,?,?,?,0,0)",
                    (game, player, 1 if player <= 5 else 2, player * game),
                )
        # Unscored games still add form history, and null stats still decay it.
        conn.execute("UPDATE games SET winner=NULL WHERE game_id=1")
        conn.execute(
            'INSERT INTO games(game_id,match_id,"order",duration_s) VALUES(3,2,2,1800)'
        )
        for player in range(1, 11):
            conn.execute(
                "INSERT INTO player_games(game_id,player_id,team) VALUES(3,?,?)",
                (player, 1 if player <= 5 else 2),
            )
        # A fourth appearance exposes the terminal history through the benchmark feature.
        conn.execute(
            'INSERT INTO games(game_id,match_id,"order",duration_s) VALUES(4,2,3,1800)'
        )
        for player in range(1, 11):
            conn.execute(
                "INSERT INTO player_games(game_id,player_id,team) VALUES(4,?,?)",
                (player, 1 if player <= 5 else 2),
            )
        history = current_form(conn, 3)
        expected = causal_form_features(conn, load_lineups(conn)).loc[4]
        assert sum(history[p] for p in range(1, 6)) / 5 == pytest.approx(
            expected.form1_3
        )
        assert sum(history[p] for p in range(6, 11)) / 5 == pytest.approx(
            expected.form2_3
        )


def test_export_applies_frozen_form_to_latest_rated_starters(database, tmp_path):
    import math
    from types import SimpleNamespace

    from promdota.feed import build_state, load_state, save_state

    with sqlite3.connect(database) as conn:
        for player in range(1, 11):
            conn.execute(
                "INSERT INTO players VALUES(?,?,?)", (player, str(player), str(player))
            )
            for game in (1, 2):
                conn.execute(
                    "INSERT INTO player_games(game_id,player_id,team) VALUES(?,?,?)",
                    (game, player, 1 if player <= 5 else 2),
                )
        state = build_state(conn, tmp_path)
    ids = sorted(state["teams"], key=lambda tid: state["teams"][tid]["key"])
    state["form_weight"] = 0.7
    state["form"] = {player: 2.0 if player <= 5 else 1.0 for player in range(1, 11)}
    baseline = state["model"].predict(
        SimpleNamespace(
            team1_id=ids[0],
            team2_id=ids[1],
            game_id=None,
            section="tier1",
            start_utc="2026-10-30T12:00Z",
        )
    )
    expected = 1 / (1 + math.exp(-(math.log(baseline / (1 - baseline)) + 0.7)))
    path = tmp_path / "state.pkl.gz"
    save_state(state, path)
    loaded = load_state(path)
    assert loaded["form_half_life"] == state["form_half_life"]
    assert loaded["form_weight"] == 0.7
    actual = export(
        loaded,
        data=tmp_path / "export",
        now=NOW,
        liquipedia_fetcher=lambda **kw: (
            {"query": {"allpages": []}} if "list" in kw else response(scheduled())
        ),
        kalshi_fetcher=lambda **kw: {"markets": []},
    )
    row = next(r for r in actual["matches"] if r["status"] == "upcoming")
    assert row["p_game"] == round(expected, 4)
    assert row["p_game"] != round(baseline, 4)


def test_saved_dota_match_page_fixture():
    from promdota.liquipedia.parse import bracket_ids

    fixture = ROOT / "tests/fixtures/liquipedia"
    with gzip.open(fixture / "lp_PGL_Wallachia_7_Group_Stage.json.gz", "rt") as handle:
        root = json.load(handle)
    assert "y9zxBDdLAA" in bracket_ids(root["wikitext"])
    with gzip.open(fixture / "lp_Match_ID_y9zxBDdLAA_0001.json.gz", "rt") as handle:
        page = json.load(handle)
    match = parse_scheduled(page["title"], page["wikitext"])[0]
    assert (match.team1_key, match.team2_key, match.best_of) == ("og", "vici gaming", 3)


def test_incremental_pages_and_prefix_expiry(database, tmp_path, capsys):
    from datetime import timedelta
    from time import perf_counter

    from promdota.feed import build_state

    with sqlite3.connect(database) as conn:
        state = build_state(conn, tmp_path)
    calls = []
    texts = {"P": scheduled(), "P/Sub": ""}

    def fetch(**kw):
        calls.append(kw)
        if "list" in kw:
            return {"query": {"allpages": [{"title": "P/Sub"}]}}
        return {
            "query": {
                "pages": {
                    t: next(iter(response(texts[t], t)["query"]["pages"].values()))
                    for t in kw["titles"].split("|")
                }
            }
        }

    def timed(now):
        calls.clear()
        start = perf_counter()
        export(
            state,
            data=tmp_path / "export",
            now=now,
            liquipedia_fetcher=fetch,
            kalshi_fetcher=lambda **kw: {"markets": []},
        )
        return perf_counter() - start, sum(
            len(q["titles"].split("|"))
            for q in calls
            if "content" in q.get("rvprop", "")
        )

    first, fetched = timed(NOW)
    assert fetched == 2
    second, fetched = timed(NOW + timedelta(minutes=15))
    assert fetched == 0
    assert len(calls) == 1 and calls[0]["rvprop"] == "ids|timestamp"
    assert "pages_checked=2 pages_fetched=0 pages_reused=2" in capsys.readouterr().out
    print(
        f"offline export first={first:.6f}s pages_fetched=2 second={second:.6f}s pages_fetched=0 pages_reused=2"
    )
    texts["P/Sub"] = "changed"
    assert timed(NOW + timedelta(minutes=30))[1] == 1
    assert [q["titles"] for q in calls if "content" in q.get("rvprop", "")] == ["P/Sub"]
    timed(NOW + timedelta(hours=6))
    assert any("list" in q for q in calls)
    cache = tmp_path / "export/feed/upcoming/latest.json.gz"
    with gzip.open(cache, "rt") as handle:
        old = json.load(handle)
    old["version"] = 1
    with gzip.open(cache, "wt") as handle:
        json.dump(old, handle)
    assert timed(NOW + timedelta(hours=6, minutes=15))[1] == 2
