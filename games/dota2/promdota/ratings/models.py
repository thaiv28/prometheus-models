"""Model registry: factories accept keyword parameters; predictions precede updates."""

from functools import partial
from typing import Protocol

from promdota.ratings.elo import EloModel


class Model(Protocol):
    def predict(self, row) -> float: ...

    def update(self, row) -> None: ...


class CoinModel:
    def predict(self, row):
        return 0.5

    def update(self, row):
        pass


class TeamEloModel(EloModel):
    """v1 name retained for team/binary Elo without offsets."""


MODELS = {"coin": CoinModel, "team_elo": TeamEloModel}
PARAM_GRIDS = {"coin": {}, "team_elo": {"k": (16, 24, 32, 48, 64, 96)}}
for region in (False, True):
    name = "player_binary" + ("_region" if region else "")
    MODELS[name] = partial(
        EloModel, unit="player", credit="binary", region_k=16 if region else 0
    )
    PARAM_GRIDS[name] = {
        "k": (16, 24, 32, 48, 64, 96),
        "new_player": ("fixed", "teammates"),
    }
    if region:
        PARAM_GRIDS[name]["region_k"] = (2, 4, 8, 16)

for region in (False, True):
    name = "player_region_glicko" if region else "player_glicko"
    MODELS[name] = partial(
        EloModel, unit="player", credit="binary", rd=True, region_k=4 if region else 0
    )
    PARAM_GRIDS[name] = {
        "k": (16, 24, 32, 48, 64),
        "rd_new": (280, 350, 450, 600),
        "rd_info": (0.125, 0.25, 0.5, 1.0),
        "new_player": ("fixed", "teammates"),
    }
    if region:
        PARAM_GRIDS[name]["region_k"] = (2, 4)

# Phase 3 pins the stage-1 winner after evaluating the real Dota 2 database.
PINNED = {}
ADOPTED = "player_glicko"

# Only adjustment grids live here. The benchmark anchors these to the current
# PINNED base, or crosses the full base grid when explicitly using --full-grid.
LADDER_BASE = {}
for variant in ("rookie", "weights", "rookie_weights"):
    name = f"player_glicko_{variant}"
    MODELS[name] = partial(EloModel, unit="player", credit="binary", rd=True)
    LADDER_BASE[name] = "player_glicko"
    grid = {}
    if "rookie" in variant:
        grid.update(
            rookie_penalty=(150, 200, 300, 400, 600),
            rookie_maps=(50, 100, 200, 400),
        )
    if "weights" in variant:
        grid.update(online_k=(0.5, 0.75, 1.0), tier3_k=(0.5, 0.75, 1.0))
    PARAM_GRIDS[name] = grid
