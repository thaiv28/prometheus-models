"""Model registry: factories accept keyword parameters; predictions precede updates."""

from functools import partial
from typing import Protocol

from promr6.ratings.elo import EloModel


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
        "rd_new": (160, 200, 240, 280, 350, 450),
        "rd_info": (0.03125, 0.0625, 0.125, 0.25, 0.5),
        "new_player": ("fixed", "teammates"),
    }
    if region:
        PARAM_GRIDS[name]["region_k"] = (2, 4)

MODELS["player_round_glicko"] = partial(
    EloModel, unit="player", credit="round", rd=True
)
PARAM_GRIDS["player_round_glicko"] = {
    "k": (16, 24, 32, 48),
    "tau": (0.5, 0.75, 1.0),
    "rd_new": (200, 280, 350, 450),
    "rd_info": (0.0625, 0.125, 0.25),
    "new_player": ("fixed", "teammates"),
}
PINNED = {}
ADOPTED = None
ADOPTED_LAYER = None
LADDER_BASE = {}
for base, credit in (("player_glicko", "binary"), ("player_round_glicko", "round")):
    for variant in ("rookie", "weights", "rookie_weights", "revert", "tier_revert"):
        name = f"{base}_{variant}"
        MODELS[name] = partial(EloModel, unit="player", credit=credit, rd=True)
        LADDER_BASE[name] = base
        grid = {}
        if "rookie" in variant:
            grid.update(
                rookie_penalty=(300, 400, 600, 800, 1200),
                rookie_maps=(200, 400, 800, 1600),
            )
        if "weights" in variant:
            grid.update(online_k=(0.5, 0.75, 1.0), tier3_k=(0.5, 0.75, 1.0))
        if variant == "revert":
            grid.update(
                season_revert=(0, 0.1, 0.2, 0.35, 0.5),
                season_month=(1, 10),
                inactive_half_life=(0, 180, 365, 730),
            )
        if variant == "tier_revert":
            grid.update(
                revert_target=("tier",),
                season_revert=(0.025, 0.05, 0.1, 0.2, 0.35),
                season_month=(1, 10),
                inactive_half_life=(0,),
            )
        PARAM_GRIDS[name] = grid
