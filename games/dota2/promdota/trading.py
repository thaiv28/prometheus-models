"""Frozen blend coefficients and private raw inputs for Prometheus execution."""

import hashlib
import json
import math
import re
from datetime import UTC, datetime, timedelta

import numpy as np
import pandas as pd

from promdota import blend
from promdota.link import scheduled_utc
from promdota.ratings.models import ADOPTED, ADOPTED_LAYER, MODELS, PINNED

VALIDATE_FROM = "2025-11-01"
RULES = re.compile(
    r"^If (?P<side>.+?) wins the (?P<event>.+): (?P<team1>.+?) vs\.? "
    r"(?P<team2>.+?) Dota 2 match originally scheduled for "
    r"(?P<day>\w{3} \d{1,2}, \d{4})(?: at (?P<time>\d{1,2}:\d{2} [AP]M) E[DS]T)?"
)


def instant(value):
    return datetime.fromisoformat(str(value).replace("Z", "+00:00")).astimezone(UTC)


def build_blend_artifact(rows, game, series_ticker, now):
    """Monthly fits using every eligible completed series strictly before M."""
    snapshots = []
    if not rows.empty:
        dates = pd.to_datetime(rows.start_utc, utc=True)
        eligible = (
            (rows.kind == "series")
            & rows.won.notna()
            & (dates >= pd.Timestamp(VALIDATE_FROM, tz="UTC"))
        )
        if eligible.any():
            first = dates[eligible].min().normalize().replace(day=1)
            last = pd.Timestamp(now).tz_convert("UTC").normalize().replace(day=1)
            for boundary in pd.date_range(
                first + pd.offsets.MonthBegin(),
                last + pd.offsets.MonthBegin(),
                freq="MS",
            ):
                training = rows[eligible & (dates < boundary)]
                if len(training) < 300:
                    continue
                a, b, n = blend.fit(training.p, training.market_p, training.won)
                snapshots.append(
                    {
                        "available_from": boundary.isoformat(),
                        "trained_through": dates.loc[training.index].max().isoformat(),
                        "training_series": n,
                        "market_slope": float(a),
                        "gap_slope": float(b),
                    }
                )
    return {
        "version": "game-blend-v1",
        "game": game,
        "series_ticker": series_ticker,
        "clip": 0.01,
        "protocol": f"Tradeable quote, no intercept, monthly earlier-only fits from {VALIDATE_FROM}, {ADOPTED}+{ADOPTED_LAYER} + stage-1 series temperature.",
        "snapshots": snapshots,
    }


def adopted_replay(conn):
    """Replay pinned Elo, fit its adopted layer and temperatures on stage 1 only."""
    from promdota.benchmark import series_rows, temper, with_series_temperature
    from promdota.evaluation import game_losses
    from promdota.ratings.layers import LAYERS
    from promdota.ratings.replay import (
        load_lineups,
        load_maps,
        load_performance,
        replay,
    )

    lineups, performance = load_lineups(conn), load_performance(conn)
    model = MODELS[ADOPTED](lineups=lineups, performance=performance, **PINNED[ADOPTED])
    source = replay(load_maps(conn), model)
    dates = pd.to_datetime(source.start_utc, utc=True)
    tuning = (dates >= pd.Timestamp("2023-01-01", tz="UTC")) & (
        dates < pd.Timestamp(VALIDATE_FROM, tz="UTC")
    )
    layer = LAYERS[ADOPTED_LAYER](
        context={"conn": conn, "lineups": lineups, "performance": performance}
    )
    layer.fit(source.loc[tuning].copy())
    source["p"] = layer.apply(source)
    # Same grid, minimum count and first-minimum tie breaking as evaluate_elo.
    grid = np.round(np.arange(0.40, 1.501, 0.01), 2)
    temperatures = {1: 1.0}
    for best_of, group in series_rows(source.loc[tuning]).groupby("best_of"):
        temperature = 1.0
        if best_of != 1 and len(group) >= 30:
            losses = [
                game_losses(temper(group.p, t), group.won).log_loss.mean() for t in grid
            ]
            temperature = float(grid[int(np.argmin(losses))])
        temperatures[int(best_of)] = temperature
    return model, with_series_temperature(source, temperatures), layer, temperatures


