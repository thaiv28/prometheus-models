

## 2026-10-30 — First GitHub runs; one DB build when the top-up saves nothing

GitHub, first runs: `refresh-db` succeeded in 770 s (two DB builds, ~80 s each, plus crawl and top-up); feed cold 248 s (64 fetches), next run 39 s (1 fetched, 63 reused), 8 candidates and all feed objects in S3. The second DB build now runs only when `opendota games` saved games. Checks: pytest, ruff.

## 2026-10-30 — First GitHub refresh runs; macOS seed junk

First `refresh-db` run: crawl 5 min, then the OpenDota loader failed on `._*.json.gz` files from a seed tarball built with macOS `tar` (they had also been synced to S3: 38,434 objects, deleted). Rebuilt the seed without Mac metadata (56,303 entries, no `._`), cleared Actions caches, and the OpenDota cache now skips dot-files (test added). Seed command in deployment.md. Checks: pytest, ruff.

## 2026-10-30 — Live CI-cost check; public repo; thinner backups

Live APIs: cold export 220 s (64 fetches), warm 4.2 s (0 fetches, 64 reused); gate with nothing changed: `run=false` in 3 s; same 8 candidates as the previous code. Repo made public (Actions minutes free). GitHub backups thinned so they don't double the cron-job.org dispatches: feed `37 * * * *`, refresh `41 */6 * * *`. Cost section rewritten. Checks: pytest, ruff.

## 2026-10-30 — Incremental feed and pre-installation gate

Added version-2 upcoming page/revision caches and six-hour prefix listings, stdlib revision/event/start/age gate, hash-skipped uploads, cached uv, lower schedules and docs-only CI checks. Two-hour forced exports preserve the three-hour candidate freshness margin. Before: live export 212 s, 64 content fetches (2026-10-30). After: offline real-state exports (4,993 finals), 64 synthetic pages, 0.0357/0.0356 s, 64/0 fetches; warm run reused 64, checked two revision batches, no listings. Gate: 2.21 s unchanged with fake network and real batch spacing. These are not live latency comparisons. CI: final full suite 377 passed in 13.47 s versus prior 361 in 13.59 s. Ruff format/check and diff whitespace passed. Planning cost: 5,760–9,120 private Actions minutes/month with stated runner assumptions; live GitHub timings unmeasured. No network, shared-cache writes or commits. External schedules/deployment remain unverified.

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
