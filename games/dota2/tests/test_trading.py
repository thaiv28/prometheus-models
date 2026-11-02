"""Offline execution contract and causal frozen-coefficient checks."""

import hashlib
import json
from collections import Counter
from datetime import UTC, datetime

import numpy as np
import pandas as pd
import pytest

from promdota import blend
from promdota.trading import build_blend_artifact, candidates

NOW = datetime(2026, 10, 29, 12, tzinfo=UTC)


def test_artifact_causal_subsets_and_minimum():
    rng = np.random.default_rng(42)
    rows = pd.DataFrame(
        {
            "kind": ["series"] * 800,
            "p": rng.uniform(0.1, 0.9, 800),
            "market_p": rng.uniform(0.1, 0.9, 800),
            "won": rng.integers(0, 2, 800),
            "start_utc": pd.date_range("2025-12-01", periods=800, freq="12h", tz="UTC"),
        }
    )
    # Map rows and unknown outcomes must not affect the fits.
    rows.loc[10:20, "kind"] = "map"
    rows.loc[80, "won"] = np.nan
    artifact = build_blend_artifact(rows, "dota2", "KXDOTA2GAME", NOW)
    assert artifact["version"] == "game-blend-v1" and artifact["clip"] == 0.01
    snapshots = artifact["snapshots"]
    assert snapshots and snapshots[-1]["available_from"] == "2026-11-01T00:00:00+00:00"
    boundaries = [s["available_from"] for s in snapshots]
    assert boundaries == sorted(set(boundaries))
    for snapshot in snapshots:
        boundary = pd.Timestamp(snapshot["available_from"])
        subset = rows[
            (rows.kind == "series")
            & rows.won.notna()
            & (rows.start_utc >= pd.Timestamp("2025-11-01", tz="UTC"))
            & (rows.start_utc < boundary)
        ]
        a, b, n = blend.fit(subset.p, subset.market_p, subset.won)
        assert snapshot["training_series"] == n >= 300
        assert snapshot["market_slope"] == a and snapshot["gap_slope"] == b
        assert snapshot["trained_through"] == subset.start_utc.max().isoformat()
        assert snapshot["trained_through"] < snapshot["available_from"]
    assert snapshots[0]["available_from"] == "2026-06-01T00:00:00+00:00"
    assert (
        build_blend_artifact(rows.iloc[:100], "dota2", "KXDOTA2GAME", NOW)["snapshots"]
        == []
    )
    # No blanket holdout exclusion: December fits may learn November outcomes.
    later = build_blend_artifact(
        rows, "dota2", "KXDOTA2GAME", datetime(2026, 11, 29, tzinfo=UTC)
    )
    assert later["snapshots"][-1]["trained_through"].startswith("2026-11-")


@pytest.fixture
def inputs():
    row = {
        "match_id": "our-match",
        "status": "upcoming",
        "start": "2026-10-29T18:00Z",
        "best_of": 3,
        "section": "INTL",
        "name1": "hotu",
        "name2": "gl",
        "p_game": 0.6,
        "p_series": 0.712345678,
    }
    pair = [
        {
            "event_ticker": "KXDOTA2GAME-TEST",
            "status": "active",
            "yes_sub_title": side,
            "rules_primary": f"If {side} wins the Tesla Cup 2026: GamerLegion vs. HOTU Dota 2 match originally scheduled for Oct 29, 2026 at 2:00 PM EDT, then Yes.",
        }
        for side in ("HOTU", "GamerLegion")
    ]
    return row, {row["match_id"]: pair}


def test_candidate_names_orientation_start_and_validation_shape(inputs):
    row, linked = inputs
    doc = candidates([row], linked, NOW, data_through="2026-10-28")
    assert doc["generated"] == "2026-10-29T12:00:00Z"
    saved = doc["matches"][0]["execution_candidate"]
    assert saved["teams"] == ["GamerLegion", "HOTU"]
    assert saved["raw"] == {"HOTU": 0.712346, "GamerLegion": 0.287654}
    assert saved["start"] == "2026-10-29T18:00Z"
    identity = json.dumps(
        ["dota2", saved["teams"], saved["event_ticker"]],
        separators=(",", ":"),
        ensure_ascii=False,
    )
    assert saved["fixture_id"] == hashlib.sha256(identity.encode()).hexdigest()
    assert saved["provenance"]["p_series"] == row["p_series"]
    assert saved["provenance"]["names"] == ["hotu", "gl"]
    assert saved["provenance"]["data_through"] == "2026-10-28"
    # Mirror saved_candidates' input validation without importing its live runtime.
    assert saved["kind"] == "candidate-v1" and saved["schema_version"] == 1
    assert saved["group"] == "dota2-series"
    assert isinstance(saved["teams"], list) and len(set(saved["teams"])) == 2
    assert all(isinstance(t, str) and t for t in saved["teams"])
    assert all(
        isinstance(saved[k], str) and saved[k] for k in ("fixture_id", "event_ticker")
    )
    assert isinstance(saved["international"], bool) and saved["international"]
    assert isinstance(saved["team_homes"], dict) and isinstance(
        saved["provenance"], dict
    )
    assert all(isinstance(v, (int, float)) and 0 < v < 1 for v in saved["raw"].values())
    assert saved["game"] == "dota2" and saved["series_ticker"] == "KXDOTA2GAME"


