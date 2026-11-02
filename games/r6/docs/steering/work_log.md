# Work log

Newest first.

## 2026-11-02 — First live crawl; parser version 2

Live crawl: 4,804 tournaments listed, 6,161 pages (1,357 subpages), 13.5 min, 32 MB. Kalshi: 1,438 series and 828 map markets, 17 min (4 map markets errored). Parser v2: `liquipediatier=5` → tier3 (was unknown: 30k series); series with opponent scores but no map details keep those scores and winner (unresolved 19,617 → 11,682, of which 9,317 walkovers); BRST and IRDT zones. Rebuild: 80,762 series, 86,058 maps, 0 parse errors; series links 623/719, map links 360/414. Checks: `uv run pytest -q`. Limit: unlinked series come from date-only rules and template-code team names (`tl`, `bd`).

## 2026-11-02 — Lineups from siege.gg

Added `scripts/005_load_lineups.py` (runs after 004): finished siege.gg pages give each side's lineup (oriented by team name, else score); otherwise a complete Liquipedia roster card plus that match's substitutions. Liquipedia names map to siege.gg IDs by unique folded nickname (same team within 365 days, else global). `promr6 siegegg fetch --from-db` reads the DB's siege.gg IDs. Checks: `uv run pytest -q` 146 passed; ruff clean. Limit: offline fixtures only until the live crawl lands.

## 2026-11-02 — Liquipedia, Kalshi and DB build

Ported the Liquipedia crawler/parser, Kalshi collector, SQLite rebuild and linker to R6. Added offline fixture coverage for maps, rounds, rosters, substitutions, walkovers and Kalshi schedule variants. Checks: 119 tests passed (0.82 s; baseline four steering tests 0.13 s), including the full temporary-data DB pipeline; ruff format/check and both CLI group help commands passed. Page6 has no walkover matches; real page4 and synthetic walkovers are covered. Limit: offline only; no live crawl.

## 2026-11-02 — siege.gg roster fetcher

Added `promr6 siegegg fetch/status/show`: polite cached fetcher (2 s pacing incl. redirects, backoff, one 60 s 429 retry; raw HTML gzip, atomic index; finished matches never refetch) and a pure version-1 parser for teams, siege.gg IDs, five-player rosters, scores, start time, competition and map scores. Checks: `uv run pytest -q` 24 passed; ruff clean; live fetch of matches 6168, 6100 and a 404 (99999). Limit: no loader yet; on old pages (5800, 2017) one map can be missing from map scores, which come from Liquipedia anyway.

## 2026-11-02 — Phase 0 and scaffold

Feasibility: go. `KXR6GAME` has 719 series since Nov 2025 (mostly tier 1, ~90% with a tradeable quote from Apr 2026); Liquipedia R6 has inline map and round results with siege.gg IDs back to 2022; siege.gg lists five-player rosters. Windows fixed (product.md). Scaffolded `games/r6` from `games/dota2`: AGENTS.md, steering docs, ledger, work-log script, steering test. Checks: `uv run pytest -q`, ruff. Limit: no data or model code yet.
