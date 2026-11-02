"""R6 template parsing uses saved raw API responses only."""

import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import pytest

from promr6.liquipedia import parse, regions

FIXTURES = Path(__file__).parent / "fixtures/liquipedia"


def page(number):
    raw = json.loads((FIXTURES / f"page{number}.json").read_text())
    p = next(iter(raw["query"]["pages"].values()))
    return p["title"], p["revisions"][0]["slots"]["main"]["*"]


@pytest.mark.parametrize(
    "value,expected",
    [
        ("1", "tier1"),
        ("2", "tier2"),
        ("3", "tier3"),
        ("4", "tier3"),
        ("S-Tier", "unknown"),
        (None, "unknown"),
    ],
)
def test_tiers(value, expected):
    assert parse.normalize_tier(value) == expected
    assert parse.section(expected) == expected


def test_infobox():
    assert parse.parse_infobox(page(4)[1])["tier"] == "tier1"
    assert parse.parse_infobox(page(3)[1])["tier"] == "tier3"
    p = parse.parse_infobox(
        "{{Infobox league|liquipediatiertype=Qualifier|type=Online|prizepoolusd=10,000}}"
    )
    assert (p["tier_type"], p["type"], p["prize_usd"]) == ("Qualifier", "Online", 10000)


def test_group_stage_all_nine_matchlists():
    title, text = page(2)
    assert len(parse.blocks(text, "Matchlist")) == 9
    matches = parse.parse_matches(title, text)
    assert len(matches) == 45
    assert all(len(m.maps) == 1 for m in matches)
    first = matches[0]
    assert (first.team1_key, first.team2_key, first.start_utc, first.siegegg_id) == (
        "darkzero",
        "wildcard",
        datetime(2026, 9, 9, 18, tzinfo=UTC),
        6168,
    )
    m = first.maps[0]
    assert (m.map_name, m.rounds1, m.rounds2, m.winner) == ("Villa", 3, 7, 2)
    assert first.substitutions == {1: [("Koshi", "J9O")], 2: []}


def test_future_scheduled_only():
    title, text = page(3)
    assert parse.parse_matches(title, text) == []
    scheduled = parse.parse_scheduled(title, text)
    assert len(scheduled) == 8
    assert all(not m.finished and not m.maps for m in scheduled)


def test_legacy_team_cards_and_overtime():
    title, text = page(6)
    cards = parse.roster_cards(text)
    assert len(cards) == 16
    assert all(len(card.players) == 5 and card.complete for card in cards.values())
    counts = Counter()
    matches = parse.parse_matches(title, text, counts=counts)
    # This snapshot contains standings walkover_win parameters, no forfeited Match.
    assert counts["walkovers"] == 0
    overtime = next(m for s in matches for m in s.maps if m.t1_ot or m.t2_ot)
    assert overtime.rounds1 == overtime.t1_atk + overtime.t1_def + overtime.t1_ot
    assert overtime.rounds2 == overtime.t2_atk + overtime.t2_def + overtime.t2_ot
    assert max(overtime.rounds1, overtime.rounds2) > 7


def test_imported_person_rosters_are_incomplete():
    cards = parse.roster_cards(page(4)[1])
    assert cards
    assert any(not card.complete for card in cards.values())
    text = "{{Opponent|X|import=true|players={{Persons|{{Person|A|type=staff}}|{{Person|B|played=false}}|{{Person|C|role=Captain}}}}}}"
    card = parse.roster_cards(text)["x"]
    assert card.players == (parse.PlayerRef("c", "C"),)
    assert not card.complete
    text = "{{TeamCard|team=X|t1p1=A|t1p2=B|t1p3=C|t1p4=D|t1p5=E|t1p6=Sub}}"
    assert [p.name for p in parse.parse_rosters(text)["x"]] == list("ABCDE")
    # Singular Person wrapper appears on current R6 pages.
    card = parse.roster_cards(
        "{{Opponent|X|import=true|players={{Person|{{Person|Y}}}}}}"
    )["x"]
    assert card.players == (parse.PlayerRef("y", "Y"),)


def match(extra="", op1="", op2=""):
    return (
        "{{Match|date=2026-01-01 10:00 {{Abbr/UTC}}|opponent1={{TeamOpponent|A"
        + op1
        + "}}|opponent2={{TeamOpponent|B"
        + op2
        + "}}"
        + extra
        + "}}"
    )


