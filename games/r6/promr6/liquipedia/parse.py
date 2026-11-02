"""Pure parsing of cached Liquipedia templates; no fetching or filesystem access."""

import re
import unicodedata
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import NamedTuple

PARSER_VERSION = 1
TZ = dict(
    zip(
        "UTC GMT WET WEST BST CET CEST EET EEST MSK TRT AST GST IST ICT SGT PHT HKT AWST KST JST AEST AEDT NZST NZDT EST EDT CST CDT MST MDT PST PDT BRT ART CLT CLST".split(),
        [
            0,
            0,
            0,
            1,
            1,
            1,
            2,
            2,
            3,
            3,
            3,
            3,
            4,
            5.5,
            7,
            8,
            8,
            8,
            8,
            9,
            9,
            10,
            11,
            12,
            13,
            -5,
            -4,
            -6,
            -5,
            -7,
            -6,
            -8,
            -7,
            -3,
            -3,
            -4,
            -3,
        ],
    )
)
# Less common zones seen in the cache (2026-10-29 tally); ALMT is +5 since March 2024.
TZ.update(
    ALMT=5,
    AQTT=5,
    UZT=5,
    TJT=5,
    PKT=5,
    KGT=6,
    ULAT=8,
    SAST=2,
    WAT=1,
    GET=4,
    AZT=4,
    AMT=4,
    MUT=4,
    IDT=3,
    IRST=3.5,
    NPT=5.75,
    MMT=6.5,
    THA=7,
    WIB=7,
    MYT=8,
    TST=8,
    PHST=8,
    BNT=8,
    VLAT=10,
    PET=-5,
    COT=-5,
    VET=-4,
    CT=-6,
    AKDT=-8,
)


def clean(value):
    return re.sub(r"<!--.*?-->", "", value, flags=re.S).strip()


def blocks(text, name):
    """Return balanced templates with exactly this name, including nested values."""
    text = clean(text)
    pattern = re.compile(r"\{\{\s*" + re.escape(name) + r"\s*(?=[|\n}])")
    out, i = [], 0
    while match := pattern.search(text, i):
        depth, j = 1, match.start() + 2
        while j < len(text) and depth:
            if text.startswith("{{", j):
                depth += 1
                j += 2
            elif text.startswith("}}", j):
                depth -= 1
                j += 2
            else:
                j += 1
        if depth == 0:
            out.append(text[match.start() : j])
        i = j
    return out


def _parts(block):
    body = clean(block)[2:-2]
    depth, start, i, out = 0, 0, 0, []
    while i < len(body):
        two = body[i : i + 2]
        if two in ("{{", "[["):
            depth += 1
            i += 2
        elif two in ("}}", "]]"):
            depth -= 1
            i += 2
        else:
            if body[i] == "|" and depth == 0:
                out.append(body[start:i].strip())
                start = i + 1
            i += 1
    return [*out, body[start:].strip()][1:]


def params(block):
    return {
        k.strip(): clean(v)
        for p in _parts(block)
        if "=" in p
        for k, v in [p.split("=", 1)]
    }


def positional(block) -> list[str]:
    return [clean(p) for p in _parts(block) if "=" not in p]


def fold(value):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", value).lower())


def normalize_tier(value):
    return {"1": "tier1", "2": "tier2", "3": "tier3", "4": "tier3"}.get(
        str(value), "unknown"
    )


def section(tier):
    return tier if tier in ("tier1", "tier2", "tier3") else "unknown"


def parse_infobox(wikitext) -> dict:
    boxes = blocks(wikitext, "Infobox league")
    p = params(boxes[0]) if boxes else {}
    result = {
        k: p.get(k) or None
        for k in ("name", "country", "type", "sdate", "edate", "mode")
    }
    result["tier"] = (
        normalize_tier(p["liquipediatier"]) if p.get("liquipediatier") else None
    )
    result["tier_type"] = p.get("liquipediatiertype", "").strip() or None
    try:
        result["prize_usd"] = float(p["prizepoolusd"].replace(",", ""))
    except (KeyError, ValueError):
        result["prize_usd"] = None
    return result


class PlayerRef(NamedTuple):
    key: str
    name: str


class RosterCard(NamedTuple):
    team: str
    players: tuple[PlayerRef, ...]
    complete: bool


