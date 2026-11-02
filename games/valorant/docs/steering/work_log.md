# Work log

## 2026-11-02 — Feed gate before install

Added a stdlib pre-install gate over the previous feed and open KXVALORANTGAME events. Live matches, passed starts, new ratings-state ETag, age, clock skew and missing/broken inputs force export; unchanged runs skip install/export/publication/dispatch and save only changed gate bytes. Prediction-log and schedule-cache persistence remain on full runs. Checks: full pytest, ruff format/check, system-python gate help, actionlint and work-log rotation passed. Live runner savings remain unmeasured; unchanged fixtures skip export after the event probe.

## 2026-11-02 — CI: shared setup, one Kalshi workflow, actionlint, dispatch on change

Scheduled jobs use the shared setup-game composite with uv download caching; Kalshi collection uses one matrix with independent game concurrency and unchanged S3 prefixes. Feeds store content-sha256 metadata excluding the top-level generated timestamp and dispatch Prometheus only on content changes; Dota retains byte-hash upload skips and its early gate. CI runs actionlint for .github changes while preserving game scoping. Checks passed: actionlint 1.7.12; full pytest; ruff format/check; eight CI-scope and fifteen mocked feed-upload scenarios; work-log rotation. Plain uv triggers a macOS configuration panic, so checks use UV_OFFLINE=1 UV_NO_SYNC=1.

Newest first. Each entry: what changed, the checks run, remaining limits. At most 150 words.

## 2026-11-02 — Workflows run from prometheus-models

Scheduled workflows moved to root `.github/workflows/valorant-{feed,kalshi-collect,refresh-db}.yml` with working directory `games/valorant`, game-prefixed concurrency groups and repo-root cache/hash paths. Raw cache keys are game-prefixed; S3 prefixes are unchanged. Per-game ci.yml is replaced by root CI, which scopes game workflow changes to that game. Checks with `UV_OFFLINE=1 UV_NO_SYNC=1`: `uv run --frozen pytest -q` (420 passed), `uv run ruff format --check .` and `uv run ruff check .` passed. Root `python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('.github/workflows/*.yml')]"` passed; directory layout and six CI classification scenarios passed. `python3 scripts/work_log.py rotate` passed. Plain uv hit a macOS configuration panic; sandbox blocked git mv's index lock, so files were moved on disk.

## 2026-11-02 — KDA model switch reverted

Reverted the commit below at the user's request: the feed and execution keep `player_round_glicko_rookie_tier_revert`, its weights and the earlier `blend_artifact.json`. The KDA variant stays in `models.py` and `elo_weights.json` for research. Checks: pytest, ruff.

## 2026-11-02 — Feed and execution use the KDA model

Branch `valorant-kda`, base `main`. `feed.py` and `trading.py` now replay `player_round_glicko_rookie_tier_revert_perf_kda` with `load_performance` (without it the bonus silently switches off; a new test guards both). Weights gain its stage-1 series temperatures (Bo3 0.87, Bo5 0.82, from a rerun on a rebuilt DB matching the perf-share report). `blend_artifact.json` refit: latest gap slope 0.583 (was 0.535). Stage 2 vs Kalshi, KDA vs `tier_revert`: series −0.0119 vs −0.0093, map −0.0122 vs −0.0108 (neither significant); full Kelly series+map $6,737 vs $5,490, depth-capped $543 vs $495. Checks: pytest 421, ruff. Limit: production still runs from `valorant-model` until cutover.

## 2026-11-02 — Moved into prometheus-models

Imported with full history into `prometheus-models/games/valorant/` (branch `main`, base: this repo's local `main` merged with `origin/main`; unpushed `perf-share` merge kept, conflicts in `elo_weights.json` (both keys kept) and the work log (entries pooled) resolved). `tests/test_steering.py` now finds the git repo from a subfolder and checks only this game's paths; the work-log hook moved to the repo root and the CI to a root workflow that checks only changed games. Production workflows still run from the old repo until cutover. Checks: steering guard fails without this entry and passes with it; full pytest and ruff from `games/valorant/`.

## 2026-10-29 — KDA performance bonus adopted

Branch `perf-share`, base `main`. Player updates add a zero-sum bonus within each side: perf_k·(stat − causal agent EMA, centred on teammates), RD-weighted, off by default. Stat is KDA=(K+0.5A−D)/rounds or VLR rating; `load_performance` feeds it through the benchmark scripts. Two variants on the frozen `tier_revert` base, perf_k grid 1–20 (first grid 5–160 hit its low edge). Both chose 7: stage 1 −0.0030 (significant), stage 2 −0.0012 (KDA) / −0.0009 (rating), n.s., no section worse; KDA is better vs Kalshi on stage 2. Adopted the KDA variant; weights and `docs/elo_backtest.md` regenerated. Checks: pytest 351 → 378 tests (32.0 s → 25.4 s; timing noise), ruff, full benchmark (16.6 min). Codex wrote the code. Limit: no holdout left; confirm on the forward window from 2026-10-29.

## 2026-10-29 — Holdout opened

Branch `holdout`, base `main`. Pulled Kalshi from S3, rebuilt the DB, and ran `evaluate_elo.py --holdout` once (July 1 – Oct 28, 2026; 1,663 maps) with frozen stage-1 parameters. `tier_revert` beats team Elo (0.650 vs 0.670 map log loss) but matches Kalshi raw (series +0.009, maps +0.0005, n.s.); blended −0.005 / −0.004 (n.s.), VCL significant. Depth-capped blended series +17.0% [+1.0, +33.7]; maps −3.6%; international series negative. Report `docs/elo_holdout.md`; ledger and current state updated. Checks: pytest. Limit: the holdout is spent; later ideas need a new forward window.

## 2026-10-29 — Tier-mean reversion adopted

Branch `tier-revert`, base `main`. `revert_target="tier"` pulls a player toward the running mean rating of their latest tier (vct, vcl, gc, t3, collegiate; offseason/unknown keep the previous tier), kept as O(1) per-tier sums. New variant `player_round_glicko_rookie_tier_revert`. Stage 1 chose 0.2 at Nov 1: −0.0007 [−0.0014, −0.0001], no section worse; stage 2 −0.0015 (n.s.; VCL −0.0021 significant; GC +0.0029 n.s.); blended vs Kalshi within 0.0005 of the old model. Adopted; series T now Bo3 0.91, Bo5 0.84. Report and weights rewritten. Caveat: sixth candidate tested on stage 2, proposed after the global version's stage-2 GC result. Checks: pytest, ruff, `evaluate_elo.py`.

## 2026-10-29 — Rating reversion toward the mean

Branch `revert`, base `main`. Added off-by-default player season/inactivity reversion toward the initial rating, separate update dates, non-mutating prediction calculations, and the fixed-base `player_round_glicko_rookie_revert` grid (40 candidates). Existing defaults retain exact synthetic predictions; RD behavior is unchanged. Tests cover boundaries, UTC offsets, multiplicative decay, teammate initialization, prediction/update agreement, validation and registry parameters with RD on/off. Documented formulas/defaults/grid. Checks: full suite passed (347 tests, 26.20 s); Ruff format/check passed. Benchmark: stage 1 chose a 0.2 pull at Jan 1, no inactivity pull (−0.0006 [−0.0013, −0.0000]); stage 2 −0.0007 (n.s.) with GC significantly worse (+0.0040). Not adopted; left off.
