from copy import deepcopy
from datetime import datetime
from types import SimpleNamespace

import pytest

from promdota.ratings.elo import EloConfig, EloModel, TeamElo
from promdota.ratings.models import MODELS, PARAM_GRIDS
from promdota.ratings.regions import REGION_CODES, macro_region


def row(**kwargs):
    values = {
        "start_utc": "2026-01-01T12:00:00Z",
        "game_id": 1,
        "team1_id": 10,
        "team2_id": 20,
        "score1": 1,
        "score2": 0,
        "won": 1,
        "region": "un",
        "international": 0,
    }
    return SimpleNamespace(**(values | kwargs))


def test_binary_and_margin_credit():
    binary = EloModel()
    assert binary.score(row()) == 1
    assert binary.score(row(won=0)) == 0
    margin = EloModel(credit="margin", c=4, k=32)
    game = row(score1=13, score2=11)
    assert margin.score(game) == pytest.approx(0.7310585786)
    assert margin.score(row(score1=13, score2=3)) == pytest.approx(0.9933071491)
    assert margin.score(row(score1=11, score2=13, won=0)) == pytest.approx(
        1 - margin.score(game)
    )
    with pytest.raises(ValueError, match="credit"):
        EloModel(credit="round")


def test_player_mean_equal_updates_and_initialization():
    lineups = {1: ((1, 2, 3, 4, 5), (6, 7, 8, 9, 11))}
    model = EloModel(unit="player", k=32, lineups=lineups)
    model.ratings.update({1: 1600, 2: 1400})
    assert model.predict(row()) == 0.5
    before = model.ratings.copy()
    model.update(row())
    assert [model.ratings[p] - before[p] for p in lineups[1][0]] == [16] * 5
    assert [model.ratings[p] - before[p] for p in lineups[1][1]] == [-16] * 5
    for mode, initial in (("fixed", 1500), ("teammates", 1600)):
        model = EloModel(unit="player", lineups=lineups, new_player=mode)
        model.ratings[1] = 1600
        model.predict(row())
        assert model.ratings[2] == initial
        assert model.ratings[6] == 1500
        mean = (1600 + 4 * initial) / 5
        assert model.predict(row()) == pytest.approx(
            1 / (1 + 10 ** ((1500 - mean) / 400))
        )


def test_lineup_fallback_and_unusual_sizes():
    model = EloModel(
        unit="player", lineups={1: ((1, 2), (3,)), 3: ((4, 5, 6, 7, 8, 9), ())}
    )
    model.predict(row())
    # A prediction alone must not save the current map's lineup as history.
    assert model.last_lineups == {}
    model.update(row())
    assert model._units(row(game_id=2), 1) == (1, 2)
    assert model._units(row(game_id=2, team2_id=99), 2) == (("team", 99),)
    model.update(row(game_id=2))
    model.update(row(game_id=3))
    assert model._units(row(game_id=4), 1) == (4, 5, 6, 7, 8, 9)
    assert model.last_lineups[20] == (3,)
    assert model.ratings[4] == model.ratings[9]


def test_region_table_and_unknowns():
    assert tuple(REGION_CODES) == ("EU", "CIS", "NA", "SA", "AS", "OCE", "AF")
    assert [macro_region(c) for c in REGION_CODES] == list(REGION_CODES)
    for code in ("us", "NA ", "unknown", None):
        assert macro_region(code) is None


def test_home_majority_earlier_maps_ties_and_international():
    model = EloModel(region_k=16)
    first = row(region="NA")
    assert model.predict(first) == 0.5
    assert model.homes == {}
    model.update(first)
    assert model.homes == {10: "NA", 20: "NA"}
    model.update(row(region="EU"))  # tie retains previous
    assert model.homes[10] == "NA"
    model.update(row(region="EU", international=1))
    model.update(row(region="un"))
    assert model.home_counts[10] == {"NA": 1, "EU": 1}
    model.predict(row(region="EU"))
    assert model.homes[10] == "NA"  # no current-map leakage
    model.update(row(region="EU"))
    assert model.homes[10] == "EU"
    assert model.offsets == {}  # same homes throughout


