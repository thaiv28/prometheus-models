"""Causal homes and frozen seven-region layer fits."""

import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from promdota.ratings.layers import (
    HALF_LIVES,
    LAYERS,
    REGIONS,
    CalibrationLayer,
    FormLayer,
    RegionalLayer,
    causal_features,
)


def planted(n=10000):
    rng = np.random.default_rng(38)
    a = rng.integers(0, len(REGIONS), n)
    b = (a + rng.integers(1, len(REGIONS), n)) % len(REGIONS)
    logits = rng.normal(0, 1, n)
    frame = pd.DataFrame({"game_id": np.arange(n), "p": 1 / (1 + np.exp(-logits))})
    features = pd.DataFrame(
        {"home1": np.array(REGIONS)[a], "home2": np.array(REGIONS)[b]}
    )
    features.index.name = "game_id"
    effects = np.array([0.45, -0.35, 0.15, -0.25, 0.2, -0.1, -0.1])
    return rng, frame, features, logits, effects[a] - effects[b]


def sample(rng, z):
    return rng.binomial(1, 1 / (1 + np.exp(-z)))


def test_regional_recovery_scope_zero_sum_and_index():
    rng, frame, features, logits, effect = planted()
    frame["won"] = sample(rng, 1.25 * logits + effect)
    layer = RegionalLayer()
    layer._features = features
    layer.fit(frame)
    assert layer.rows == len(frame)
    assert layer.s == pytest.approx(1.25, abs=0.08)
    assert list(layer.effects.values()) == pytest.approx(
        [0.45, -0.35, 0.15, -0.25, 0.2, -0.1, -0.1], abs=0.08
    )
    assert sum(layer.effects.values()) == pytest.approx(0, abs=1e-14)
    features.loc[0, "home2"] = features.loc[0, "home1"]
    features.loc[1, "home1"] = None
    apply = frame.iloc[:4].copy()
    apply.index = [8, 3, 3, 7]
    adjusted = layer.apply(apply)
    assert adjusted.index.equals(apply.index)
    assert adjusted.iloc[:2].tolist() == apply.p.iloc[:2].tolist()
    assert not np.allclose(adjusted.iloc[2:], apply.p.iloc[2:])
    assert "rows=10000" in layer.describe() and "ridge=4" in layer.describe()


def test_regional_threshold_ridge_and_refit():
    _, frame, features, logits, effect = planted(100)
    # Fractional targets make the unpenalized optimum exact, isolating shrinkage.
    frame["won"] = 1 / (1 + np.exp(-(1.7 * logits + effect)))
    small = RegionalLayer()
    small._features = features
    small.fit(frame.iloc[:49])
    pd.testing.assert_series_equal(small.apply(frame), frame.p)
    assert "identity (<50" in small.describe()
    small.fit(frame.iloc[:50])
    large = RegionalLayer()
    large._features = features
    large.fit(pd.concat([frame.iloc[:50]] * 100, ignore_index=True))
    assert abs(small.s - 1) < abs(large.s - 1)
    assert np.linalg.norm(list(small.effects.values())) < np.linalg.norm(
        list(large.effects.values())
    )
    small.fit(frame.iloc[:0])
    assert small.s == 1 and all(e == 0 for e in small.effects.values())


def test_causal_homes_and_excluded_events():
    conn = sqlite3.connect(":memory:")
    conn.executescript(
        (
            Path(__file__).resolve().parents[1] / "scripts/001_create_tables.sql"
        ).read_text()
    )
    conn.executescript("""
        INSERT INTO teams(team_id,key) VALUES (10,'a'),(20,'b');
        INSERT INTO events(event_id,title,section,region,international,excluded)
        VALUES (1,'NA','tier1','NA',0,0),(2,'EU','tier2','EU',0,0),
               (3,'CIS','tier1','CIS',1,0),(4,'AS','tier3','AS',0,1);
    """)
    for match, event in [(1, 1), (2, 2), (3, 3), (4, 4), (5, 2)]:
        conn.execute(
            """INSERT INTO matches(match_id,event_id,page,ordinal,start_utc,time_known,
                team1_id,team2_id,score1,score2,winner)
                VALUES (?,?,'Synthetic',0,?,1,10,20,2,0,1)""",
            (match, event, f"2024-01-{match:02d}T00:00:00Z"),
        )
    conn.executemany(
        'INSERT INTO games(game_id,match_id,"order",winner) VALUES (?,?,?,?)',
        [
            (1, 1, 1, 1),
            (2, 1, 2, 1),
            (3, 2, 1, 1),
            (4, 3, 1, 1),
            (5, 4, 1, 1),
            (6, 5, 1, 1),
            (7, 5, 2, 1),
            (8, 5, 3, None),
        ],
    )
    features = causal_features(conn, {})
    assert features.index.tolist() == [1, 2, 3, 4, 6, 7]
    assert features.home1.tolist() == [None, "NA", "NA", "NA", "NA", "NA"]
    assert features.home1.tolist() == features.home2.tolist()
    assert set(LAYERS) == {"none", "regional", "calibration", "form"}
    conn.close()


