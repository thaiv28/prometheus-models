"""Pure parsing of siege.gg match overviews, rosters and game results."""

import json
import re
from dataclasses import dataclass
from datetime import UTC, datetime

from bs4 import BeautifulSoup

PARSER_VERSION = 1


@dataclass(frozen=True)
class SiegePlayer:
    nickname: str
    siegegg_player_id: int


@dataclass(frozen=True)
class SiegeTeam:
    name: str
    siegegg_team_id: int | None
    score: int | None
    players: tuple[SiegePlayer, ...]


@dataclass(frozen=True)
class SiegeMatch:
    team1: SiegeTeam
    team2: SiegeTeam
    start_utc: str | None
    competition: str | None
    maps: tuple[tuple[str, int, int], ...]
    finished: bool


def _text(node):
    return node.get_text(" ", strip=True) if node else ""


def _number(node):
    value = _text(node)
    return int(value) if value.isdecimal() else None


def _team(soup, side):
    overview = soup.select_one(f".match__overview.team--{side}")
    if overview is None or not overview.select_one(".match__name"):
        return None
    link = overview.select_one('a[href*="/teams/"]')
    match = re.search(r"/teams/(\d+)", link.get("href", "")) if link else None
    players = {}
    for link in soup.select(
        f'.match__roster.team--{side} .roster__player .player__username a[href*="/players/"]'
    ):
        player = re.search(r"/players/(\d+)(?:-|/|$)", link["href"])
        if player:
            key = int(player[1])
            players.setdefault(key, SiegePlayer(_text(link), key))
    return SiegeTeam(
        _text(overview.select_one(".match__name")),
        int(match[1]) if match else None,
        _number(overview.select_one(".match__score")),
        tuple(players.values()),
    )


def _json_dates(value):
    if isinstance(value, dict):
        if isinstance(value.get("startDate"), str):
            yield value["startDate"]
        for child in value.values():
            yield from _json_dates(child)
    elif isinstance(value, list):
        for child in value:
            yield from _json_dates(child)


def _start(soup):
    values = [t["datetime"] for t in soup.select("time[datetime]")]
    for script in soup.select('script[type="application/ld+json"]'):
        try:
            values.extend(_json_dates(json.loads(script.get_text())))
        except (ValueError, TypeError):
            continue
    for value in values:
        try:
            date = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if date.tzinfo is not None:
                return date.astimezone(UTC).isoformat().replace("+00:00", "Z")
        except ValueError:
            continue
    return None


def parse_match(html: bytes | str) -> SiegeMatch | None:
    soup = BeautifulSoup(html, "lxml")
    team1, team2 = _team(soup, "a"), _team(soup, "b")
    if team1 is None or team2 is None:
        return None
    maps = []
    section = soup.select_one("#games")
    has_results = section is not None and "Game results" in _text(section)
    games = section.select(".match__games .game") if has_results else []
    for game in games:
        name = _text(game.select_one(".game__text__won"))
        name = name.removeprefix("won ")
        scores = [
            _number(item)
            for item in game.select(".game__text__score .game__score__item")
        ]
        scores = [score for score in scores if score is not None]
        if name and len(scores) == 2:
            maps.append((name, *scores))
    competition = soup.select_one('a[href*="/competitions/"]')
    return SiegeMatch(
        team1,
        team2,
        _start(soup),
        _text(competition) or None,
        tuple(maps),
        team1.score is not None and team2.score is not None and bool(games),
    )
