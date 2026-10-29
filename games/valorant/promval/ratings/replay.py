"""Load played maps and replay a model chronologically without result leakage."""

import json
from itertools import pairwise

import pandas as pd


def load_maps(conn) -> pd.DataFrame:
    return pd.read_sql(
        """SELECT g.game_id, m.match_id, m.start_utc, g."order", g.map, g.picked_by,
                  m.team1_id, m.team2_id, g.score1, g.score2,
                  e.region, (g.score1 > g.score2) AS won,
                  m.best_of, m.event_id, COALESCE(e.section, 'unknown') AS section,
                  COALESCE(e.international, 0) AS international,
                  (m.winner = 1) AS series_won
           FROM maps g JOIN matches m USING (match_id)
           LEFT JOIN events e USING (event_id)
           WHERE g.score1 != g.score2
           ORDER BY m.start_utc, m.match_id, g."order"
        """,
        conn,
    )


def load_lineups(conn):
    """Load each side's starters once, outside candidate replays."""
    lineups = {}
    for game_id, player_id, team in conn.execute(
        "SELECT game_id, player_id, team FROM player_maps ORDER BY game_id, player_id"
    ):
        if team in (1, 2):
            lineups.setdefault(game_id, ([], []))[team - 1].append(player_id)
    return {game: (tuple(a), tuple(b)) for game, (a, b) in lineups.items()}


def load_performance(conn) -> dict:
    """Load each player's agents and performance once, outside candidate replays."""
    performance = {}
    for (
        game,
        player,
        team,
        agents,
        kills,
        deaths,
        assists,
        rating,
        rounds,
    ) in conn.execute(
        """SELECT p.game_id, p.player_id, p.team, p.agents,
                  p.kills, p.deaths, p.assists, p.rating, g.score1 + g.score2
           FROM player_maps p JOIN maps g USING (game_id)
           WHERE g.score1 + g.score2 > 0"""
    ):
        if team not in (1, 2):
            continue
        try:
            parsed = json.loads(agents) if agents else []
        except (ValueError, TypeError):
            parsed = []
        agents = (
            tuple(parsed)
            if isinstance(parsed, list) and all(isinstance(a, str) for a in parsed)
            else ()
        )
        kda = (
            (kills + 0.5 * assists - deaths) / rounds
            if all(v is not None for v in (kills, deaths, assists))
            else None
        )
        performance.setdefault(game, {})[player] = (agents, kda, rating)
    return performance


def replay(maps, model) -> pd.DataFrame:
    keys = ["start_utc", "match_id", "order"]
    # load_maps already orders rows; avoid O(n log n) work on every candidate.
    ordered = all(
        a <= b for a, b in pairwise(maps[keys].itertuples(index=False, name=None))
    )
    result = (maps if ordered else maps.sort_values(keys, kind="stable")).copy()
    probabilities = []
    for row in result.itertuples(index=False):
        probabilities.append(model.predict(row))
        model.update(row)
    result["p"] = probabilities
    return result.reset_index(drop=True)
