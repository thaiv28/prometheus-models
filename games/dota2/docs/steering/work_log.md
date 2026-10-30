## 2026-10-29 — Stage-1 baseline on partial data

Ran `evaluate_elo.py --validate-from 2026-07-01` (stage 1 only, 64 s, 8 jobs) on the 2026-10-29 build: player_glicko 0.6294 vs team_elo 0.6501 game log loss, 38,131 games; RD parameters at grid minima. Recorded in the ledger and Current state; no code change. OpenDota per-game top-up day 1 running.

## 2026-10-29 — Stage subpages, retry on dropped connections, date-only Kalshi schedules

Branch `subpages`. Dota tournaments link stages through per-series tab templates, so the crawler now also lists every non-redirect article (`list=allpages`, ns 0, ~170 requests) and crawls titles under a tournament root. Tab links drop `#fragment`s and collapse spaces; the loader skips a second title with the same page ID. Liquipedia retries dropped connections. Kalshi's 2025 markets give only a date: it reads as noon New York time. Real data: +642 subpages, orphan Match pages 1,786 → 10; 45,645 series, 91,503 games (57,759 with players). Kalshi links: series 909 → 1,380 of 1,869, games 1,882 of 2,564; 12 result mismatches. Checks: pytest, ruff, real crawl and rebuild.

## 2026-10-29 — Binary Dota ratings and benchmark

Ported replay, complete 5v5 lineups, causal homes and two-stage evaluation to games/player_games. Registered binary player Glicko and optional ladder variants; removed round credit and old pins. Preserved earlier-lineup/team-pseudo-player fallback, RD, series temperatures, quote orientation, returns and causal blends. Updated Dota windows and game report wording; retained the outcome-based independence diagnostic. Restored five test modules using synthetic schema-backed databases; no shared cache writes. Checks: `UV_NO_SYNC=1 uv run pytest -q` (247 passed, zero skips, 12.56s versus baseline 127 passed/117 skipped, 7.65s), Ruff format/check, CLI help and diff whitespace passed. Plain uv run still panics in this sandbox; Ruff passes with UV_NO_SYNC. Tech: 2,402 words. Real DB, model selection/pins and benchmark report regeneration remain pending; no real-data benchmark or network used.

## 2026-10-29 — Dota 2 data layer

Converted Liquipedia crawling/parsing to Dota tournaments and Match pages; added projected OpenDota bulk/single caches and offline winner/player enrichment. Replaced maps with games, ported Kalshi Dota loading/linking, and updated steering docs. Checks: `UV_NO_SYNC=1 uv run pytest -q` (127 passed, 117 requested Phase 3 skips), Ruff format/check, diff whitespace and CLI help passed. The full temporary-cache setup_db test verifies reversed Vici winner, ten players and four Kalshi markets. Baseline archive: 263 passed, 3 skipped in 12.40s; current suite 1.14s, with Phase 3 coverage deferred. Plain uv sync panics in this sandbox; the already-synced environment works with UV_NO_SYNC. Unresolved series now stay with a NULL winner, so `opendota games` finds their match IDs after a rebuild. Real crawl pending.

## 2026-10-29 — Scaffold from cs2-model

Copied cs2-model `origin/main` (75bab17) per Prometheus `docs/playbooks/new_game.md`; package `promdota`, CLI `promdota`, DB `db/dota2.db`. Removed feed, trading, blend artifact, stored weights and their workflows/tests until the holdout gate passes. Product and Current state rewritten with the Phase 0 findings (Kalshi volumes, Liquipedia and OpenDota coverage, windows). Data and benchmark code are still CS2's. Checks: pytest (263 passed, 3 skipped), ruff.