def test_region_offsets_only_cross_region_and_zero_sum():
    model = EloModel(region_k=16)
    model.update(row(team1_id=1, team2_id=2, region="NA"))
    model.update(row(team1_id=3, team2_id=4, region="AS"))
    cross = row(team1_id=1, team2_id=3, region="CIS")
    expected = model.predict(cross)
    model.update(cross)
    assert model.offsets["NA"] == pytest.approx(16 * (1 - expected))
    assert sum(model.offsets.values()) == pytest.approx(0)
    assert "CIS" not in model.offsets  # current host isn't either earlier home
    offsets = model.offsets.copy()
    model.update(row(team1_id=1, team2_id=99, region="un"))
    assert model.offsets == offsets
    model.update(row(team1_id=3, team2_id=4, region="un"))
    assert model.offsets == offsets
    no_offset = EloModel(region_k=0)
    no_offset.ratings = model.ratings.copy()
    # Set known unequal offsets to isolate their contribution to prediction.
    model.homes[1], model.homes[3] = "NA", "AS"
    model.offsets = {"NA": 10, "AS": -10}
    assert model.predict(cross) > no_offset.predict(cross)


def test_registry_grids_and_v1_regression():
    assert len(MODELS) == len(PARAM_GRIDS) == 12
    assert "team_binary" not in MODELS
    for name in MODELS:
        if name == "coin":
            continue
        grid = PARAM_GRIDS[name]
        if "_glicko" in name:
            continue
        assert grid["k"] == (16, 24, 32, 48, 64, 96)
        assert ("region_k" in grid) == name.endswith("_region")
        assert ("new_player" in grid) == name.startswith("player")
        assert ("c" in grid) == ("margin" in name)
        assert "tau" not in grid
        model = MODELS[name](**{p: values[0] for p, values in grid.items()})
        assert model.predict(row()) == 0.5
    old = TeamElo(EloConfig(k=48))
    new = MODELS["team_elo"](k=48)
    probabilities = []
    for a, b, won in ((10, 20, 1), (10, 20, 0), (20, 30, 1), (30, 10, 0), (10, 20, 1)):
        game = row(team1_id=a, team2_id=b, won=won)
        probabilities.append(new.predict(game))
        assert new.predict(game) == old.expected(a, b)
        new.update(game)
        old.update(a, b, won)
        assert new.ratings == old.ratings
    assert probabilities == pytest.approx(
        [
            0.5,
            0.5686413919,
            0.5047414372393056,
            0.4705644068707748,
            0.48881289673471856,
        ],
        abs=1e-9,
    )


@pytest.mark.parametrize("credit", ["binary", "margin"])
def test_rd_first_move_and_update_expectation(credit):
    from math import log

    lineups = {1: ((1, 2), (3, 4))}
    base = EloModel(unit="player", credit=credit, k=12, lineups=lineups)
    model = EloModel(unit="player", credit=credit, k=12, lineups=lineups, rd=True)
    # Unequal strengths exercise the information term away from 50%.
    for candidate in (base, model):
        candidate.ratings.update({1: 1510, 2: 1510, 3: 1490, 4: 1490})
    expected = base._state(row())[-1]
    before = model.ratings.copy()
    base.update(row())
    model.update(row())
    for player in (1, 2, 3, 4):
        assert model.ratings[player] - before[player] == pytest.approx(
            4 * (base.ratings[player] - before[player])
        )
    information = 0.125 * (log(10) / 400) ** 2 * expected * (1 - expected)
    assert model.rd_variance[1] == pytest.approx(1 / (1 / 280**2 + information))
    assert model.rd_variance[1] < 280**2


