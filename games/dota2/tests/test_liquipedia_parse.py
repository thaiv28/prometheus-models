"""Dota template parsing uses saved wikitext only."""

import gzip
import json
from collections import Counter
from pathlib import Path

import pytest

from promdota.liquipedia import parse

FIXTURES = Path(__file__).parent / "fixtures/liquipedia"


def page(name):
    return json.loads(gzip.decompress((FIXTURES / (name + ".json.gz")).read_bytes()))


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
    p = parse.parse_infobox(page("lp_PGL_Wallachia_7")["wikitext"])
    assert p["tier"] == "tier1"
    assert isinstance(p["leagueid"], int)
    p = parse.parse_infobox(
        "{{Infobox league|liquipediatiertype=Qualifier|leagueid=no}}"
    )
    assert (p["tier_type"], p["leagueid"]) == ("Qualifier", None)


def test_inline_games():
    p = page("lp_European_Pro_League_40")
    matches = parse.parse_matches(p["title"], p["wikitext"])
    assert len(matches) > 10
    games = [g for m in matches for g in m.games]
    assert any(g.dota_match_id == 8995367925 for g in games)
    assert all(g.winner in (1, 2) for g in games)
    assert any(g.duration_s for g in games)


def test_match_page_reversed_and_brackets():
    p = page("lp_Match_ID_y9zxBDdLAA_0001")
    (m,) = parse.parse_matches(p["title"], p["wikitext"])
    assert (m.team1_key, m.team2_key) == ("og", "vici gaming")
    assert (m.games[0].dota_match_id, m.games[0].team1_side, m.games[0].winner) == (
        8719042091,
        "dire",
        None,
    )
    assert m.winner is None
    assert m.start_utc.isoformat() == "2026-03-07T08:00:00+00:00"
    assert parse.match_page_key(p["title"]) == ("y9zxBDdLAA", "0001")
    assert parse.match_page_key("Other") is None
    assert parse.bracket_ids(page("lp_PGL_Wallachia_7")["wikitext"]) == ["i06NQD47ce"]
    assert parse.bracket_ids(page("lp_PGL_Wallachia_7_Group_Stage")["wikitext"]) == [
        "y9zxBDdLAA",
        "y9zxBDdLAB",
        "y9zxBDdLAC",
        "y9zxBDdLAD",
        "y9zxBDdLAE",
    ]
    assert parse.parse_matches("P", "{{Match}}") == []


def test_scheduled_unplayed_and_rejections():
    text = "{{Match|opponent1={{TeamOpponent|A}}|opponent2={{TeamOpponent|B}}|date=Jan 1, 2026 - 10:00 {{Abbr/SGT}}|bestof=3|map1={{Map|winner=1|team1side=radiant|length=43m36s}}|map2={{Map|finished=false|winner=2}}|map3={{Map}}}}"
    (m,) = parse.parse_matches("P", text)
    assert (
        m.best_of,
        m.games[0].duration_s,
        m.games[0].winner,
        m.games[0].team1_side,
    ) == (3, 2616, 1, "radiant")
    assert len(m.games) == 1
    unplayed = text.replace("winner=1", "winner=0")
    assert parse.parse_matches("P", unplayed) == []
    assert len(parse.parse_scheduled("P", unplayed)) == 1
    counts = Counter()
    assert not parse.parse_matches(
        "P", text.replace("Jan 1, 2026 - 10:00 {{Abbr/SGT}}", "bad"), counts=counts
    )
    assert counts["dateless"] == 1
    assert not parse.parse_matches(
        "P", text.replace("TeamOpponent|A", "TeamOpponent|bye")
    )
    assert parse.PARSER_VERSION == 2


def test_nested_params_and_zones():
    block = "{{Thing|one|x={{Other|a=b}}|y=[[Target|label]]<!--x-->|z=ok}}"
    assert parse.params(block) == {
        "x": "{{Other|a=b}}",
        "y": "[[Target|label]]",
        "z": "ok",
    }
    assert parse.positional(block) == ["one"]
    for zone, hour in (("EET", 8), ("CEST", 8), ("SGT", 2), ("UTC-3", 13)):
        dt, known, unknown = parse.parse_date(
            f"March 5, 2026 - 10:00 {{{{Abbr/{zone}}}}}"
        )
        assert (dt.hour, known, unknown) == (hour, 1, False)


def test_person_rosters():
    text = (
        "{{Opponent|X|players={{Persons|"
        + "".join("{{Person|" + name + "}}" for name in "ABCDE")
        + "}}}}"
    )
    assert [p.key for p in parse.parse_rosters(text)["x"]] == list("abcde")
