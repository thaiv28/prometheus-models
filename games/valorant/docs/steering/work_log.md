# Work log

Newest first. Each entry: what changed, the checks run, remaining limits. At most 150 words.

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

## 2026-10-29 — Map strength offsets and pick bonus

Branch `map-strength`, base `main`. Added optional centred per-player/team map offsets, picker strength bonuses, and `predict_maps` without history mutation. Replay loads picked_by; two registry variants fix the adopted rookie/RD base and vary map/pick parameters. Tests cover centring, keys, update expectations, missing context, prediction state, exact default predictions, registry grids and SQL loading. Checks: 293 tests passed (24.14 s); `uv run --no-sync pytest -q`, Ruff format/check and `git diff --check` passed. Plain `uv run` crashed in macOS configuration; offline/no-sync runs passed. Grids rescaled after a first run (round-level points amplify ~3× into map odds): map_k {0.5,1,2,4}, pick_bonus {1,2,3,5,8}. Verdict: both rejected (gains below 0.0005); left off.

## 2026-10-29 — Series momentum chain

Branch `momentum`, base `main`. Added exact two-state series/slot odds and stage-1 momentum MLE using first-map probabilities. The optional benchmark flag fits each model/layer separately, then refits temperatures; Kalshi map markets use slot chances conditional on being played. Added `series_odds.py` for frozen stage comparisons, clustered intervals and calibration. Real DB: m=0.196441; m+T versus T series log-loss Δ +0.000005 stage 1, +0.000162 [+0.000028,+0.000299] stage 2; later-map slot Δ +0.001640. Checks: pytest, ruff format/check, diff check, real-DB report. Observed CI timing: 262 existing tests 24.42s → 270 tests 24.57s; 8 added tests alone 1.57s. Used `UV_OFFLINE=1 UV_NO_SYNC=1` after uv's local startup panic. Verdict: rejected (no gain over the temperature; slot odds worse); flag stays off. Limits: holdout unopened.

## 2026-10-29 — Full-crawl two-stage benchmark

Branch `full-rerun`, base `main`. Rebuilt the DB from the complete crawl (28,770 matches from 2021; 12 min) and reran the two-stage benchmark (stage 1 2023 – Aug 2025, 25,649 maps). Widened grids where choices hit edges: rookie_penalty {50,100,150,200,300}, rookie_maps {100,200,400,800}, form H {3,…,80}. Adopted rookie 200/400 (stage 2 −0.0044, significant). Dropped form (H drifts to 80; stage 2 flat, VCL significantly worse) and regional (no gain). Wrote `elo_weights.json`. Vs Kalshi: depth-capped series+map flat ROI +30.5% [+11.7, +53.2], Kelly $50 → $450. Report and ledger updated. Checks: pytest, ruff, `evaluate_elo.py` (3.7 min). Limits: holdout unopened; weights omit the series temperature.

## 2026-10-29 — Retry dropped VLR connections

Branch `crawl-retry`, base `main`. The 4-worker crawl stopped at 18,147 match pages on `RemoteDisconnected` (VLR closed a connection), which the fetcher didn't retry. It now retries `ConnectionError` and `http.client.HTTPException` with the same shared backoff as 429/5xx. Checks: pytest, ruff.

## 2026-10-29 — Stage-1 series temperature

Branch `series-temp`, base `main`. The series check showed independent-map series odds are too extreme (Bo3: 5% predicted → 10% won, 96% → 90%). `evaluate_elo.py` now fits, per model and best-of (Bo3, Bo5; ≥ 30 rows, grid 0.40–1.50), a temperature T on stage-1 series log loss and applies p′ = σ(T·logit p) to every series probability (series metrics, Kalshi series comparison, returns); Bo1 unchanged. Layer variants fit their own T on layered stage-1 rows. `--no-series-temperature` restores the old odds. Result (`rookie+form`): T = 0.79 Bo3, 0.68 Bo5; stage-2 series log loss −0.0050 [−0.0088, −0.0011]. Checks: pytest (261), ruff.

## 2026-10-29 — Realism and grid results (partial crawl)

Data and docs only. Second two-stage run on 10,027 matches (stage 1 Mar 2024 – Aug 2025). Adopted rookie discount 150 / 200 maps (stage 1 −0.0046, stage 2 −0.0069); kept form (weaker: −0.0015 / −0.0007); rejected multi-stat form (VCT worse). Depth caps leave 307/534 series and 99/675 map bets fillable; filled bets keep positive ROI but Kelly drops from $4,637 to $298. Kalshi's series price sharpens toward the start (model edge only at the early quote). Series odds from independent maps are too extreme (5% → 10%, 96% → 90%). Report committed; ledger updated. Checks: pytest.