@pytest.mark.parametrize(
    "extra,op1,op2",
    [
        ("|walkover=1", "", ""),
        ("", "|score=W", "|score=FF"),
        ("", "|score=L", "|score=DQ"),
    ],
)
def test_walkovers(extra, op1, op2):
    counts = Counter()
    text = match(
        extra + "|map1={{Map|map=Villa|finished=true|score1=7|score2=0}}", op1, op2
    )
    (m,) = parse.parse_matches("P", text, counts=counts)
    assert m.walkover and not m.maps and m.winner is None
    assert counts["walkovers"] == counts["unresolved_matches"] == 1
    assert sum(m.walkover for m in parse.parse_matches(*page(4))) == 2


def test_map_scores_finished_and_unresolved():
    text = match(
        "|bestof=3|map1={{Map|map=Bank|score1=8|score2=7}}|map2={{Map|finished=true|t1atk=2|t1def=5|t2atk=1|t2def=3|score1=0|score2=9}}|map3={{Map|finished=skip|t1atk=7|t2atk=1}}"
    )
    (m,) = parse.parse_matches("P", text)
    assert (m.best_of, m.winner, len(m.maps)) == (3, 1, 2)
    assert (m.maps[1].rounds1, m.maps[1].rounds2) == (7, 4)
    counts = Counter()
    (m,) = parse.parse_matches("P", match("|finished=true"), counts=counts)
    assert m.winner is None and counts["unresolved_matches"] == 1
    assert not parse.parse_matches(
        "P", match("|map1={{Map|finished=true|score1=6|score2=6}}")
    )
    assert parse.PARSER_VERSION == 2


def test_series_score_without_maps_and_tiers():
    (m,) = parse.parse_matches("P", match("|finished=true", "|score=2", "|score=0"))
    assert (m.score1, m.score2, m.winner, m.maps) == (2, 0, 1, [])
    (m,) = parse.parse_matches("P", match("|finished=true", "|score=1", "|score=1"))
    assert m.winner is None
    (m,) = parse.parse_matches("P", match("|finished=true", "|score=W", "|score=FF"))
    assert m.walkover and m.winner is None
    assert parse.normalize_tier("5") == "tier3"
    assert parse.parse_date("2026-01-01 10:00 {{Abbr/BRST}}")[0].hour == 12


def test_nested_params_and_zones():
    block = "{{Thing|one|x={{Other|a=b}}|y=[[Target|label]]<!--x-->|z=ok}}"
    assert parse.params(block) == {
        "x": "{{Other|a=b}}",
        "y": "[[Target|label]]",
        "z": "ok",
    }
    assert parse.positional(block) == ["one"]
    for zone, hour in (
        ("EDT", 14),
        ("EST", 15),
        ("CEST", 8),
        ("BRT", 13),
        ("SGT", 2),
        ("UTC-3", 13),
        ("UTC+05:30", 4),
    ):
        dt, known, unknown = parse.parse_date(f"2026-03-05 10:00 {{{{Abbr/{zone}}}}}")
        assert (dt.hour, known, unknown) == (hour, 1, False)
    assert parse.parse_date("May 16, 2022 - 13:20 {{Abbr/EDT}}")[0].hour == 17
    assert parse.parse_date("2026-03-05")[1:] == (0, False)
    counts = Counter()
    parse.parse_matches(
        "P", match("|finished=true").replace("Abbr/UTC", "Abbr/UNKNOWN"), counts=counts
    )
    assert counts["unknown_tz"] == 1
    assert parse.parse_date("2026-03-05 10:00 {{Abbr/UNKNOWN}}")[1] == 0
    assert parse.parse_date("bad") == (None, 0, False)
    counts = Counter()
    assert not parse.parse_matches(
        "P", match().replace("2026-01-01 10:00", "bad"), counts=counts
    )
    assert counts["dateless"] == 1
    assert not parse.parse_matches(
        "P", match().replace("TeamOpponent|A", "TeamOpponent|bye")
    )


@pytest.mark.parametrize(
    "country,expected",
    [
        ("United States", "NA"),
        ("MENA", "EU"),
        ("Brazil", "SA"),
        ("Japan", "APAC"),
        ("Oceania", "APAC"),
        ("China", "CN"),
        (None, None),
    ],
)
def test_regions(country, expected):
    assert regions.region(country) == expected
