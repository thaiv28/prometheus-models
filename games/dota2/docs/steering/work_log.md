## 2026-10-30 — Live export check

Ran `feed-state` (14 s, 4,993 finals, 6,639 teams) and a live `export` (212 s, mostly 64 Liquipedia fetches at 2 s spacing): 30 upcoming, 10 candidates, 186 TBD sides skipped, 1,212 Kalshi-priced. Through Prometheus's `saved_candidates` with the packaged blend: 20 proposals; read-only `PublicKalshi.resolve`: 6 of 10 events resolved, 4 had no two-sided quote, no identity failures. Limit: a 10-minute feed job spending ~3.5 min on Liquipedia is a large share of its CI budget; measure on GitHub.

## 2026-10-30 — Dota site feed and private candidates

Implemented adopted+form snapshots, DB-free public export, private series candidates, frozen blend artifact, listing modes and S3 workflows. Offline checks: 361 pytest tests passed in 13.59 s (initial 317 passed plus work-log guard failure, 21.36 s); CI test time decreased. Ruff format/check, YAML/shell parsing and diff whitespace passed. Real DB: state 13.69 s, 4,993 finals/6,639 rated teams; empty-cache no-fetch export 0.04 s, 4,993 finals, zero upcoming/candidates. Prometheus load_feeds accepted all 4,993 rows. Artifact: 11.55 s, eight snapshots; latest slopes 1.221800583/0.862891521, n=1,178. Checks used UV_NO_SYNC=1 because normal uv panics locally. No network, uploads, shared-cache writes or commits. Workflows not deployed; Dota disabled in execution. Requested Valorant schema file absent; validated against Prometheus directly.

## 2026-10-30 — Gate overridden by the user

The user overrode the narrowly failed holdout gate (log-loss edge significant); Phase 6 starts with Dota disabled in execution. Docs only.

## 2026-10-30 — Holdout opened: gate fails narrowly

`evaluate_elo.py --holdout` (126 s) on the frozen adopted model + form, trade set series/all tiers: blended series −0.0290 vs Kalshi (significant), but blended depth-capped flat ROI +14.5% [−0.4, +31.4]: below the playbook gate. Report `docs/elo_holdout.md`; verdict in the ledger and Current state. Stopped at playbook H4; no retune, no reopening. Checks: pytest, ruff.

## 2026-10-30 — Ladder done: adopted reversion + form over rookie/tier K

Stage 1 for the ported variants, then stage-2 look 2 with survivors and layers. Adopted `player_glicko_rw_tier_revert` (`ADOPTED`, pinned) scored with the `form` layer (`ADOPTED_LAYER`); rejected reversion to start, the KDA bonus, regional and calibration. Tier-revert grid widened to 0.025–0.35. Trade set fixed for the holdout: series only, all tiers. `docs/elo_backtest.md` is look 2. Checks: pytest, ruff, stage-1 runs (~1–2 min), look 2 (138 s).

## 2026-10-30 — Reversion, KDA performance and starter form ladder

Ported season/inactivity and tier-target reversion, within-side hero-adjusted KDA-per-minute bonuses, and causal starter form with stage-1-only fitting. Added three fixed-CANDIDATE ladder grids and pinned the rookie/weights stage-1 winner; adopted model unchanged. Performance loads once for worker and final replays. Tests cover boundaries, tier sums, prediction state, hero thresholds, missing stats/duration, causal form and fixed grids. Checks: `UV_NO_SYNC=1 uv run pytest -q`: 318 passed in 17.76 s (17.94 s wall), versus baseline 254 in 21.77 s (22.46 s wall); measured CI time did not increase. Ruff format/check passed with `UV_NO_SYNC=1`; plain uv hit a local system-configuration panic. Diff whitespace passed. Requested eight-worker real-DB smoke with `--validate-from 2026-07-01` passed in 26.83 s wall (script: 26.55 s), report `/tmp/smoke.md`. No stage-2 evaluation or adoption decision.

## 2026-10-30 — Ladder stage 1: rookie and tier/online K; per-section stage-1 tables

Rookie grid widened to penalty 300–1,200, maps 200–1,600 (the first grid chose both maxima). Stage-1 baseline comparisons now split by section, as adoption needs (they showed only "all"). Stage 1 over the pinned base: `player_glicko_rookie_weights` (penalty 600, maps 800, online K 0.75, tier-3 K 0.75) −0.0122 [−0.0139, −0.0106], significant in every tier; weights alone chose 1.0. Ledger has the numbers. No stage-2 look. Checks: pytest, ruff, three stage-1 runs (~2 min each).

## 2026-10-30 — Base pinned; first stage-2 run

OpenDota top-up with the API key: 24,690 games saved (392 missing, 187 errors); players on 84,091 of 91,503 games; Liquipedia/OpenDota winner conflicts 177 (Liquipedia kept). Widened player_glicko RD grids (rd_new 160–450, rd_info 0.03125–0.5); pinned k 24, rd_new 280, rd_info 0.0625, fixed. First stage-2 look: level with Kalshi (blended series −0.0042 n.s., +11.8% flat); numbers in the ledger, report in `docs/elo_backtest.md`, weights in `elo_weights.json`. Checks: rebuild, benchmark (stage 1 131 s; pinned run 24 s), ruff. Committed `13e7c44` with 6 tests still expecting the empty pin and old grids; fixed in the next commit (tests set their own pin state; full grid 300 points); pytest passes there.

## 2026-10-29 — OpenDota API key

The OpenDota fetcher reads `OPENDOTA_API_KEY`: requests carry it, spacing drops to 0.1 s and the per-run cap rises from 1,800 to 100,000 (default `--limit` follows). Without a key nothing changes. Typer tracebacks no longer print locals, so the key can't reach a log. Key stored in the main checkout's gitignored `.env`. Checks: pytest, ruff.

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
