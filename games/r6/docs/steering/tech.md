# Tech

## Stack

Python 3.12, uv, SQLite (raw SQL), typer CLI `promr6`, pytest, ruff. Ported from `../dota2` and `../cs2` as each phase needs it.

## Layout

| Path | Contents |
|---|---|
| `promr6/main.py` | CLI entry point |
| `promr6/liquipedia/__init__.py` | Liquipedia package |
| `promr6/liquipedia/http.py` | Polite API requests, contact and retry backoff |
| `promr6/liquipedia/cache.py` | Raw gzip page cache and atomic index |
| `promr6/liquipedia/crawl.py` | Categories, revisions and tournament subpages |
| `promr6/liquipedia/parse.py` | Pure wikitext parser, version 1 |
| `promr6/liquipedia/regions.py` | R6 host macro regions |
| `promr6/liquipedia/cli.py` | Crawl and cache status commands |
| `promr6/kalshi/__init__.py` | Kalshi package |
| `promr6/kalshi/api.py` | Injectable public Kalshi API client |
| `promr6/kalshi/collect.py` | Catalogs, trades, candles and books |
| `promr6/kalshi/cli.py` | Collect and books commands |
| `promr6/link.py` | Market rules, team identity and match/map linking |
| `scripts/001_create_tables.sql` | SQLite source schema |
| `scripts/002_load_liquipedia.py` | Cached pages → events, matches, maps and rosters |
| `scripts/003_load_kalshi.py` | Cached market catalogs → SQLite |
| `scripts/004_load_lineups.py` | Cached siege.gg and complete Liquipedia cards → map lineups, `team_siegegg` names |
| `scripts/005_link_kalshi.py` | Links and settlement report |
| `scripts/setup_db.sh` | Offline database rebuild |
| `scripts/kalshi_data.sh` | Kalshi collection and optional S3 backup |
| `tests/test_liquipedia_crawl.py` | Offline crawl/cache/HTTP checks |
| `tests/test_liquipedia_parse.py` | Real R6 wikitext fixtures |
| `tests/test_liquipedia_db.py` | Temporary database and rebuild checks |
| `tests/test_kalshi_collect.py` | Offline collector checks |
| `tests/test_link.py` | Rules, identity passes and settlement checks |
| `scripts/work_log.py` | Work-log reader and rotation (pre-commit hook) |
| `tests/test_steering.py` | Work-log and doc-budget guard |
| `promr6/siegegg/http.py` | Polite urllib requests, redirects and retries |
| `promr6/siegegg/cache.py` | Atomic raw HTML and fetch metadata |
| `promr6/siegegg/parse.py` | Pure typed match and roster parser |
| `promr6/siegegg/fetch.py` | Injectable, cache-aware match fetching and summaries |
| `promr6/siegegg/cli.py` | `siegegg fetch/status/show` commands |
| `tests/test_siegegg.py` | Offline fixtures and temporary-cache transport tests |

## siege.gg fetcher

Source: `https://siege.gg/matches/<id>`; positional IDs and `--from-file` combine with `--from-db` (the DB at `PROMR6_DB`, default `db/r6.db`), selecting distinct non-null `matches.siegegg_id` newest first. Under `PROMR6_DATA` (default `data/`), `siegegg/matches/<id>.html.gz` preserves response bytes; atomic `siegegg/index.json` stores status, final URL, UTC fetch timestamp and finished flag. Save raw before parsing. Finished pages never refetch, even with `--refresh`; unfinished and 404 pages require `--refresh`. `--limit` caps attempted IDs, excluding cache hits; summary counts unique IDs processed.

Requests and redirects are spaced at least two seconds apart. The repository User-Agent accepts contact via `SIEGEGG_CONTACT`. Timeouts, dropped connections and 5xx retry with backoff (three tries); 429 waits 60 seconds and retries once. Tests inject transports and use temporary data roots.

Pure `parse_match(bytes | str)` returns immutable match/team/player dataclasses, ordered rosters deduplicated by player ID, scores, optional UTC time and competition, map scores in team order, and finished status; 404 HTML returns `None`. Finished means two numeric overview scores plus at least one game in “Game results”. `PARSER_VERSION = 1`; bump when parser output changes. Fixture 5800 has a 2–1 series score but only two recorded maps; the parser preserves those two.

## Liquipedia crawler

`promr6 liquipedia crawl [--limit N] [--full]` uses only `action=query` at `https://liquipedia.net/rainbowsix/api.php`. Requests use gzip, at least two seconds between requests and retry backoff. User-Agent: `r6-model/0.1 (+https://github.com/thaiv28/prometheus-models)`, with contact overridden by `LIQUIPEDIA_CONTACT`. Credit: Liquipedia contributors, CC BY-SA 3.0.

Category:Tournaments supplies roots; namespace-0 `list=allpages` and tab links discover subpages, parented to the nearest tournament root. Revision checks fetch changed pages; `--full` refreshes all. R6 has no namespace-130 Match-page pass. `PROMR6_DATA` defaults to `data/`; raw responses are saved under `liquipedia/pages/<sha1-prefix>/<sha1>.json.gz`, with revisions and ownership in atomic `index.json`. `promr6 liquipedia status` reports cache counts and latest fetch time. Parsers never fetch.

