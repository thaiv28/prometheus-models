"""Offline matching, settlement and catalog-to-database regression checks."""

import json
from dataclasses import replace
from pathlib import Path

import pytest

from promr6.link import (
    Event,
    cross_check,
    link,
    market_row,
    normalize,
    scheduled_utc,
)

REPO = Path(__file__).resolve().parents[1]
FIXTURES = REPO / "tests" / "fixtures" / "kalshi"
TIME = "2026-10-28T21:00:00Z"


def event(
    ticker="series",
    names=("FÚRIA Female", "MIBR Female"),
    ids=("kr", "mibr"),
    scheduled=TIME,
    **kwargs,
):
    return Event(
        ticker,
        tuple(
            {
                "ticker": f"{ticker}-{i}",
                "team_name": name,
                "competitor_id": cid,
                "team_code": str(i),
                "scheduled_utc": scheduled,
                "open_time": "2026-10-27T21:00:00Z",
                "result": "yes" if i == 0 else "no",
            }
            for i, (name, cid) in enumerate(zip(names, ids))
        ),
        **kwargs,
    )


def match(mid=1, names=("FURIA GC", "MIBR GC"), ids=(10, 20), start=TIME):
    return {
        "match_id": mid,
        "team1_name": names[0],
        "team2_name": names[1],
        "team1_key": names[0].lower(),
        "team2_key": names[1].lower(),
        "team1_id": ids[0],
        "team2_id": ids[1],
        "start_utc": start,
        "winner": 1,
        "maps": [{"map_id": 100 + mid, "map_order": 1, "winner": 1}],
    }


@pytest.mark.parametrize(
    ("a", "b", "equal"),
    [
        ("FÚRIA Female", "FURIA GC", True),
        ("MIBR Female", "MIBR GC", True),
        ("Team Liquid", "Team Liquid Brazil", False),
        ("G2 Esports", "G2", True),
        ("The Team G2 Gaming Club", "G2 Esport", True),
        ("MIBR Women", "MIBR GC", True),
    ],
)
def test_normalize(a, b, equal):
    assert (normalize(a) == normalize(b)) == equal
    assert isinstance(normalize(a), tuple)


@pytest.mark.parametrize(
    ("date", "zone", "expected"),
    [
        ("Oct 30, 2026", "EDT", "2026-10-30T21:00:00Z"),
        ("Dec 30, 2026", "EST", "2026-12-30T22:00:00Z"),
    ],
)
def test_schedule(date, zone, expected):
    assert (
        scheduled_utc(f"match originally scheduled for {date} at 5:00 PM {zone}, then")
        == expected
    )


def test_invalid_schedule():
    assert scheduled_utc("no schedule") is None
    assert scheduled_utc("originally scheduled for Oct 99, 2026, then") is None


def test_date_only_schedule_is_unknown():
    assert scheduled_utc("originally scheduled for Dec 5, 2025, then") is None
    assert scheduled_utc("originally scheduled for Oct 99, 2026 at 5:00 PM EDT") is None


def test_three_passes():
    exact = event()
    renamed = event("renamed", names=("New Brand", "Other Brand"))
    fuzzy = event("fuzzy", names=("Furia G", "MIBR GC"), ids=("unknown", "unknown2"))
    result = link([renamed, fuzzy, exact], [match()])
    assert {r.event_ticker: r.method for r in result.links} == {
        "series": "exact",
        "renamed": "alias",
        "fuzzy": "anchor",
    }
    assert {
        a.competitor_id: (a.liquipedia_team_id, a.events) for a in result.aliases
    } == {
        "kr": (10, 2),
        "mibr": (20, 2),
        "unknown": (10, 1),
        "unknown2": (20, 1),
    }
    assert cross_check([renamed, fuzzy, exact], result.links, [match()]).agreements == 6


