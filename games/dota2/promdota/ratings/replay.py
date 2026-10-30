"""Load played games and replay a model chronologically without result leakage."""

from itertools import pairwise

import pandas as pd


def load_maps(conn) -> pd.DataFrame:
    return pd.read_sql(
        """SELECT g.game_id, m.match_id, m.start_utc, g."order", NULL AS map,
                  m.team1_id, m.team2_id, (g.winner = 1) AS score1, (g.winner = 2) AS score2,
                  e.region, (g.winner = 1) AS won,
                  m.best_of, m.event_id, COALESCE(e.section, 'unknown') AS section,
                  COALESCE(e.international, 0) AS international,
                  (m.winner = 1) AS series_won,
                  COALESCE(e.online, 1) AS online
           FROM games g JOIN matches m USING (match_id)
           JOIN events e USING (event_id)
           WHERE g.winner IS NOT NULL AND e.excluded = 0
           ORDER BY m.start_utc, m.match_id, g."order"
        """,
        conn,
    )


def load_lineups(conn):
    """Load complete 5v5 starters once; incomplete games have no lineup."""
    lineups = {}
    for game_id, player_id, team in conn.execute(
        "SELECT game_id, player_id, team FROM player_games ORDER BY game_id, player_id"
    ):
        if team in (1, 2):
            lineups.setdefault(game_id, ([], []))[team - 1].append(player_id)
    return {
        game: (tuple(a), tuple(b))
        for game, (a, b) in lineups.items()
        if len(a) == len(b) == 5
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