def test_regional_frozen_outcomes():
    rng, frame, features, logits, effects = planted(1000)
    frame["won"] = sample(rng, logits + effects)
    layer = RegionalLayer()
    layer._features = features
    layer.fit(frame.iloc[:700])
    before = layer.apply(frame.iloc[700:])
    description = layer.describe()
    frame.loc[700:, "won"] = 1 - frame.loc[700:, "won"]
    layer.fit(frame.iloc[:700])
    assert layer.describe() == description
    pd.testing.assert_series_equal(before, layer.apply(frame.iloc[700:]))


def test_calibration_recovery_threshold_and_frozen_groups():
    rng = np.random.default_rng(38)
    logits = rng.normal(0, 2, 10000)
    frame = pd.DataFrame(
        {
            "p": 1 / (1 + np.exp(-logits)),
            "won": sample(rng, 0.7 * logits),
            "section": "tier1",
            "online": 0,
        }
    )
    small = frame.iloc[:299].assign(section="tier3", online=1)
    layer = CalibrationLayer()
    layer.fit(pd.concat([frame, small], ignore_index=True))
    assert layer.temperatures[("tier1", 0)] == pytest.approx(0.7, abs=0.04)
    assert layer.temperatures[("tier3", 1)] == 1
    assert "tier1/online=0: rows=10000, T=" in layer.describe()
    assert "tier3/online=1: rows=299, T=1.0000" in layer.describe()
    expected = 1 / (1 + np.exp(-layer.temperatures[("tier1", 0)] * logits))
    np.testing.assert_allclose(layer.apply(frame), expected)
    np.testing.assert_allclose(layer.apply(small), small.p)
    unseen = small.assign(section="tier2")
    np.testing.assert_allclose(layer.apply(unseen), unseen.p)
    before = layer.apply(frame)
    pd.testing.assert_series_equal(before, layer.apply(frame.assign(won=1 - frame.won)))
    layer.fit(small)
    assert layer.temperatures == {("tier3", 1): 1}


def test_calibration_identity_index_clipping_and_threshold():
    frame = pd.DataFrame(
        {
            "p": [0.1, 0.3, 0.8],
            "won": [0, 1, 1],
            "section": ["tier1", "tier2", "tier3"],
            "online": [0, 1, 1],
        },
        index=[8, 3, 3],
    )
    layer = LAYERS["calibration"]()
    layer.fit(frame)
    pd.testing.assert_series_equal(layer.apply(frame), frame.p, check_exact=False)
    extremes = frame.assign(p=[0, 1, 0.5])
    np.testing.assert_allclose(layer.apply(extremes), [1e-6, 1 - 1e-6, 0.5])
    threshold = pd.concat([frame.iloc[:1]] * 300, ignore_index=True)
    layer.fit(threshold)
    assert layer.temperatures[("tier1", 0)] != 1


def test_form_recovery_frozen_stage1_missing_and_empty():
    rng, frame, features, logits, _ = planted(2000)
    for h in HALF_LIVES:
        features[f"form1_{h}"] = rng.normal(0, 1, len(frame))
        features[f"form2_{h}"] = rng.normal(0, 1, len(frame))
    frame["won"] = sample(rng, logits + 2.3 * (features.form1_3 - features.form2_3))
    layer = FormLayer()
    layer._features = features
    layer.fit(frame.iloc[:1500])
    assert layer.half_life == 3
    assert layer.w == pytest.approx(2.3, abs=0.3)
    prediction = layer.apply(frame.iloc[1500:])
    description = layer.describe()
    frame.loc[1500:, "won"] = 1 - frame.loc[1500:, "won"]
    layer.fit(frame.iloc[:1500])
    assert layer.describe() == description
    pd.testing.assert_series_equal(prediction, layer.apply(frame.iloc[1500:]))
    features.loc[1500, "form1_3"] = np.nan
    assert layer.apply(frame.iloc[1500:]).iloc[0] == frame.p.iloc[1500]
    layer.fit(frame.iloc[:0])
    pd.testing.assert_series_equal(layer.apply(frame), frame.p)