def test_order_free_and_alias_conflict():
    reversed_match = match(names=("MIBR GC", "FURIA GC"), ids=(20, 10))
    result = link([event()], [reversed_match])
    assert result.links[0].team_ids == (10, 20)
    assert cross_check([event()], result.links, [reversed_match]).checked == 2
    later = event("later", scheduled="2026-11-10T21:00:00Z")
    conflicting = match(2, ids=(99, 20), start="2026-11-10T21:00:00Z")
    renamed = event("renamed", names=("New Brand", "Other Brand"))
    result = link([event(), later, renamed], [match(), conflicting])
    assert [a.competitor_id for a in result.aliases] == ["mibr"]
    assert result.links[-1].match_id is None
    assert result.aliases[0].events == 2


def test_ambiguous_and_missing():
    result = link([event()], [match(), match(2)])
    assert result.links[0].match_id is None
    assert "ambiguous" in result.links[0].reason
    assert not result.aliases
    incomplete = replace(event(), markets=event().markets[:1])
    assert (
        link([incomplete], [match()]).links[0].reason
        == "expected two competitor markets"
    )
    no_time = replace(
        event(),
        markets=tuple(
            {**m, "scheduled_utc": None, "open_time": None} for m in event().markets
        ),
    )
    assert "missing" in link([no_time], [match()]).links[0].reason


@pytest.mark.parametrize(
    ("start", "linked"),
    [
        ("2026-10-29T21:00:00Z", True),
        ("2026-10-27T21:00:00Z", True),
        ("2026-10-30T03:00:00Z", True),
        ("2026-10-30T04:00:00Z", False),
    ],
)
def test_slip_window(start, linked):
    assert (
        link([event()], [match(start=start)]).links[0].match_id is not None
    ) == linked


def test_fallback_and_no_partial_alias():
    assert link([event(scheduled=None)], [match()]).links[0].method == "exact"
    renamed = event("rename", names=("New Brand", "Other Brand"), ids=("kr", "unknown"))
    assert link([event(), renamed], [match()]).links[-1].match_id is None


def test_maps_and_results():
    series = event("KXR6GAME-26X")
    # Reverse market ordering to verify inherited competitor identities.
    played = replace(
        event("KXR6MAP-26X-1", kind="map", map_number=1),
        markets=tuple(reversed(series.markets)),
    )
    unplayed = event("KXR6MAP-26X-2", kind="map", map_number=2)
    result = link([series, played, unplayed], [match()])
    assert result.links[1].map_id == 101
    assert result.links[1].team_ids == (20, 10)
    assert result.links[2].match_id == 1
    assert result.links[2].reason == "unplayed"
    checked = cross_check([series, played, unplayed], result.links, [match()])
    assert (checked.agreements, checked.checked, checked.mismatches) == (4, 4, [])
    wrong = match()
    wrong["winner"] = 2
    wrong["maps"][0]["winner"] = 2
    checked = cross_check([series, played], result.links[:2], [wrong])
    assert checked.agreements == 0 and checked.checked == 4
    assert len(checked.mismatches) == 4
    assert "map_id=101" in checked.mismatches[-1]
    assert link([played], [match()]).links[0].map_id == 101


def test_scalar_draw_and_unresolved_skipped():
    scalar = replace(
        event(), markets=tuple({**m, "result": "scalar"} for m in event().markets)
    )
    result = link([scalar], [match()])
    assert cross_check([scalar], result.links, [match()]).checked == 0
    drawn = {**match(), "winner": None}
    assert cross_check([event()], result.links, [drawn]).checked == 0


def test_old_ticker_does_not_supply_date():
    row = market_row(
        {
            "ticker": "KXR6GAME-25-DRX",
            "event_ticker": "KXR6GAME-25",
            "yes_sub_title": "DRX",
        },
        "KXR6GAME",
    )
    assert row["scheduled_utc"] is None
    assert row["team_code"] == "DRX"