def _people(text):
    # A few pages use Person (singular) as the enclosing list as well.
    for block in blocks(text, "Person"):
        p, pos = params(block), positional(block)
        if pos and not pos[0].startswith("{{"):
            if (
                p.get("type", "").lower() != "staff"
                and p.get("played", "").lower() != "false"
            ):
                yield PlayerRef((p.get("link") or pos[0]).lower(), pos[0])
        else:
            yield from _people(block[2:-2])


def roster_cards(wikitext):
    """Listed starters only: imports never imply unlisted player identities."""
    cards = {}
    for block in blocks(wikitext, "TeamCard"):
        p = params(block)
        names = [p.get(f"t1p{i}") or p.get(f"p{i}", "") for i in range(1, 6)]
        if p.get("team"):
            people = tuple(
                PlayerRef((p.get(f"t1p{i}link") or p.get(f"p{i}link") or n).lower(), n)
                for i, n in enumerate(names, 1)
                if n
            )
            cards[fold(p["team"])] = RosterCard(p["team"], people, len(people) == 5)
    for block in blocks(wikitext, "Opponent"):
        pos, p = positional(block), params(block)
        if not pos or ("players" not in p and p.get("import", "").lower() != "true"):
            continue
        people = tuple(_people(p.get("players", "")))[:5]
        cards.setdefault(fold(pos[0]), RosterCard(pos[0], people, len(people) == 5))
    return cards


def parse_rosters(wikitext) -> dict[str, tuple[PlayerRef, ...]]:
    return {key: card.players for key, card in roster_cards(wikitext).items()}


def parse_date(value):
    """Return UTC time, precision flag and whether an unknown zone was seen."""
    match = re.match(
        r"\s*(\d{4}-\d{2}-\d{2}|[A-Za-z]+ \d{1,2}, \d{4})(?:\s*(?:-\s*)?(\d{1,2}:\d{2}))?",
        value,
    )
    if not match:
        return None, 0, False
    date = match[1].replace("Sept ", "Sep ")
    dt = None
    for fmt in ("%Y-%m-%d %H:%M", "%B %d, %Y %H:%M", "%b %d, %Y %H:%M"):
        try:
            dt = datetime.strptime(date + " " + (match[2] or "12:00"), fmt)
            break
        except ValueError:
            pass
    if dt is None:
        return None, 0, False
    zone = re.search(r"Abbr/([^}|\s]+)", value)
    explicit = zone and re.fullmatch(r"UTC([+-]\d{1,2})(?::(\d\d))?", zone[1])
    if explicit:
        sign = -1 if explicit[1].startswith("-") else 1
        hours = int(explicit[1]) + sign * int(explicit[2] or 0) / 60
    unknown = bool(zone and not explicit and zone[1] not in TZ)
    offset = hours if explicit else TZ.get(zone[1], 0) if zone else 0
    offset = offset if match[2] else 0
    return (
        (dt - timedelta(hours=offset)).replace(tzinfo=UTC),
        int(bool(match[2]) and not unknown),
        unknown,
    )


@dataclass
class ParsedMap:
    order: int
    map_name: str | None
    rounds1: int
    rounds2: int
    winner: int
    t1_atk: int
    t1_def: int
    t1_ot: int
    t2_atk: int
    t2_def: int
    t2_ot: int
    t1_first_side: str | None


@dataclass
class ParsedMatch:
    ordinal: int
    team1_key: str
    team2_key: str
    start_utc: datetime
    time_known: int
    best_of: int
    maps: list[ParsedMap]
    winner: int | None
    siegegg_id: int | None
    walkover: int
    substitutions: dict[int, list[tuple[str, str]]]


def _number(p, key):
    try:
        return int(p.get(key, ""))
    except (ValueError, TypeError):
        return None