def test_rd_growth_cap_floor_and_prediction_has_no_leakage():
    from math import log

    model = EloModel(unit="player", rd=True, k=12, lineups={1: ((1,), (2,))})
    model.update(row())
    first_variance = model.rd_variance.copy()
    first_seen = model.last_seen.copy()
    # Repeated and future predictions must not age/shrink RD or save dates.
    future = row(start_utc="2026-01-04T00:00:00Z")
    model.predict(future)
    model.predict(future)
    assert model.rd_variance == first_variance
    assert model.last_seen == first_seen
    model.ratings = {1: 1500, 2: 1500}
    aged = first_variance[1] + 10**2 * 2.5
    model.update(future)
    assert model.ratings[1] - 1500 == pytest.approx(6 * aged / 140**2)
    information = 0.125 * (log(10) / 400) ** 2 * 0.25
    assert model.rd_variance[1] == pytest.approx(1 / (1 / aged + information))
    assert model.last_seen[1].isoformat() == "2026-01-04T00:00:00+00:00"
    model.ratings = {1: 1500, 2: 1500}
    model.update(row(start_utc="2030-01-01T00:00:00Z"))
    assert model.ratings[1] == pytest.approx(1524)  # Growth capped at new RD.
    for _ in range(1000):
        model.ratings = {1: 1500, 2: 1500}
        model.update(row(start_utc="2030-01-01T00:00:00Z"))
    assert model.rd_variance == {1: 140**2, 2: 140**2}


@pytest.mark.parametrize("credit", ["binary", "margin"])
@pytest.mark.parametrize("region_k", [0, 4])
def test_rd_disabled_preserves_existing_player_variants(credit, region_k):
    options = {
        "unit": "player",
        "credit": credit,
        "region_k": region_k,
        "lineups": {1: ((1, 2), (3, 4)), 2: ((1, 5), (6, 7))},
    }
    original = EloModel(**options)
    disabled = EloModel(**options, rd=False, rd_new=350, rd_info=0.25)
    games = [
        row(region="NA"),
        row(game_id=2, team1_id=30, team2_id=40, region="AS"),
        row(team2_id=30, international=1, region="CIS"),
        row(game_id=2, score1=4, score2=13, won=0),
    ]
    for game in games:
        assert original.predict(game) == disabled.predict(game)
        original.update(game)
        disabled.update(game)
        assert original.ratings == disabled.ratings
        assert original.offsets == disabled.offsets
    assert disabled.rd_variance == disabled.last_seen == {}


def test_team_ignores_rd_and_player_validates_parameters():
    original = EloModel()
    ignored = EloModel(rd=True, rd_new=-1, rd_info=-1)
    for game in [row(), row(won=0), row(team2_id=30)]:
        assert original.predict(game) == ignored.predict(game)
        original.update(game)
        ignored.update(game)
        assert original.ratings == ignored.ratings
    assert ignored.rd_variance == ignored.last_seen == {}
    for invalid in (
        {"rd_floor": 0},
        {"rd_new": 100},
        {"rd_info": 0},
        {"rd_growth": -1},
        {"rd_info": float("inf")},
        {"rd_new": float("nan")},
    ):
        with pytest.raises(ValueError, match="RD"):
            EloModel(unit="player", rd=True, **invalid)


def test_glicko_registry_and_exact_grids():
    for region in (False, True):
        name = "player_region_glicko" if region else "player_glicko"
        grid = {
            "k": (16, 24, 32, 48, 64),
            "rd_new": (160, 200, 240, 280, 350, 450),
            "rd_info": (0.03125, 0.0625, 0.125, 0.25, 0.5),
            "new_player": ("fixed", "teammates"),
        }
        if region:
            grid["region_k"] = (2, 4)
        assert PARAM_GRIDS[name] == grid
        model = MODELS[name]()
        assert model.unit == "player" and model.credit == "binary" and model.rd
        assert bool(model.region_k) == region
        assert model.rd_floor == 140 and model.rd_growth == 10
        assert model.predict(row()) == 0.5
        assert model.rd_variance == model.last_seen == {}