@pytest.mark.parametrize(
    ("kalshi", "liquipedia", "code", "method"),
    [
        ("DRX", "KIWOOM DRX", "DRX", "anchor"),
        (
            "Bilibili Gaming",
            "Guangzhou Huadu Bilibili Gaming (Bilibili Gaming)",
            "BLG",
            "exact",
        ),
        (
            "Guangzhou Huadu Bilibili Gaming",
            "Guangzhou Huadu Bilibili Gaming (Bilibili Gaming)",
            "BLG",
            "exact",
        ),
        ("XLG Gaming", "Xi Lai Gaming", "XLG", "anchor"),
        ("eSports Cologne", "CGN Esports", "CGN", "anchor"),
        ("SGE Vision", "Eintracht Frankfurt Team Vision", "SGE", "anchor"),
        ("SGE Vision", "Eintracht Frankfurt", "SGE", None),
        ("Valorando", "VALORANDO", "VAL", "exact"),
    ],
)
def test_real_name_variants(kalshi, liquipedia, code, method):
    target = event(names=(kalshi, "Opponent"))
    target.markets[0]["team_code"] = code
    result = link([target], [match(names=(liquipedia, "Opponent"))])
    assert result.links[0].method == method
    if method is None:
        assert result.links[0].reason == "anchor: other team implausible"


def test_fuzzy_last_without_confirmed_side():
    target = event(names=("Furia G", "MIBR G"), ids=("x", "y"))
    result = link([target], [match()])
    assert result.links[0].method == "fuzzy"
    assert not result.aliases


@pytest.mark.parametrize("name", ["RIZON", "ALTERNATE aTTaX"])
def test_exact_team_preferred_over_subteam(name):
    target = event(names=(name, "Opponent"))
    matches = [
        match(
            1,
            names=(name + " Cherry" if name == "RIZON" else name + " Ruby", "Opponent"),
            ids=(30, 20),
        ),
        match(2, names=(name, "Opponent")),
    ]
    assert link([target], matches).links[0].match_id == 2
    # The exact team exists in the window, but plays somebody else.
    matches[1]["team2_name"] = "Different"
    matches[1]["team2_key"] = "different"
    matches[1]["team2_id"] = 40
    assert link([target], matches).links[0].match_id is None


def test_anchor_requires_unique_confirmed_team_and_plausible_other():
    target = event(names=("DRX", "Opponent"))
    candidates = [
        match(names=("KIWOOM DRX", "Opponent")),
        match(2, names=("DRX Academy", "Opponent"), ids=(30, 20)),
    ]
    assert link([target], candidates).links[0].match_id is None
    rejected = link([target], [match(names=("Unrelated", "Opponent"))]).links[0]
    assert rejected.match_id is None
    assert rejected.reason == "anchor: other team implausible"


def test_alias_learned_from_anchor_enables_later_round():
    later = "2026-11-10T21:00:00Z"
    renamed = event("first", names=("New Brand", "Other Brand"), scheduled=later)
    anchored = event("second", names=("DRX", "Opponent"))
    result = link(
        [renamed, anchored],
        [
            match(names=("KIWOOM DRX", "Opponent")),
            match(2, names=("KIWOOM DRX", "Opponent"), start=later),
        ],
    )
    assert [(r.match_id, r.method) for r in result.links] == [
        (2, "alias"),
        (1, "anchor"),
    ]
    assert {a.events for a in result.aliases} == {2}


def test_anchor_conflict_drops_alias_permanently():
    later = "2026-11-10T21:00:00Z"
    last = "2026-11-20T21:00:00Z"
    events = [
        event("first", names=("DRX", "Opponent")),
        event("second", names=("DRX", "Opponent"), scheduled=later),
        event("third", names=("New Brand", "Other Brand"), scheduled=last),
    ]
    result = link(
        events,
        [
            match(names=("KIWOOM DRX", "Opponent")),
            match(2, names=("KIWOOM DRX", "Opponent"), ids=(99, 20), start=later),
            match(3, names=("KIWOOM DRX", "Opponent"), start=last),
        ],
    )
    assert [r.method for r in result.links] == ["anchor", "anchor", None]
    assert [a.competitor_id for a in result.aliases] == ["mibr"]