## Database

`scripts/setup_db.sh` rebuilds `db/r6.db` offline through scripts 001–005. Tables: `events`, `teams`, `players`, `matches`, `maps`, `rosters`, `player_maps`, `match_substitutions`, `kalshi_markets`, `team_aliases`, `kalshi_links`. Parse failures are written beside the database in `parse_errors.txt`; loaders print aggregate counts.

Event IDs use page IDs; missing infobox fields inherit independently from ancestors. Only one title per page ID is loaded. Teams, players and matches use deterministic hashes, retaining Dota's duplicate rules. Tiers 1/2/3–4 map to tier1/tier2/tier3; other values are unknown. Region groups are NA, EU/MENA, SA/Brazil/LATAM, APAC and CN. Online/LAN and international classifications remain separate.

Inline Match blocks contain TeamOpponent sides, optional best-of and siege.gg IDs. ISO dates and listed time zones convert to UTC; unknown zones are counted and clear `time_known`. Finished maps with unequal totals count as resolved; attack, defense and overtime rounds are summed, falling back to scores when all round fields are blank. Map IDs are match ID × 10 + map order (1–9). Series scores and winners are recomputed from maps. Walkovers retain series, discard maps and have NULL winners; unresolved series are counted separately. Substitutions store player in/out per match side.

TeamCards supply five starters, excluding later slots; Persons excludes staff and players marked unplayed. Imported partial rosters retain listed players with `complete=0`. `004_load_lineups.py` fills `player_maps` offline: finished cached siege.gg pages supply each side with at least four players (retaining extras above five); missing sides use complete Liquipedia cards from the nearest ancestor with a card, applying folded-name substitutions. Orientation uses normalized team names, then unique direct/swapped series scores or single-map rounds; unresolved orientation skips the siege.gg page. Players use `siegegg:<id>` keys and deterministic `stable_id("player:siegegg:<id>")` IDs, with the most frequent nickname. Folded Liquipedia nicknames unify to a unique siege.gg identity on the same team within 365 days, otherwise globally; ambiguous names retain `liquipedia:<folded>` keys and corresponding stable IDs. Partial cards supply no lineup.

## Kalshi collector

`promr6 kalshi collect [--no-books] [--limit N]` refreshes `KXR6GAME` and `KXR6MAP`, archives final-market trades/candles and snapshots active books. `--limit` caps new trade/candle fetches combined. `promr6 kalshi books --every 60 --minutes 60` refreshes active tickers on each pass. Raw files live under `PROMR6_DATA/kalshi` (default `data/kalshi`); tests use temporary roots and injected API clients. `scripts/kalshi_data.sh` can back up to `r6-model/kalshi/` in `DATA_BACKUP_BUCKET`.

## Kalshi ↔ Liquipedia links

Catalogs load from `kalshi/markets/{KXR6GAME,KXR6MAP}.json`; absent inputs load zero rows. Rules identify R6 tournaments, opponents, dates and optional EDT/EST times. Date-only schedules use noon ET (16:00Z) of that date as the window centre, ±30 hours. Team name variants are the display name, the template key and every siege.gg name in `team_siegegg` (written by 004). Map N targets `map_order=N`; map-event series lookup replaces `KXR6MAP-` with `KXR6GAME-`.

Exact, alias and anchor passes repeat before fuzzy matching (both team similarities ≥0.8). Anchors require a unique confirmed team and plausible opponent; conflicting aliases are dropped, ambiguous candidates stay unresolved, and excluded events supply no candidates. Generic academy overlap protection remains. `team_aliases` retains consistent competitor identities; `kalshi_links` records match/map identity, method and failure reason. Settlements are cross-checked against winners; `db/link_report.txt` records unresolved links and mismatches.

## Model change rules

Do not tune or select on holdout. Stage 1 tunes on outcomes only, [2023-01-01,2026-01-01). Stage 2 freezes parameters and validates outcomes and Kalshi's tradeable quote, [2026-01-01,2026-07-01). Holdout is 2026-07-01 on, opened once. Tradeable quote: first hourly bid/ask at least 30 minutes after listing and at least 2 hours before start, spread ≤0.06. Use paired match-clustered intervals; require significant stage-1 gain and no stage-2 regression, including guarded sections: all, tier1, tier2, tier3, international.

- An added parameter, feature or layer also needs a stage-1 gain of at least 0.0005 log loss.
- A stage-2 gain is reported but never rescues a change that failed stage 1; don't tune on stage 2 to pass it.
- Removals ship when every guarded section's interval stays below +0.0005 on both stages (non-inferior).
- Every tested model idea goes in the [research ledger](../research/README.md), adopted or not, with its numbers; count the tests run against stage 2.
- Trading results are reported, not gates. Data fixes ship when correct and the benchmark doesn't get significantly worse.