@pytest.mark.parametrize("maps", [0, 1, 10, 29, 30, 40])
def test_rookie_log_discount_and_update_only_counts(maps):
    from math import log1p

    model = EloModel(
        unit="player", rookie_penalty=100, rookie_maps=30, lineups={1: ((1,), (2,))}
    )
    for _ in range(maps):
        model.update(row())
    model.ratings = {1: 1600, 2: 1500}
    before = model.ratings.copy()
    discount = 100 * (1 - log1p(maps) / log1p(30)) if maps < 30 else 0
    assert model._strength((1,)) == pytest.approx(1600 - discount)
    for _ in range(2):
        model.predict(row())
    assert model.ratings == before
    assert model.map_counts == ({1: maps, 2: maps} if maps else {})
    model.update(row())
    assert model.map_counts == {1: maps + 1, 2: maps + 1}


@pytest.mark.parametrize("credit", ["binary"])
def test_adjusted_strengths_drive_update_expectation(credit):
    model = EloModel(
        unit="player",
        credit=credit,
        rookie_penalty=100,
        move_up_penalty=80,
        lineups={1: ((1,), (2,))},
    )
    model.ratings = {1: 1600, 2: 1500}
    model.map_counts = {1: 30}
    model.tier_homes = {1: 2, 2: 3}
    model.tier_counts = {1: {2: 5}, 2: {3: 5}}
    game = row(section="tier1")
    # Side 1 is promoted (1600 - 80); side 2 is a rookie (1500 - 100).
    expected = 1 / (1 + 10 ** ((1400 - 1520) / 400))
    assert model._state(game)[-1] == pytest.approx(expected)
    before = model.ratings.copy()
    model.predict(game)
    assert model.ratings == before
    model.update(game)
    assert model.ratings[1] == pytest.approx(1600 + 32 * (model.score(game) - expected))
    assert model.ratings[2] == pytest.approx(1500 - 32 * (model.score(game) - expected))


@pytest.mark.parametrize(
    "home,target,adjustment", [("tier2", "tier1", -100), ("tier1", "tier2", 50)]
)
def test_tier_moves_fade_with_prior_rank_count(home, target, adjustment):
    model = EloModel(
        unit="player",
        move_up_penalty=100,
        move_down_bonus=50,
        move_maps=4,
        lineups={1: ((1,), (2,))},
    )
    for _ in range(10):
        model.update(row(section=home))
    for played in range(6):
        model.ratings = {1: 1500, 2: 1500}
        counts = {p: c.copy() for p, c in model.tier_counts.items()}
        homes = model.tier_homes.copy()
        game = row(section=target)
        model.predict(game)
        model.predict(game)
        rank = 3 if target == "tier1" else 2
        assert model._strength((1,), rank) == 1500 + adjustment * max(0, 1 - played / 4)
        assert model.ratings == {1: 1500, 2: 1500}
        assert model.tier_counts == counts and model.tier_homes == homes
        model.update(game)


def test_tier_home_majority_ties_and_unranked_maps():
    model = EloModel(
        unit="player",
        move_up_penalty=100,
        move_down_bonus=50,
        lineups={1: ((1,), (2,))},
    )
    model.predict(row(section="tier1"))
    assert model.tier_homes == model.tier_counts == {}
    for section, home in [
        ("tier3", 1),
        ("tier3", 1),
        ("tier2", 1),
        ("tier1", 1),
        ("tier1", 1),
        ("tier1", 3),
    ]:
        model.update(row(section=section))
        assert model.tier_homes == {1: home, 2: home}
    counts = {p: c.copy() for p, c in model.tier_counts.items()}
    for section in ("unknown", None):
        model.ratings = {1: 1600, 2: 1500}
        assert model.predict(row(section=section)) == 1 / (1 + 10 ** (-100 / 400))
        model.update(row(section=section))
        assert model.tier_counts == counts
        assert model.tier_homes == {1: 3, 2: 3}


@pytest.mark.parametrize("variant", ["rookie", "weights", "rookie_weights"])
def test_ladder_registry_exact_grids(variant):
    name = f"player_glicko_{variant}"
    grid = {}
    if "rookie" in variant:
        grid.update(
            rookie_penalty=(300, 400, 600, 800, 1200),
            rookie_maps=(200, 400, 800, 1600),
        )
    if "weights" in variant:
        grid.update(online_k=(0.5, 0.75, 1.0), tier3_k=(0.5, 0.75, 1.0))
    assert PARAM_GRIDS[name] == grid
    model = MODELS[name](**{p: values[0] for p, values in grid.items()})
    assert model.unit == "player" and model.credit == "binary" and model.rd
    assert model.predict(row()) == 0.5


