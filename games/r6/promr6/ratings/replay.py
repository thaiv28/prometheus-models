"""Load played games and replay a model chronologically without result leakage."""

from itertools import pairwise

import pandas as pd


def load_maps(conn) -> pd.DataFrame:
    return pd.read_sql(
        """SELECT g.map_id, m.match_id, m.start_utc, g.map_order AS "order", g.map_name AS map,
                  m.team1_id, m.team2_id, g.rounds1 AS score1, g.rounds2 AS score2,
                  e.region, (g.winner = 1) AS won,
                  m.best_of, m.event_id, COALESCE(e.section, 'unknown') AS section,
                  COALESCE(e.international, 0) AS international,
                  (m.winner = 1) AS series_won,
                  COALESCE(e.online, 1) AS online
           FROM maps g JOIN matches m USING (match_id)
           JOIN events e USING (event_id)
           WHERE g.winner IS NOT NULL AND e.excluded = 0
           ORDER BY m.start_utc, m.match_id, g.map_order
        """,
        conn,
    )


def load_lineups(conn):
    """Accept each side independently with at least four listed starters."""
    lineups = {}
    for map_id, player_id, team in conn.execute(
        "SELECT map_id, player_id, team_side FROM player_maps ORDER BY map_id, player_id"
    ):
        if team in (1, 2):
            lineups.setdefault(map_id, ([], []))[team - 1].append(player_id)
    return {
        game: (tuple(a) if len(a) >= 4 else (), tuple(b) if len(b) >= 4 else ())
        for game, (a, b) in lineups.items()
    }


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