def adopted_series_rows(conn, directory):
    """Build the benchmark's tradeable series rows for adopted Elo plus form."""
    from promdota.benchmark import report_market_rows

    _, source, _, _ = adopted_replay(conn)
    rows = report_market_rows(conn, source, directory)
    return rows.loc[rows.kind == "series"].copy() if not rows.empty else rows


def candidates(feed_rows, linked_markets, now, *, data_through=None, skipped=None):
    """Build execution records; linked pairs are ordered as our team 1, team 2.

    ``skipped`` optionally receives a count of rejected linked feed matches.
    Current markets are supplied by the feed's existing linker, never fetched here.
    """
    now = now.astimezone(UTC)
    at = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    matches = []
    for row in feed_rows:
        if row["match_id"] not in linked_markets:
            continue
        try:
            if (
                row["status"] != "upcoming"
                or instant(row["start"]) <= now
                or row["best_of"] is None
            ):
                raise ValueError("ineligible feed match")
            pair = linked_markets[row["match_id"]]
            if len(pair) != 2 or any(
                m.get("status") not in (None, "open", "active") for m in pair
            ):
                raise ValueError("not an open pair")
            parsed = [RULES.match(m.get("rules_primary") or "") for m in pair]
            if not all(parsed):
                raise ValueError("invalid rules")
            rules = [
                {
                    k: v.strip() if v is not None else None
                    for k, v in p.groupdict().items()
                }
                for p in parsed
            ]
            names = [r["side"] for r in rules]
            teams = sorted([rules[0]["team1"], rules[0]["team2"]])
            if (
                len(set(teams)) != 2
                or sorted(names) != teams
                or any(sorted([r["team1"], r["team2"]]) != teams for r in rules)
                or any(
                    (m.get("yes_sub_title") or "").strip() != r["side"]
                    for m, r in zip(pair, rules)
                )
                or pair[0]["event_ticker"] != pair[1]["event_ticker"]
                or not pair[0]["event_ticker"].startswith("KXDOTA2GAME-")
                or any(
                    m.get("series_ticker", m.get("series", "KXDOTA2GAME"))
                    != "KXDOTA2GAME"
                    for m in pair
                )
            ):
                raise ValueError("inconsistent teams")
            starts = [instant(scheduled_utc(m["rules_primary"])) for m in pair]
            start = starts[0]
            if (
                starts[1] != start
                or start <= now
                or abs(start - instant(row["start"])) > timedelta(hours=18)
            ):
                raise ValueError("inconsistent start")
            p = row["p_series"]
            raw = {names[0]: round(p, 6), names[1]: round(1 - p, 6)}
            if not all(math.isfinite(v) and 0 < v < 1 for v in raw.values()):
                raise ValueError("invalid probability")
            event = pair[0]["event_ticker"]
            identity = json.dumps(
                ["dota2", teams, event], separators=(",", ":"), ensure_ascii=False
            )
            matches.append(
                {
                    "execution_candidate": {
                        "kind": "candidate-v1",
                        "schema_version": 1,
                        "game": "dota2",
                        "series_ticker": "KXDOTA2GAME",
                        "at": at,
                        "fixture_id": hashlib.sha256(identity.encode()).hexdigest(),
                        "event_ticker": event,
                        "teams": teams,
                        "team_homes": {},
                        "international": bool(
                            row.get("international", row["section"] == "INTL")
                        ),
                        "group": "dota2-series",
                        "start": start.strftime("%Y-%m-%dT%H:%MZ"),
                        "raw": raw,
                        "provenance": {
                            "model": ADOPTED,
                            "match_id": row["match_id"],
                            "p_game": row["p_game"],
                            "p_series": p,
                            "best_of": row["best_of"],
                            "data_through": data_through,
                            "names": [row["name1"], row["name2"]],
                            "start": row["start"],
                        },
                    }
                }
            )
        except (KeyError, TypeError, ValueError):
            if skipped is not None:
                skipped["candidates"] += 1
    return {"version": 1, "game": "dota2", "generated": at, "matches": matches}