def test_teams_ignore_player_adjustments():
    original = EloModel()
    adjusted = EloModel(rookie_penalty=200, move_up_penalty=100, move_down_bonus=50)
    for game in (row(section="tier2"), row(section="tier1"), row(section="unknown")):
        assert original.predict(game) == adjusted.predict(game)
        original.update(game)
        adjusted.update(game)
        assert original.ratings == adjusted.ratings
    assert adjusted.map_counts == adjusted.tier_counts == adjusted.tier_homes == {}


@pytest.mark.parametrize(
    "options",
    [
        {"rookie_penalty": -1},
        {"rookie_maps": 0},
        {"move_up_penalty": -1},
        {"move_down_bonus": -1},
        {"move_maps": 0},
        {"rookie_maps": float("nan")},
        {"move_up_penalty": float("inf")},
    ],
)
def test_invalid_player_adjustment_parameters(options):
    with pytest.raises(ValueError, match="rookie/move"):
        EloModel(unit="player", **options)


@pytest.mark.parametrize("rd", [False, True])
def test_k_multipliers_one_exactly_preserve_replay(rd):
    options = {"unit": "player", "credit": "binary", "rd": rd}
    legacy = EloModel(**options)
    default = EloModel(**options)
    explicit = EloModel(**options, online_k=1.0, tier3_k=1.0)
    for i in range(12):
        values = {
            "game_id": i + 1,
            "won": i % 2,
            "score1": 13 if i % 2 else 7,
            "score2": 7 if i % 2 else 13,
        }
        old_row = row(**values)
        game = row(**values, online=i % 2, section=("tier1", "tier3")[i % 2])
        assert (
            legacy.predict(old_row) == default.predict(game) == explicit.predict(game)
        )
        legacy.update(old_row)
        for model in (default, explicit):
            model.update(game)
            assert model.ratings == legacy.ratings
            assert model.rd_variance == legacy.rd_variance


@pytest.mark.parametrize(
    "online,tier,ratio",
    [(0, "tier1", 1), (1, "tier1", 0.5), (0, "tier3", 0.75), (1, "tier3", 0.375)],
)
def test_k_multipliers_scale_two_map_replay(online, tier, ratio):
    import pandas as pd

    from promdota.ratings.replay import replay

    # Disjoint teams give both maps the same pre-update expectation.
    maps = pd.DataFrame(
        [
            vars(row(game_id=1, match_id=1, order=1, online=0, section="tier1")),
            vars(
                row(
                    game_id=2,
                    match_id=2,
                    order=1,
                    team1_id=30,
                    team2_id=40,
                    online=online,
                    section=tier,
                )
            ),
        ]
    )
    model = EloModel(online_k=0.5, tier3_k=0.75)
    replay(maps, model)
    assert model.ratings[30] - 1500 == ratio * (model.ratings[10] - 1500)
    assert 1500 - model.ratings[40] == ratio * (1500 - model.ratings[20])


@pytest.mark.parametrize("parameter", ["online_k", "tier3_k"])
@pytest.mark.parametrize("value", [0, -0.1, 2.01, float("inf"), float("nan")])
def test_invalid_k_multipliers(parameter, value):
    with pytest.raises(ValueError, match="online_k and tier3_k"):
        EloModel(**{parameter: value})


def reversion_model(rd, start="2025-01-01T00:00:00Z", **options):
    model = EloModel(unit="player", rd=rd, lineups={1: ((1,), (2,))}, **options)
    model.update(row(start_utc=start))
    model.ratings = {1: 1700, 2: 1500}
    return model


@pytest.mark.parametrize("rd", [False, True])
@pytest.mark.parametrize(
    "date,factor",
    [
        ("2025-12-31T23:59:59Z", 1),
        ("2026-01-01T00:00:00Z", 0.5),
        ("2027-01-01T00:00:00Z", 0.25),
    ],
)
def test_season_reversion_boundaries(rd, date, factor):
    model = reversion_model(rd, season_revert=0.5)
    expected = 1 / (1 + 10 ** (-200 * factor / 400))
    assert model.predict(row(start_utc=date)) == expected


