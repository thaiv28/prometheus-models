# Work log

Newest first.

## 2026-11-02 — siege.gg roster fetcher

Added `promr6 siegegg fetch/status/show`: polite cached fetcher (2 s pacing incl. redirects, backoff, one 60 s 429 retry; raw HTML gzip, atomic index; finished matches never refetch) and a pure version-1 parser for teams, siege.gg IDs, five-player rosters, scores, start time, competition and map scores. Checks: `uv run pytest -q` 24 passed; ruff clean; live fetch of matches 6168, 6100 and a 404 (99999). Limit: no loader yet; on old pages (5800, 2017) one map can be missing from map scores, which come from Liquipedia anyway.

## 2026-11-02 — Phase 0 and scaffold

Feasibility: go. `KXR6GAME` has 719 series since Nov 2025 (mostly tier 1, ~90% with a tradeable quote from Apr 2026); Liquipedia R6 has inline map and round results with siege.gg IDs back to 2022; siege.gg lists five-player rosters. Windows fixed (product.md). Scaffolded `games/r6` from `games/dota2`: AGENTS.md, steering docs, ledger, work-log script, steering test. Checks: `uv run pytest -q`, ruff. Limit: no data or model code yet.