def _map(order, value):
    maps = blocks(value, "Map")
    if not maps:
        return None
    p = params(maps[0])
    fields = [
        f"t{side}{part}" for side in (1, 2) for part in ("atk", "def", "otatk", "otdef")
    ]
    has_rounds = any(p.get(key, "").strip() for key in fields)
    has_score = any(p.get(key, "").strip() for key in ("score1", "score2"))
    if p.get("finished", "").lower() != "true" and not has_score:
        return None
    rounds = [_number(p, key) or 0 for key in fields]
    total1, total2 = (
        (sum(rounds[:4]), sum(rounds[4:]))
        if has_rounds
        else (_number(p, "score1"), _number(p, "score2"))
    )
    if total1 is None or total2 is None or total1 == total2:
        return None
    return ParsedMap(
        order,
        p.get("map") or None,
        total1,
        total2,
        1 if total1 > total2 else 2,
        rounds[0],
        rounds[1],
        rounds[2] + rounds[3],
        rounds[4],
        rounds[5],
        rounds[6] + rounds[7],
        p.get("t1firstside") if p.get("t1firstside") in ("atk", "def") else None,
    )


def _read_match(block, ordinal, counts):
    p = params(block)
    teams, opponents, substitutions = [], [], {}
    for side in (1, 2):
        opponent = blocks(p.get(f"opponent{side}", ""), "TeamOpponent")
        if len(opponent) != 1 or not positional(opponent[0]):
            return None
        teams.append(positional(opponent[0])[0].strip().lower())
        op = params(opponent[0])
        opponents.append(op)
        substitutions[side] = []
        for sub in blocks(op.get("substitutes", ""), "Substitution"):
            sp = params(sub)
            incoming = blocks(sp.get("in", ""), "OpponentPlayer")
            player_in = (
                positional(incoming[0])[0]
                if incoming and positional(incoming[0])
                else sp.get("in", "")
            )
            if player_in and sp.get("out"):
                substitutions[side].append((player_in, sp["out"]))
    if any(t in ("", "tbd", "bye") for t in teams):
        return None
    dt, known, unknown = parse_date(p.get("date", ""))
    counts["unknown_tz"] += unknown
    if dt is None:
        counts["dateless"] += 1
        return None
    walkover = int(
        p.get("walkover", "").lower() not in ("", "false", "0")
        or any(
            op.get("score", "").upper() in ("W", "FF", "L", "DQ") for op in opponents
        )
    )
    maps, mapkeys = (
        [],
        sorted((k for k in p if re.fullmatch(r"map\d+", k)), key=lambda k: int(k[3:])),
    )
    for key in mapkeys:
        order = int(key[3:])
        if not 1 <= order <= 9:
            counts["map_order_gt9"] += 1
        elif not walkover and (m := _map(order, p[key])):
            maps.append(m)
    wins1, wins2 = sum(m.winner == 1 for m in maps), sum(m.winner == 2 for m in maps)
    winner = None if wins1 == wins2 or walkover else 1 if wins1 > wins2 else 2
    return ParsedMatch(
        ordinal,
        *teams,
        dt,
        known,
        _number(p, "bestof") or len(mapkeys),
        maps,
        winner,
        _number(p, "siegegg"),
        walkover,
        substitutions,
    )


def parse_matches(
    title, wikitext, *, counts: Counter | None = None
) -> list[ParsedMatch]:
    counts = counts if counts is not None else Counter()
    matches = []
    for ordinal, block in enumerate(blocks(wikitext, "Match")):
        m = _read_match(block, ordinal, counts)
        if m and (
            m.maps or m.walkover or params(block).get("finished", "").lower() == "true"
        ):
            counts["walkovers"] += m.walkover
            counts["unresolved_matches"] += m.winner is None
            matches.append(m)
    return matches


@dataclass
class ScheduledMatch:
    title: str
    ordinal: int
    team1_key: str
    team2_key: str
    start_utc: datetime
    time_known: int
    best_of: int | None
    maps: list[tuple[int, int]]
    finished: bool


def parse_scheduled(title, wikitext) -> list[ScheduledMatch]:
    matches = []
    for ordinal, block in enumerate(blocks(wikitext, "Match")):
        m = _read_match(block, ordinal, Counter())
        if m:
            matches.append(
                ScheduledMatch(
                    title,
                    ordinal,
                    m.team1_key,
                    m.team2_key,
                    m.start_utc,
                    m.time_known,
                    m.best_of or None,
                    [(int(g.winner == 1), int(g.winner == 2)) for g in m.maps],
                    bool(m.winner is not None or m.walkover),
                )
            )
    return matches