def test_sge_short_name_via_learned_alias():
    later = "2026-11-10T21:00:00Z"
    events = [
        event("short", names=("SGE Vision", "Opponent"), scheduled=later),
        event("long", names=("SGE Vision", "Opponent")),
    ]
    result = link(
        events,
        [
            match(names=("Eintracht Frankfurt Team Vision", "Opponent")),
            match(2, names=("Eintracht Frankfurt", "Opponent"), start=later),
        ],
    )
    assert [r.method for r in result.links] == ["alias", "anchor"]


@pytest.mark.parametrize("series", ["KXR6GAME", "KXR6MAP"])
def test_r6_rules_with_colon_tournament(series):
    raw = {
        "ticker": f"{series}-26OCT311400ILLAZU-1-ILL",
        "event_ticker": f"{series}-26OCT311400ILLAZU-1",
        "yes_sub_title": "ILLYRIANS",
        "rules_primary": (
            "If ILLYRIANS wins the CCT Europe Closed Qualifier: Series #13 2026: "
            "ILLYRIANS vs. Azuolas R6 match originally scheduled for "
            "Oct 31, 2026 at 2:00 PM EDT, then the market resolves to Yes."
        ),
    }
    row = market_row(raw, series)
    assert row["scheduled_utc"] == "2026-10-31T18:00:00Z"
    assert row["event_name"] == "CCT Europe Closed Qualifier: Series #13 2026"
    assert row["kind"] == ("map" if series == "KXR6MAP" else "series")
    assert row["map_number"] == (1 if series == "KXR6MAP" else None)


def test_r6_normalization():
    assert normalize("GG Team G2 Esports") == normalize("G2")
    assert normalize("ENCE Academy") != normalize("ENCE")


def test_liquipedia_template_key_variants():
    target = event(names=("1WIN", "G2"))
    candidate = match(names=("Roster Display", "G2 Esports"))
    candidate["team1_key"] = "1WIN"
    assert link([target], [candidate]).links[0].method == "exact"
    candidate["team1_key"] = "1w"
    # 1w versus 1WIN reaches the existing 0.6 anchor threshold (2/3),
    # with G2 as the unique confirmed opponent; no abbreviation rule needed.
    assert link([target], [candidate]).links[0].method == "anchor"
    prior = event("prior", names=("1WIN", "G2"), scheduled="2026-10-20T21:00:00Z")
    known = match(2, names=("1WIN", "G2"), start="2026-10-20T21:00:00Z")
    result = link([target, prior], [candidate, known])
    assert [row.method for row in result.links] == ["alias", "exact"]


def test_academy_alone_does_not_make_anchor_opponent_plausible():
    target = event(names=("B8 Academy", "Inner Circle Academy"))
    correct = match(names=("B8 Academy", "Inner Circle Academy"))
    assert link([target], [correct]).links[0].method == "exact"
    candidate = match(names=("B8 Academy", "EF Academy"))
    rejected = link([target], [candidate]).links[0]
    assert rejected.match_id is None
    assert rejected.reason == "anchor: other team implausible"


def test_fixture_rules_catalog():
    from promr6.link import events_from_markets

    raw = json.loads((FIXTURES / "markets_sample.json").read_text())
    rows = [
        market_row(market, series)
        for series, markets in raw.items()
        for market in markets
    ]
    timed = rows[0]
    assert timed["scheduled_utc"] == "2026-10-25T16:00:00Z"
    assert timed["event_name"] == "Challenger League 2026"
    assert rows[2]["scheduled_utc"] is None
    assert rows[2]["event_name"] == "Blast R6 Major Munich"
    map_events = [e for e in events_from_markets(rows) if e.kind == "map"]
    assert {e.map_number for e in map_events} == {1, 2}
    assert {e.series_ticker for e in map_events} == {"KXR6GAME-26OCT251200FAZEFURIA"}