@pytest.mark.parametrize("rd", [False, True])
@pytest.mark.parametrize(
    "date,factor",
    [
        ("2025-09-30T23:59:59Z", 1),
        ("2025-10-01T00:00:00Z", 0.5),
        # The date must be compared in UTC, including offset datetime inputs.
        (datetime.fromisoformat("2025-09-30T20:00:00-04:00"), 0.5),
    ],
)
def test_october_season_reversion(rd, date, factor):
    model = reversion_model(rd, season_revert=0.5, season_month=10)
    assert model.predict(row(start_utc=date)) == 1 / (1 + 10 ** (-200 * factor / 400))


@pytest.mark.parametrize("rd", [False, True])
@pytest.mark.parametrize(
    "options,date,factor",
    [
        ({"inactive_half_life": 365}, "2026-01-01T00:00:00Z", 0.5),
        (
            {"inactive_half_life": 365, "season_revert": 0.5},
            "2026-01-01T00:00:00Z",
            0.25,
        ),
        ({"season_revert": 1}, "2026-01-01T00:00:00Z", 0),
        ({"season_revert": 1}, "2025-01-01T00:00:00Z", 1),
        ({"season_revert": 0.5, "inactive_half_life": 365}, "2024-01-01T00:00:00Z", 1),
    ],
)
def test_inactivity_and_combined_reversion(rd, options, date, factor):
    model = reversion_model(rd, **options)
    assert model.predict(row(start_utc=date)) == 1 / (1 + 10 ** (-200 * factor / 400))


@pytest.mark.parametrize("rd", [False, True])
@pytest.mark.parametrize("credit", ["binary"])
def test_reversion_prediction_and_update_agree_without_prediction_history(rd, credit):
    model = reversion_model(
        rd,
        season_revert=0.5,
        inactive_half_life=365,
        credit=credit,
        rookie_penalty=200,
        move_up_penalty=100,
    )
    model.tier_homes = {1: 2, 2: 3}
    game = row(
        start_utc=datetime.fromisoformat("2026-01-01T00:00:00Z"), section="tier1"
    )
    before = deepcopy({k: v for k, v in vars(model).items() if isinstance(v, dict)})
    expected = model._state(game)[-1]
    prediction = model.predict(game)
    assert prediction == model.predict(game)
    assert prediction == pytest.approx(expected)
    assert {k: v for k, v in vars(model).items() if isinstance(v, dict)} == before
    # Reversion happens before rookie/move adjustments: effective difference is 50-100.
    assert expected == 1 / (1 + 10 ** (50 / 400))
    weight = 4 if rd else 1  # The long gap grows RD back to its cap.
    model.update(game)
    delta = model.k * (model.score(game) - expected) * weight
    assert model.ratings[1] == pytest.approx(1550 + delta)
    assert model.ratings[2] == pytest.approx(1500 - delta)
    assert model.last_played == {1: game.start_utc, 2: game.start_utc}
    # A second map at the same start must not revert again.
    expected = model._state(game)[-1]
    previous = model.ratings.copy()
    weight = model.rd_variance[1] / model.rd_floor**2 if rd else 1
    model.update(game)
    assert model.ratings[1] == pytest.approx(
        previous[1] + model.k * (model.score(game) - expected) * weight
    )


@pytest.mark.parametrize("rd", [False, True])
def test_reversion_teammates_initialization_and_new_players(rd):
    model = reversion_model(rd, season_revert=0.5, new_player="teammates")
    model.lineups[2] = ((1, 3), (2, 4))
    game = row(game_id=2, start_utc="2026-01-01T00:00:00Z")
    before_dates = model.last_played.copy()
    prediction = model.predict(game)
    assert model.ratings == {1: 1700, 2: 1500, 3: 1600, 4: 1500}
    assert model.last_played == before_dates
    assert prediction == 1 / (1 + 10 ** (-100 / 400))
    # Even far-future predictions do not revert players with no update history.
    assert model._rating(3, datetime.fromisoformat("2030-01-01T00:00:00Z")) == 1600
    model.update(game)
    weight = 4 if rd else 1
    assert (
        model.ratings[1]
        == model.ratings[3]
        == pytest.approx(1600 + 32 * (1 - prediction) * weight)
    )