@pytest.mark.parametrize(
    "change",
    [
        "subtitle",
        "teams",
        "same-side",
        "rules",
        "closed",
        "missing",
        "time",
        "started",
        "unknown",
        "live",
        "kalshi-started",
    ],
)
def test_rejected_candidates_counted(inputs, change):
    row, linked = inputs
    pair = linked[row["match_id"]]
    if change == "subtitle":
        pair[0]["yes_sub_title"] = "Other"
    elif change == "teams":
        pair[1]["rules_primary"] = pair[1]["rules_primary"].replace(
            "GamerLegion vs.", "Other vs."
        )
    elif change == "same-side":
        pair[1] = pair[0].copy()
    elif change == "rules":
        pair[0]["rules_primary"] = "not rules"
    elif change == "closed":
        pair[0]["status"] = "closed"
    elif change == "missing":
        pair.pop()
    elif change == "time":
        row["start"] = "2026-10-30T13:00Z"
    elif change == "started":
        row["start"] = "2026-10-29T12:00Z"
    elif change == "unknown":
        row["best_of"] = None
    elif change == "live":
        row["status"] = "live"
    elif change == "kalshi-started":
        for market in pair:
            market["rules_primary"] = market["rules_primary"].replace(
                "2:00 PM", "8:00 AM"
            )
    skipped = Counter()
    assert candidates([row], linked, NOW, skipped=skipped)["matches"] == []
    assert skipped["candidates"] == 1


def test_no_current_markets(inputs):
    row, _ = inputs
    assert candidates([row], {}, NOW)["matches"] == []


def test_date_only_rules_use_new_york_noon(inputs):
    row, linked = inputs
    for market in linked[row["match_id"]]:
        market["rules_primary"] = market["rules_primary"].replace(" at 2:00 PM EDT", "")
    candidate = candidates([row], linked, NOW)["matches"][0]["execution_candidate"]
    assert candidate["start"] == "2026-10-29T16:00Z"


@pytest.mark.parametrize("field", ["event_ticker", "series", "series_ticker"])
def test_game_market_candidates_never_emitted(inputs, field):
    row, linked = inputs
    for market in linked[row["match_id"]]:
        market[field] = "KXDOTA2MAP-TEST-1" if field == "event_ticker" else "KXDOTA2MAP"
    assert candidates([row], linked, NOW)["matches"] == []


def test_adopted_replay_matches_benchmark_form_and_temperature():
    import runpy
    import sqlite3
    from pathlib import Path

    from promdota.benchmark import with_series_temperature
    from promdota.ratings.layers import LAYERS
    from promdota.ratings.models import ADOPTED, ADOPTED_LAYER, MODELS, PINNED
    from promdota.ratings.replay import (
        load_lineups,
        load_maps,
        load_performance,
        replay,
    )
    from promdota.trading import adopted_replay

    benchmark = runpy.run_path(
        str(Path(__file__).parents[1] / "scripts/evaluate_elo.py")
    )
    fit_series_temperature = benchmark["fit_series_temperature"]
    scored_rows = benchmark["scored_rows"]

    with sqlite3.connect(":memory:") as conn:
        conn.executescript(Path("scripts/001_create_tables.sql").read_text())
        conn.execute(
            "INSERT INTO events (event_id,title,section,international,excluded) VALUES (1,'Test','tier1',1,0)"
        )
        conn.executemany(
            "INSERT INTO teams VALUES (?,?,?)", [(1, "a", "A"), (2, "b", "B")]
        )
        conn.executemany(
            "INSERT INTO players VALUES (?,?,?)",
            [(i, str(i), str(i)) for i in range(1, 11)],
        )
        for game in range(1, 44):
            start = (
                f"2024-01-{(game - 1) // 2 + 1:02d}T{(game % 2) * 12:02d}:00:00Z"
                if game < 43
                else "2025-11-02T00:00:00Z"
            )
            winner = 1 if game % 3 else 2
            conn.execute(
                "INSERT INTO matches VALUES (?,1,'Test',?,?,1,3,1,2,2,0,?)",
                (game, game, start, winner),
            )
            conn.execute(
                "INSERT INTO games VALUES (?,?,1,NULL,NULL,?,1800,NULL)",
                (game, game, winner),
            )
            conn.executemany(
                "INSERT INTO player_games (game_id,player_id,team,kills,deaths,assists) VALUES (?,?,?,?,?,?)",
                [
                    (game, i, 1 if i <= 5 else 2, (game % 3) + i, 1, 3)
                    for i in range(1, 11)
                ],
            )
        lineups, performance = load_lineups(conn), load_performance(conn)
        source = replay(
            load_maps(conn),
            MODELS[ADOPTED](
                lineups=lineups, performance=performance, **PINNED[ADOPTED]
            ),
        )
        layer = LAYERS[ADOPTED_LAYER](
            context={"conn": conn, "lineups": lineups, "performance": performance}
        )
        layer.fit(scored_rows(source, "2023-01-01", "2025-11-01"))
        adjusted = source.copy()
        adjusted["p"] = layer.apply(adjusted)
        temperatures = fit_series_temperature(
            scored_rows(adjusted, "2023-01-01", "2025-11-01")
        )
        _, actual, fitted, actual_temperatures = adopted_replay(conn)
        pd.testing.assert_frame_equal(
            actual, with_series_temperature(adjusted, temperatures)
        )
        assert fitted.half_life == layer.half_life and fitted.w == layer.w
        assert actual_temperatures == temperatures
        assert not np.allclose(actual.p, source.p)
