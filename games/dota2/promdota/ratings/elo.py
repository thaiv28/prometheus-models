"""Composable Elo variants and the original binary team Elo reference."""

from dataclasses import dataclass
from datetime import UTC, datetime
from math import isfinite, log, log1p, tanh

from promdota.ratings.regions import macro_region

TIER_RANKS = {"tier3": 1, "tier2": 2, "tier1": 3}


@dataclass(frozen=True)
class EloConfig:
    k: float = 32.0
    init: float = 1500.0
    scale: float = 400.0


class TeamElo:
    def __init__(self, config=None):
        self.config = config or EloConfig()
        self.ratings = {}

    def expected(self, a, b):
        rating_a = self.ratings.get(a, self.config.init)
        rating_b = self.ratings.get(b, self.config.init)
        return 1 / (1 + 10 ** ((rating_b - rating_a) / self.config.scale))

    def update(self, a, b, score_a):
        delta = self.config.k * (score_a - self.expected(a, b))
        self.ratings[a] = self.ratings.get(a, self.config.init) + delta
        self.ratings[b] = self.ratings.get(b, self.config.init) - delta


class EloModel:
    """Composable credit, rating unit and macro-region offsets.

    predict may initialize starters, but only update records lineup/home history.
    Home counts have seven buckets, so all history maintenance is constant time.
    """

    def __init__(
        self,
        *,
        unit="team",
        credit="binary",
        k=32.0,
        c=4.0,
        region_k=0.0,
        new_player="fixed",
        lineups=None,
        init=1500.0,
        scale=400.0,
        rd=False,
        rd_new=280.0,
        rd_floor=140.0,
        rd_growth=10.0,
        rd_info=0.125,
        rookie_penalty=0.0,
        rookie_maps=30,
        move_up_penalty=0.0,
        move_down_bonus=0.0,
        move_maps=20,
        online_k=1.0,
        tier3_k=1.0,
        season_revert=0.0,
        season_month=1,
        inactive_half_life=0.0,
        revert_target="init",
        performance=None,
        perf_stat="kda",
        perf_k=0.0,
        perf_alpha=0.01,
        perf_min_count=20,
    ):
        if unit not in {"team", "player"} or credit not in {
            "binary",
            "margin",
        }:
            raise ValueError("unknown Elo unit or credit")
        if new_player not in {"fixed", "teammates"}:
            raise ValueError("unknown new_player mode")
        if (
            not isfinite(season_revert)
            or not 0 <= season_revert <= 1
            or not isinstance(season_month, int)
            or isinstance(season_month, bool)
            or not 1 <= season_month <= 12
            or not isfinite(inactive_half_life)
            or inactive_half_life < 0
        ):
            raise ValueError("invalid player reversion parameters")
        if (
            perf_stat != "kda"
            or not isfinite(perf_k)
            or perf_k < 0
            or not isfinite(perf_alpha)
            or not 0 < perf_alpha <= 1
            or not isinstance(perf_min_count, int)
            or isinstance(perf_min_count, bool)
            or perf_min_count < 1
        ):
            raise ValueError("invalid performance parameters")
        self.performance = performance if performance is not None else {}
        self.perf_stat, self.perf_k = perf_stat, perf_k
        self.perf_alpha, self.perf_min_count = perf_alpha, perf_min_count
        self.hero_mean, self.hero_count = {}, {}
        self.global_mean = None
        self.season_revert, self.season_month = season_revert, season_month
        self.inactive_half_life = inactive_half_life
        self.last_played = {}
        if revert_target not in {"init", "tier"}:
            raise ValueError("unknown revert_target")
        # Tier target: running rating sums by each player's latest ranked section.
        self.revert_target = revert_target
        self.tier_of, self.tier_sum, self.tier_count = {}, {}, {}
        if k <= 0 or c <= 0 or region_k < 0 or scale <= 0:
            raise ValueError("Elo parameters must be positive (region_k may be zero)")
        if not (0 < online_k <= 2 and 0 < tier3_k <= 2):
            raise ValueError("online_k and tier3_k must be in (0, 2]")
        self.online_k, self.tier3_k = online_k, tier3_k
        self.rd = bool(rd and unit == "player")
        if self.rd and (
            not all(isfinite(v) for v in (rd_new, rd_floor, rd_growth, rd_info))
            or rd_floor <= 0
            or rd_new < rd_floor
            or rd_growth < 0
            or rd_info <= 0
        ):
            raise ValueError("invalid player RD parameters")
        self.rd_new, self.rd_floor = rd_new, rd_floor
        self.rd_growth, self.rd_info = rd_growth, rd_info
        self.rd_variance = {}
        self.last_seen = {}
        if unit == "player" and (
            not all(
                isfinite(v)
                for v in (
                    rookie_penalty,
                    rookie_maps,
                    move_up_penalty,
                    move_down_bonus,
                    move_maps,
                )
            )
            or min(rookie_penalty, move_up_penalty, move_down_bonus) < 0
            or min(rookie_maps, move_maps) <= 0
        ):
            raise ValueError("invalid player rookie/move parameters")
        self.rookie_penalty, self.rookie_maps = rookie_penalty, rookie_maps
        self.move_up_penalty, self.move_down_bonus = move_up_penalty, move_down_bonus
        self.move_maps = move_maps
        self.map_counts = {}
        self.tier_counts = {}
        self.tier_homes = {}
        self.unit, self.credit = unit, credit
        self.k, self.c = k, c
        self.region_k, self.new_player = region_k, new_player
        self.init, self.scale = init, scale
        self.lineups = lineups if lineups is not None else {}
        self.ratings = {}
        self.last_lineups = {}
        self.homes = {}
        self.home_counts = {}
        self.offsets = {}
        # Preserve the v1 public rating accessor.
        self.elo = self

    def _units(self, row, side):
        team = getattr(row, f"team{side}_id")
        if self.unit == "team":
            return (team,)
        starters = self.lineups.get(row.game_id, ((), ()))[side - 1]
        if starters:
            return starters
        return self.last_lineups.get(team, (("team", team),))

    def _reversion_date(self, row):
        if self.unit != "player" or not (self.season_revert or self.inactive_half_life):
            return None
        date = row.start_utc
        if isinstance(date, str):
            date = datetime.fromisoformat(date)
        if date.tzinfo is None:
            return date.replace(tzinfo=UTC)
        return date.astimezone(UTC)

    def _rating(self, player, date=None):
        rating = self.ratings[player]
        previous = self.last_played.get(player)
        if date is None or previous is None or date <= previous:
            return rating
        factor = 1.0
        if self.season_revert:
            # The season index changes at midnight UTC on the first of the month.
            seasons = (date.year - (date.month < self.season_month)) - (
                previous.year - (previous.month < self.season_month)
            )
            factor *= (1 - self.season_revert) ** seasons
        if self.inactive_half_life:
            days = (date - previous).total_seconds() / 86400
            factor *= 0.5 ** (days / self.inactive_half_life)
        if factor == 1:
            return rating
        target = self.init
        section = self.tier_of.get(player)
        if section is not None:
            target = self.tier_sum[section] / self.tier_count[section]
        return target + factor * (rating - target)

    def _set_rating(self, player, value):
        section = self.tier_of.get(player)
        if section is not None:
            self.tier_sum[section] += value - self.ratings[player]
        self.ratings[player] = value

    def _effective_rating(self, player, rank, date=None):
        rating = self._rating(player, date)
        maps = self.map_counts.get(player, 0)
        if self.rookie_penalty and maps < self.rookie_maps:
            rating -= self.rookie_penalty * (1 - log1p(maps) / log1p(self.rookie_maps))
        home = self.tier_homes.get(player)
        if rank is not None and home is not None and rank != home:
            played = self.tier_counts.get(player, {}).get(rank, 0)
            adjustment = -self.move_up_penalty if rank > home else self.move_down_bonus
            rating += adjustment * max(0.0, 1 - played / self.move_maps)
        return rating

    def _strength(self, units, rank=None, date=None):
        known = [self._rating(p, date) for p in units if p in self.ratings]
        initial = (
            sum(known) / len(known)
            if known and self.new_player == "teammates"
            else self.init
        )
        for player in units:
            self.ratings.setdefault(player, initial)
        if self.unit == "player" and (
            self.rookie_penalty or self.move_up_penalty or self.move_down_bonus
        ):
            return sum(self._effective_rating(p, rank, date) for p in units) / len(
                units
            )
        return sum(self._rating(p, date) for p in units) / len(units)

    def _state(self, row, *, revert=True):
        a, b = self._units(row, 1), self._units(row, 2)
        home_a, home_b = self.homes.get(row.team1_id), self.homes.get(row.team2_id)
        rank = TIER_RANKS.get(getattr(row, "section", None))
        date = self._reversion_date(row) if revert else None
        strength_a, strength_b = (
            self._strength(a, rank, date),
            self._strength(b, rank, date),
        )
        if self.region_k:
            strength_a += self.offsets.get(home_a, 0)
            strength_b += self.offsets.get(home_b, 0)
        # Stable logistic, algebraically the original base-ten Elo formula.
        x = (strength_a - strength_b) / self.scale
        if abs(x) < 300:
            expected = 1 / (1 + 10 ** (-x))
        else:
            expected = 1.0 if x > 0 else 0.0
        return a, b, home_a, home_b, expected

    def predict(self, row):
        return self._state(row)[-1]

    def score(self, row):
        if self.credit == "binary":
            return row.won
        magnitude = 0.5 * tanh(abs(row.score1 - row.score2) / self.c)
        return 0.5 + (magnitude if row.won else -magnitude)

    def update(self, row):
        played = self._reversion_date(row)
        if played is not None:
            # Compute every reverted value before committing: targets read the sums.
            reverted = {
                player: self._rating(player, played)
                for player in dict.fromkeys(
                    (*self._units(row, 1), *self._units(row, 2))
                )
                if player in self.ratings
            }
            for player, value in reverted.items():
                self._set_rating(player, value)
        a, b, home_a, home_b, expected = self._state(row, revert=False)
        error = self.score(row) - expected
        k = self.k
        if getattr(row, "online", False):
            k *= self.online_k
        if getattr(row, "section", None) == "tier3":
            k *= self.tier3_k
        delta = k * error
        bonus = {}
        observations = []
        if self.unit == "player" and self.perf_k > 0:
            performances = self.performance.get(row.game_id, {})
            for units in (a, b):
                raw = {}
                for player in units:
                    perf = performances.get(player)
                    if perf is None or perf[1] is None:
                        continue
                    hero, value = perf
                    qualified = (
                        hero is not None
                        and self.hero_count.get(hero, 0) >= self.perf_min_count
                    )
                    expectation = (
                        self.hero_mean[hero]
                        if qualified
                        else self.global_mean
                        if self.global_mean is not None
                        else 0.0
                    )
                    raw[player] = value - expectation
                    observations.append((hero, value))
                if len(raw) >= 2:
                    # Centre the bonus within each side so it is zero-sum.
                    centre = sum(raw.values()) / len(raw)
                    bonus.update(
                        (player, self.perf_k * (value - centre))
                        for player, value in raw.items()
                    )
        if self.rd:
            date = row.start_utc
            if isinstance(date, str):
                date = datetime.fromisoformat(date)
            information = self.rd_info * (log(10) / self.scale) ** 2
            information *= expected * (1 - expected)
        for units, change in ((a, delta), (b, -delta)):
            for player in units:
                weight = 1.0
                if self.rd:
                    variance = self.rd_variance.get(player, self.rd_new**2)
                    days = (
                        max(
                            0.0, (date - self.last_seen[player]).total_seconds() / 86400
                        )
                        if player in self.last_seen
                        else 0.0
                    )
                    variance = min(self.rd_new**2, variance + self.rd_growth**2 * days)
                    weight = variance / self.rd_floor**2
                    self.rd_variance[player] = max(
                        self.rd_floor**2, 1 / (1 / variance + information)
                    )
                    self.last_seen[player] = date
                self._set_rating(
                    player,
                    self.ratings[player] + (change + bonus.get(player, 0.0)) * weight,
                )
                if played is not None:
                    self.last_played[player] = played
        for hero, value in observations:
            if hero is not None:
                if hero not in self.hero_mean:
                    self.hero_mean[hero] = value
                else:
                    self.hero_mean[hero] += self.perf_alpha * (
                        value - self.hero_mean[hero]
                    )
                self.hero_count[hero] = self.hero_count.get(hero, 0) + 1
            if self.global_mean is None:
                self.global_mean = value
            else:
                self.global_mean += self.perf_alpha * (value - self.global_mean)
        if (
            self.region_k
            and home_a is not None
            and home_b is not None
            and home_a != home_b
        ):
            change = self.region_k * error
            self.offsets[home_a] = self.offsets.get(home_a, 0) + change
            self.offsets[home_b] = self.offsets.get(home_b, 0) - change
        region = macro_region(getattr(row, "region", None))
        for side, units in ((1, a), (2, b)):
            team = getattr(row, f"team{side}_id")
            if self.unit == "player":
                self.last_lineups[team] = units
                section = getattr(row, "section", None)
                if self.revert_target == "tier" and section in TIER_RANKS:
                    for player in units:
                        previous = self.tier_of.get(player)
                        if previous == section:
                            continue
                        if previous is not None:
                            self.tier_sum[previous] -= self.ratings[player]
                            self.tier_count[previous] -= 1
                        self.tier_of[player] = section
                        self.tier_sum[section] = (
                            self.tier_sum.get(section, 0.0) + self.ratings[player]
                        )
                        self.tier_count[section] = self.tier_count.get(section, 0) + 1
                for player in units:
                    if self.rookie_penalty:
                        self.map_counts[player] = self.map_counts.get(player, 0) + 1
                    rank = TIER_RANKS.get(getattr(row, "section", None))
                    if (
                        self.move_up_penalty or self.move_down_bonus
                    ) and rank is not None:
                        counts = self.tier_counts.setdefault(player, {})
                        counts[rank] = counts.get(rank, 0) + 1
                        previous = self.tier_homes.get(player)
                        if counts[rank] > counts.get(previous, 0):
                            self.tier_homes[player] = rank
            if (
                self.region_k
                and region is not None
                and not getattr(row, "international", False)
            ):
                counts = self.home_counts.setdefault(team, {})
                counts[region] = counts.get(region, 0) + 1
                previous = self.homes.get(team)
                # The incremented bucket is the only possible new leader.
                if counts[region] > counts.get(previous, 0):
                    self.homes[team] = region