def test_team_reversion_options_have_no_effect():
    model = EloModel(season_revert=1, inactive_half_life=1)
    baseline = EloModel()
    for date in ("2025-01-01T00:00:00Z", "2026-01-01T00:00:00Z"):
        game = row(start_utc=date)
        assert model.predict(game) == baseline.predict(game)
        model.update(game)
        baseline.update(game)
        assert model.ratings == baseline.ratings
    assert model.last_played == {}


@pytest.mark.parametrize(
    "options",
    [
        {"season_revert": -0.1},
        {"season_revert": 1.1},
        {"season_revert": float("nan")},
        {"season_revert": float("inf")},
        {"season_month": 0},
        {"season_month": 13},
        {"season_month": 1.5},
        {"season_month": 1.0},
        {"season_month": True},
        {"season_month": float("nan")},
        {"season_month": float("inf")},
        {"inactive_half_life": -1},
        {"inactive_half_life": float("nan")},
        {"inactive_half_life": float("inf")},
    ],
)
def test_invalid_reversion_parameters(options):
    with pytest.raises(ValueError, match="reversion"):
        EloModel(unit="player", **options)


def tier_sums_match(model):
    for section, total in model.tier_sum.items():
        members = [p for p, s in model.tier_of.items() if s == section]
        assert model.tier_count[section] == len(members)
        assert total == pytest.approx(sum(model.ratings[p] for p in members))


@pytest.mark.parametrize("rd", [False, True])
def test_tier_reversion_pulls_toward_latest_tier_mean(rd):
    lineups = {1: ((1,), (2,)), 2: ((3,), (4,)), 3: ((1,), (3,)), 4: ((3,), (5,))}
    model = EloModel(
        unit="player", rd=rd, lineups=lineups, season_revert=0.5, revert_target="tier"
    )
    model.update(row(game_id=1, start_utc="2025-03-01T00:00:00Z", section="tier1"))
    model.update(row(game_id=2, start_utc="2025-03-02T00:00:00Z", section="tier3"))
    # Unknown-section games neither set nor move a player's tier.
    model.update(row(game_id=4, start_utc="2025-03-03T00:00:00Z", section="unknown"))
    assert model.tier_of == {1: "tier1", 2: "tier1", 3: "tier3", 4: "tier3"}
    tier_sums_match(model)
    tier1 = (model.ratings[1] + model.ratings[2]) / 2
    tier3 = (model.ratings[3] + model.ratings[4]) / 2
    game = row(game_id=3, start_utc="2026-01-05T00:00:00Z", section="tier1")
    r1 = tier1 + 0.5 * (model.ratings[1] - tier1)
    r3 = tier3 + 0.5 * (model.ratings[3] - tier3)
    expected = 1 / (1 + 10 ** (-(r1 - r3) / 400))
    assert model._state(game)[-1] == pytest.approx(expected)
    model.update(game)
    # Player 3 moves from tier3 to tier1; sums follow every rating change and move.
    assert model.tier_of[3] == "tier1" and model.tier_count["tier3"] == 1
    tier_sums_match(model)


def test_tier_reversion_prediction_matches_update_expectation():
    lineups = {1: ((1,), (2,)), 2: ((1,), (2,))}
    model = EloModel(
        unit="player", lineups=lineups, season_revert=0.35, revert_target="tier"
    )
    model.update(row(game_id=1, start_utc="2025-03-01T00:00:00Z", section="tier2"))
    game = row(game_id=2, start_utc="2026-02-01T00:00:00Z", section="tier2")
    tier2 = (model.ratings[1] + model.ratings[2]) / 2
    reverted = tier2 + 0.65 * (model.ratings[1] - tier2)
    expected = model._state(game)[-1]
    model.update(game)
    # The update starts from the reverted rating and uses the predicted chance.
    assert model.ratings[1] == pytest.approx(reverted + model.k * (1 - expected))
    tier_sums_match(model)