def test_loader_linker_fixture_catalog(tmp_path, monkeypatch, capsys):
    import importlib.util
    import sqlite3

    monkeypatch.setenv("PROMR6_DATA", str(tmp_path / "data"))
    database = tmp_path / "db" / "r6.db"
    database.parent.mkdir()
    monkeypatch.setenv("PROMR6_DB", str(database))
    raw = json.loads((FIXTURES / "markets_sample.json").read_text())
    catalog = tmp_path / "data" / "kalshi" / "markets"
    catalog.mkdir(parents=True)
    for series, markets in raw.items():
        (catalog / f"{series}.json").write_text(json.dumps(markets))
    with sqlite3.connect(database) as conn:
        conn.executescript((REPO / "scripts" / "001_create_tables.sql").read_text())
        conn.execute(
            "INSERT INTO events (event_id,title,section,international,excluded) VALUES (1,'Fixture','matches',1,0)"
        )
        conn.executemany(
            "INSERT INTO teams (team_id,key,name) VALUES (?,?,?)",
            [(10, "furia", "FURIA"), (20, "faze clan", "FaZe Clan")],
        )
        conn.execute(
            "INSERT INTO matches (match_id,event_id,page,ordinal,start_utc,time_known,team1_id,team2_id,score1,score2,winner) VALUES (1,1,'Fixture',1,'2026-10-25T16:00:00Z',1,10,20,2,0,1)"
        )
        conn.execute(
            "INSERT INTO maps (map_id,match_id,map_order,map_name,rounds1,rounds2,winner) VALUES (11,1,1,'Villa',3,7,2)"
        )
    modules = []
    for name in ("003_load_kalshi", "004_link_kalshi"):
        spec = importlib.util.spec_from_file_location(
            name, REPO / "scripts" / f"{name}.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)
    for _ in range(2):
        for module in modules:
            module.main()
    assert "kalshi_markets=12 missing_catalogs=0" in capsys.readouterr().out
    with sqlite3.connect(database) as conn:
        assert conn.execute("SELECT count(*) FROM kalshi_markets").fetchone()[0] == 12
        assert conn.execute("SELECT count(*) FROM kalshi_links").fetchone()[0] == 6
        assert conn.execute(
            "SELECT match_id,map_id FROM kalshi_links WHERE event_ticker=?",
            ("KXR6MAP-26OCT251200FAZEFURIA-1",),
        ).fetchone() == (1, 11)
        assert conn.execute("PRAGMA foreign_key_check").fetchall() == []
        conn.execute("UPDATE matches SET winner=2")
    modules[1].main()
    report = (database.parent / "link_report.txt").read_text()
    assert "unplayed" in report
    assert raw["KXR6GAME"][0]["ticker"] in report


def test_fixture_market_links_to_parsed_liquipedia_series():
    from promr6.link import events_from_markets
    from promr6.liquipedia.parse import parse_matches

    raw = json.loads((FIXTURES / "markets_sample.json").read_text())["KXR6GAME"][:2]
    # The captured page fixtures cover other tournaments/days. Parse a compact
    # representative R6 Match for the unchanged fixture market's real matchup.
    wikitext = """{{Matchlist|id=fixture|M1={{Match
      |opponent1={{TeamOpponent|FURIA Esports|score=2}}
      |opponent2={{TeamOpponent|FaZe Clan|score=1}}
      |date=2026-10-25 12:00 {{Abbr/EDT}}|finished=true|bestof=3
      |map1={{Map|map=Villa|score1=7|score2=3|finished=true}}
      |map2={{Map|map=Bank|score1=3|score2=7|finished=true}}
      |map3={{Map|map=Clubhouse|score1=7|score2=4|finished=true}}
    }}}}"""
    parsed = parse_matches("Fixture", wikitext)[0]
    candidate = match(
        names=(parsed.team1_key, parsed.team2_key),
        start=parsed.start_utc.isoformat().replace("+00:00", "Z"),
    )
    candidate["winner"] = parsed.winner
    events = events_from_markets([market_row(m, "KXR6GAME") for m in raw])
    result = link(events, [candidate])
    assert result.links[0].match_id == candidate["match_id"]
    assert result.links[0].method == "exact"
    assert cross_check(events, result.links, [candidate]).agreements == 2