def test_init_target_keeps_no_tier_state():
    model = reversion_model(False, season_revert=0.5)
    model.update(row(start_utc="2026-01-02T00:00:00Z", section="tier1"))
    assert model.tier_of == {} and model.tier_sum == {}
    with pytest.raises(ValueError):
        EloModel(revert_target="league")


@pytest.mark.parametrize("rd,weight", [(False, 1), (True, 4)])
def test_performance_zero_sum_causal_and_missing(rd, weight):
    options = {"unit": "player", "rd": rd, "lineups": {1: ((1, 2, 5), (3, 4, 6))}}
    baseline = EloModel(**options)
    model = EloModel(
        **options,
        perf_k=20,
        performance={1: {1: (10, 4), 2: (20, 0), 3: (30, 2), 4: (40, None)}},
    )
    model.predict(row())
    assert model.hero_mean == {} and model.global_mean is None
    baseline.update(row())
    model.update(row())
    assert model.ratings[1] - baseline.ratings[1] == pytest.approx(40 * weight)
    assert model.ratings[2] - baseline.ratings[2] == pytest.approx(-40 * weight)
    for player in (3, 4, 5, 6):
        assert model.ratings[player] == baseline.ratings[player]
    assert model.hero_count == {10: 1, 20: 1, 30: 1}
    assert model.hero_mean == {10: 4, 20: 0, 30: 2}
    assert model.global_mean == pytest.approx((4 * 0.99) * 0.99 + 0.01 * 2)


@pytest.mark.parametrize("count,bonus", [(19, 0), (20, -20)])
def test_hero_ema_threshold_and_update_after_game(count, bonus):
    options = {"unit": "player", "lineups": {1: ((1, 2), (3,))}}
    model = EloModel(**options, perf_k=20, performance={1: {1: (10, 1), 2: (20, 1)}})
    model.hero_count = {10: count}
    model.hero_mean = {10: 3}
    model.global_mean = 1
    baseline = EloModel(**options)
    baseline.update(row())
    model.update(row())
    assert model.ratings[1] - baseline.ratings[1] == pytest.approx(bonus)
    assert model.ratings[2] - baseline.ratings[2] == pytest.approx(-bonus)
    assert model.hero_mean[10] == pytest.approx(2.98)
    assert model.hero_count[10] == count + 1


@pytest.mark.parametrize(
    "options",
    [
        {"perf_stat": "rating"},
        {"perf_k": -1},
        {"perf_k": float("nan")},
        {"perf_alpha": 0},
        {"perf_min_count": True},
    ],
)
def test_invalid_performance_options(options):
    with pytest.raises(ValueError, match="performance"):
        EloModel(**options)


def test_missing_hero_uses_global_without_hero_bucket():
    model = EloModel(
        unit="player",
        perf_k=20,
        lineups={1: ((1, 2), (3,))},
        performance={1: {1: (None, 2), 2: (None, 0)}},
    )
    for _ in range(21):
        model.update(row())
    assert model.hero_mean == model.hero_count == {}
    assert model.global_mean is not None


@pytest.mark.parametrize("rd", [False, True])
def test_disabled_new_parameters_preserve_ratings(rd):
    options = {"unit": "player", "rd": rd, "lineups": {1: ((1, 2), (3, 4))}}
    original = EloModel(**options)
    disabled = EloModel(
        **options,
        season_revert=0,
        inactive_half_life=0,
        perf_k=0,
        performance={1: {1: (1, 99), 2: (2, -99)}},
    )
    for year in (2025, 2026, 2027):
        game = row(start_utc=f"{year}-10-01T00:00:00Z")
        assert original.predict(game) == disabled.predict(game)
        original.update(game)
        disabled.update(game)
        assert original.ratings == disabled.ratings
        assert original.rd_variance == disabled.rd_variance
    assert disabled.last_played == disabled.hero_mean == disabled.hero_count == {}
