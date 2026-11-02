# Work log archive

Older entries moved from `work_log.md`, newest first.

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

## 2026-10-29 — Wider rookie/form grids; multi-stat form layer

Branch `form-grid`, base `main`. Expanded rookie penalty/map grids while fixing K=32 and rd_new=280 for rookie variants; moves-only unchanged. Form half-lives now {2,3,5,8,12}. Added `form_multi` and ordered `regional_form_multi`: causal starter means of rating, ACS, KAST, ADR and fk−fd, stage-1 standard deviations, ridge-1 logistic weights and stage-1 half-life selection. Shared cached history skips null observations per stat. Tests cover grids, recovery, selection, frozen scales, missing/constant data, causality, composition and registration. Checks: `uv run pytest -q` (243 passed, 18.99s; prior recorded 235 in 18.08s), `uv run ruff format --check`, `uv run ruff check`, `git diff --check` passed. Used `UV_OFFLINE=1 UV_NO_SYNC=1` after plain uv hit its local startup panic. Limits: not benchmarked; no network or holdout access.

## 2026-10-29 — Backtest realism: rounded fees, depth caps, quote robustness, series check

Branch `realism`, base `main`. Added cent-ceiling order fees, $1 contract stakes with fee-inclusive flat ROI, rounded-fee Kelly cash sizing, and tape-volume depth caps (6 hours, 50%; missing tapes unfilled). Returns pair unlimited and capped fills. Added 24/6-hour quote rules, frozen-model quote robustness, and standalone/in-report series calibration, conditional map-2 and decider residual checks. Tests cover fees, depth/orientation, cash caps, quote cutoffs, report assembly without retuning, planted dependence and calibration counts. Baseline: 235 tests in 26.19s. Checks: `uv run pytest -q` (252 passed, 22.38s), `uv run ruff format --check`, `uv run ruff check`, and `git diff --check` passed. Plain offline `uv run` hits the local startup panic; checks use `UV_OFFLINE=1 UV_NO_SYNC=1`. Limits: no network, real-data benchmark or holdout evaluation; tape volume is a fill proxy without queue position/slippage. Changes uncommitted as requested.

## 2026-10-29 — refresh-db: fresh AWS login before uploads

Branch `game-candidates`, base `main`. The first Valorant run with the speedups spent 52 min reparsing every match (`cached=0`: restored pickles looked older than their raw pages, since neither S3 nor the Actions cache keeps file times), then its snapshot upload failed with `ExpiredToken` (the OIDC session lasts an hour). Parsed pickles are now touched before every crawl, not only on a cache miss, and the job logs in to AWS again before the uploads. Checks: workflow tests, YAML parse.

## 2026-10-29 — refresh-db: no VLR S3 listing on a cache hit

Branch `game-candidates`, base `main`. With the raw Actions cache restored, the VLR `aws s3 sync` still listed and compared ~77k objects (7.5 min of a run). Only this workflow writes them, so the sync now runs only on a cache miss; Kalshi data (written by the collector) still syncs every run. Checks: workflow tests, YAML parse. Timing to confirm on the next run.

## 2026-10-29 — Refresh speed (requested branch refresh-speed, base main)

Cache built DBs by input inventory and code hash; unchanged hours skip rebuilds when S3 state metadata `inputs=<hash>` matches. Cold raw-cache misses extract `valorant-model/seed/raw.tar.zst` before sync; successful raw-cache saves refresh missing or week-old seeds. Rebuilds publish the walk-forward artifact to `valorant-model/feed/blend_artifact.json`, without changing the committed artifact. Workflow tests cover cache keys, skip guards, uploads and seed guards. Checks: offline no-sync pytest: 393 passed (81.58s); workflow tests: 9 passed (0.06s). Ruff format/check, cached-PyYAML parsing and Bash syntax pass. Standard uv/uvx hit sandbox/runtime errors; checks use offline no-sync and cached PyYAML. Runner timings must be measured after merge. Sandbox blocked Git metadata writes, so fetch/branch creation failed; edits remain in the existing game-feed checkout.

The DB cache key hashes file contents (not sizes), so a same-size page revision still rebuilds. Workflow tests updated for the content hash.

## 2026-10-29 — Game execution inputs

Branch `game-candidates`, base `main`. Added frozen `promval/blend_artifact.json` and atomic private `data/feed/candidates.json`, uploaded to private `valorant-model/feed/candidates.json` for Prometheus's execution Lambda. Shared benchmark row construction preserves quote rules, stage-1 temperatures and orientation. Candidates validate paired rules, names and starts; export both international and domestic groups. Artifact: 7 snapshots; latest November 1, 2026, a=1.069742465, b=0.535410478, n=1263. Checks (UV_OFFLINE=1 UV_NO_SYNC=1; plain uv startup panics): pytest 390 passed in 25.56s versus existing 373 in 27.69s; 16 new trading tests 0.18s; Ruff format/check and diff check passed. Real blend-artifact, feed-state and offline snapshot export passed (5 upcoming, 2,457 finals, 1,287 prices, zero candidates). No network or commits; Prometheus packaging/deployment remains external.

## 2026-10-29 — refresh-db: save the raw cache before the DB build

Branch `game-feed`, base `main`. The first `refresh-db` run spent 35 min seeding ~1 GB from S3, then timed out (45 min) in the DB build, so the Actions cache was never saved. The raw cache is now saved right after the crawl; on a cache miss, parsed pickles are touched after the S3 download (S3 sets mtimes to upload time, which made valid pickles look older than their raw pages and forced a full reparse); timeout 90 min. Checks: workflow tests (new order guard), YAML parse. Run timing to follow on GitHub.

## 2026-10-29 — Snapshot site feed workflows

Branch `game-feed`, base phase-1 commit `45b5ba5`. Split DB replay/closing quotes into an atomic, versioned gzip-pickle snapshot; exports load it without SQLite. Added hourly refresh-db and 10-minute feed dispatch workflows (GitHub schedules are backups), raw Actions cache and conditional S3 prediction-log persistence. S3: `valorant-model/{vlr/,kalshi/,feed/{state.pkl.gz,predictions.json,valorant.json.gz,upcoming/}}`. Checks: offline/no-sync uv pytest (369 passed, 27.81 s), Ruff format/check, shell syntax, diff check and real-DB snapshot/export passed; 1,890,179-byte state built in 3.83 s; export 0.54 s versus DB 4.68 s, identical after removing generated. Plain uv startup panics on macOS. Limits: workflows not yet run on GitHub; runner times unmeasured; raw cache must be seeded in S3 once. No network or commits. Merged main: the feed now replays the adopted `player_round_glicko_rookie_tier_revert`; its stage-1 series temperatures (Bo3 0.91, Bo5 0.84, from docs/elo_backtest.md) are stored in elo_weights.json.

## 2026-10-29 — Website prediction feed

Branch `game-feed`, base `main`. Added `promval export` for the Prometheus feed: upcoming/live matches, replayed results, section filters and oriented Kalshi current/closing prices. Future calls refresh in `data/predictions.json`, then freeze at start; missing future listings are removed. Upcoming pages use a separate cache; `--no-fetch` is offline. Stored existing series temperatures and retained them on refits; shared candle helpers preserve benchmark behavior. Checks (UV_OFFLINE=1 UV_NO_SYNC=1; plain uv startup panics): pytest 363 passed, Ruff format/check, diff check, real-DB offline export (2,457 finals; 1,287 prices). Observed suite timing: 347 existing tests 66.17s → 363 tests 76.04s; 16 feed tests alone 2.38s. Limits: DB only as fresh as the last crawl + `setup_db`; VLR skips same-day results, so finished matches await a result until ingested; TBD sides omitted. No commits.

## 2026-10-28 — First two-stage benchmark (partial crawl)

Data and docs only. Rebuilt on the crawl so far (7,597 matches from 2024-06) and ran the two-stage benchmark: stage 1 Oct 2024 – Aug 2025, stage 2 Sep 2025 – Jun 2026. Adopted (candidates, to rerun on full history): rookie discount (stage 1 −0.0046, stage 2 −0.0070, both significant) and the form layer (−0.0030 / −0.0027). Rejected: tier moves (no effect). Regional calibration not significant on 327 cross-region maps. Best, `player_round_glicko_rookie+form`: blended series vs Kalshi −0.017 (significant). Committed `docs/elo_backtest.md`; ledger updated. Checks: pytest.

## 2026-10-28 — Regional calibration and form layers

Branch `layers`, base `main`. Added ridge-shrunk zero-sum regional calibration, player-rating recent form with stage-1 half-life selection, and their ordered combination. A shared causal history pass records pre-map homes/form, caches per instance, and ignores international hosts for home counts. Reports include fitted parameters and row counts. Synthetic tests cover causality, decay, missing ratings, regional shrinkage/thresholds, parameter recovery, stage separation, composition and report integration. Checks: `UV_NO_SYNC=1 uv run pytest -q` (235 passed, 18.08s; baseline 224 in 24.95s), `uv run ruff format --check`, `uv run ruff check` (both with `UV_NO_SYNC=1`), and `git diff --check` passed. Plain offline `uv run` hit the local startup panic; `UV_NO_SYNC=1` uses the existing environment without network. Limits: not yet benchmarked on full data.

## 2026-10-28 — Model change rules and research ledger

Docs only. Added tech.md "Model change rules" (two stages: tune on outcomes 2023-01 to 2025-09, validate frozen models against outcomes and Kalshi 2025-09 to 2026-07, holdout opened once; adopt only on a significant stage-1 gain with no guarded regression and ≥ 0.0005 for additions; confirm on stage 2; removals non-inferior; data fixes lighter), `docs/research/README.md` (ledger, backfilled with every variant tested so far and its partial-crawl numbers), and AGENTS.md pointers: ledger entries for every test, commit `docs/elo_backtest.md` with each model change (first full-data report pending the crawl). Checks: pytest.

## 2026-10-28 — Two-stage benchmark and layer hook

Branch `two-stage`, base `main`. Split outcome tuning (2023-01-01 to 2025-09-01 exclusive) from frozen validation against Kalshi (2025-09-01 to 2026-07-01 exclusive). Added ISO date controls, context-aware layer hooks with identity default, validation summaries, monthly identical-row breakdowns, and synthetic separation/layer tests. Holdout remains optional and excluded from selection/blend fitting. Checks: offline `uv run pytest -q` (201 passed, 17.46s), `uv run ruff format --check`, and `uv run ruff check`, with `UV_NO_SYNC=1` to avoid sandbox sync startup panic; direct virtualenv checks also passed. Limits: no full-data benchmark or network; baseline CI timing unavailable after initial uv startup failure. Monthly ROI avoids unnecessary bootstrap work.

## 2026-10-28 — Rookie discount and tier moves

Branch `rookie-moves`, base `main`. Added optional player-only logarithmic rookie discounts and linearly fading tier-move adjustments to prediction/update strengths, with update-only map counts and majority tier homes. Registered three narrowed-grid Glicko variants; existing defaults retain exact predictions. Tests cover decay, promotions/demotions, ties, excluded sections, update expectations, leakage and registry grids. Checks: offline `uv run --no-sync pytest -q` (221 passed, 14.40 s; baseline 198 in 21.52 s), `ruff format --check`, `ruff check`, and `git diff --check` passed. Plain `uv run` panicked locally; used the existing environment with `--no-sync`. Limits: not yet benchmarked; no holdout tuning or network access.

## 2026-10-28 — Parallel VLR crawl

Branch `crawl-workers`, base `main`. `promval vlr crawl --workers N` fetches each results page's missing match and economy pages in N threads. The fetcher is thread-safe: one shared request slot per `--min-interval` (the total rate cap), and a 429/5xx pauses every worker for the backoff, not only the one that hit it. Default stays 1 worker. Checks: pytest, ruff.

## 2026-10-28 — Pick advantage check; capped-Kelly rerun

Docs only. On Feb–Jun 2026 picked maps (2,409), the picking team won 52.5% vs 50.0% predicted by player_round_glicko (+2.5 pts, 95% [+0.5, +4.4]); a constant picker bonus of 0.11 logit improves picked-map log loss 0.6457 → 0.6443 (in-sample). Pre-veto the picker of map 1 isn't predictable in Bo3 (VLR team1 picks it 46%) but is in Bo5 (70%), so a full map model is deferred. Capped-Kelly rerun (tradeable quotes, in-sample): player_round_glicko raw series+map flat ROI +13.4% [+1.5, +27.0], $50 → $3,622; blended series +9.6%, $50 → $158; blended maps −3.4%. Limits: in-sample parameters; fills at hourly quotes with no depth.

## 2026-10-28 — Prometheus-style Kelly caps in the backtest

Branch `lol-sizing`, base `main`. Returns tables now size like Prometheus's pregame executor (`LOL_SIZING` in `promval/backtest.py`): full Kelly, at most 10% of capital per fixture, $250 per order and per fixture, $1k exposure and $2k per UTC day, all of a day's bets sized from that day's opening capital, nothing once capital is $0; `summarize(..., sizing="full")` keeps the uncapped path. Reports add a series+map row so the fixture cap spans both kinds. Parser now stores `maps.picked_by` (1/2, from VLR's `picked mod-1/2` badge); `PARSER_VERSION` 2. Checks: pytest, ruff.

## 2026-10-28 — Kalshi quotes a bot could trade before the veto

Branch `quote-time`, base `main`. The benchmark priced Kalshi at the last hourly candle before VLR's scheduled start, which can already reflect the veto and late news. Default is now `--quote tradeable`: the first hourly bid/ask ending ≥ 30 min after listing and ≥ 2 h before start with spread ≤ 6¢ (`--max-spread`); `--quote prestart` keeps the old rule. Measured on Feb–Jun 2026 linked markets: 30 min after listing books are empty (median spread 13¢, quarter ≥ 93¢); the tradeable rule covers 83% of markets at a median 40 h before start. Rerun (Feb–Jun 2026, in-sample): Kalshi's early price is much less sharp (series log loss 0.632 vs 0.604 pre-start); player_round_glicko raw vs Kalshi series +0.009, maps −0.003 (not significant), flat ROI +6.7%/+14.9% (intervals include 0), full Kelly still goes broke; blended series −0.006, flat ROI +5.9%, Kelly $50→$77; blended maps worse (+0.011, significant). Checks: pytest (193), ruff.

## 2026-10-28 — Walk-forward market blend; wider RD grid

Branch `blend`, base `main`. `promval/blend.py`: logit p = a·logit(mid) + b·(logit model − logit mid), no intercept, fitted by month on earlier rows only (series and maps separately; ≥100 rows, else mid). Reports add blended log-loss and full-Kelly tables. RD grid widened (rd_new to 600, rd_info to 1.0; chosen 280/0.25, inside). Checks: pytest (192), ruff. Run on VLR from Sep 2025, tuning Feb–Jun 2026 (4,237 maps, in-sample params): player_round_glicko vs Kalshi raw series +0.037 (significant), maps +0.008; blended series +0.003, maps +0.004 (not significant); blended flat ROI series −3%, maps −9%. Blend fits a ≈ 1.06–1.41 (> 1: Kalshi mids underconfident) and b ≈ 0.11 series, 0.52 maps. 113 s wall.

## 2026-10-28 — Player RD, combined variants, Kalshi Kelly backtest

Branch `glicko`, base `main`. Ported Prometheus's player RD (new 280→grid, floor 140, growth 10/√day; moves scale by RD²/floor²), added `player_round_glicko` and `player_round_region_glicko`, and `promval/backtest.py`: after-fee edge against the pre-match hourly ask, full Kelly per match from $50, flat-stake ROI with match bootstrap. Reports now show log loss vs Kalshi and returns by tier. Checks: pytest (188), ruff. Rough run (VLR from Dec 2025; tuning June, in-sample): player_round_glicko maps 0.6389 (v1 0.6614; significant), series 0.6034 (v1 0.6530; significant); vs Kalshi series +0.042, maps +0.009 (not significant); flat ROI ≈ 0%, full Kelly $50 → $0.37. Limits: rd_new and rd_info at grid edges; raw model edges are overconfident.

## 2026-10-28 — Elo variants: margin, round, player, region

Branch `elo-variants`, base `main`. One composable Elo: credit (binary, margin 0.5 + 0.5·tanh(diff/c), round share with an exact first-to-13 map DP and temperature τ), unit (team, or players with the side = starters' mean), and region offsets (host country → Americas/EMEA/Pacific/China; homes from earlier non-international maps; offsets move only on cross-region maps); 12 variants, grids widened after edge hits. Checks: pytest (169), ruff. Rough run (VLR from Feb 2026; tuning = June, 549 maps): player_round 0.6487, player_margin 0.6502, team_round 0.6512, team_margin 0.6521, v1 0.6627; margin and round beat v1 significantly on maps; player ≈ team; region offsets pick the smallest weight (no gain yet). Limits: cold start; rerun on full data.

## 2026-10-28 — Parallel parse and parsed cache

Branch `fast-build`, base `main` (31a140a). Added versioned atomic parsed caches with raw-mtime invalidation, bounded process-pool parsing, configurable jobs, and batched SQLite inserts in numeric match order. Five-match fixture loader timings: original serial 1.135 s; cold jobs=1 0.991 s, cold jobs=8 0.851 s, warm jobs=8 0.023 s (cold jobs=4 0.897 s). All six tables matched exactly across these runs. Tests cover warm-cache parser avoidance, both raw-file mtimes, parser-version invalidation, serial/parallel equality, uncached parse errors, and transaction rollback. Checks: pytest (160 passed, 20.61 s), ruff format/check, and diff whitespace check passed. Used `UV_NO_SYNC=true` because plain uv dependency sync crashes in macOS system configuration. Limit: no 30k-match benchmark; fixture timings include worker startup. Real cache (1,129 matches): cold 93 s with 8 jobs (serial ≈ 0.31 s/match), warm 9 s.

## 2026-10-28 — Elo v1 and benchmark harness

Branch `elo-v1`, base `main` (e5d0f2d). Added `team_elo` (one rating per VLR team, map win = 1, loss = 0, K from a grid by tuning log loss), a coin baseline, chronological replay, Prometheus's scoring and series-clustered bootstrap helpers, series odds from map odds, an opt-in holdout (from 2026-07-01), and a comparison with Kalshi's last hourly pre-match midpoint on linked markets (maps use the model's pre-match chance). Added numpy and pandas. Checks: pytest (152 passed), ruff format/check; `scripts/evaluate_elo.py` ran end to end on a partial DB (VLR crawled back to 2026-06-25: 141 tuning maps), too little data to judge. Limits: rerun after the VLR backfill.

## 2026-10-28 — Kalshi–VLR linking

Branch `kalshi-link`, base `main`. `005_load_kalshi.py` loads the catalog into `kalshi_markets`; `006_link_kalshi.py` links Kalshi series and map events to VLR matches and maps (exact, VLR parenthetical names, learned competitor-UUID aliases, an anchor pass on one confirmed team with a plausible opponent, then fuzzy), and cross-checks settled results. Checks: pytest (142 passed), ruff format/check; on the real catalog with VLR cached from Aug 9 to Oct 27 2026: 288/335 series and 629/724 map events in that window linked (first version: 194/252), 1,840/1,840 settled results agree with VLR. Limits: unlinked are mostly events VLR lacks (Monsters Reloaded qualifier) or academy rosters Kalshi names after the main org ("Natus Vincere" = VLR "Natus Vincere Junior"); see `db/link_report.txt`.

## 2026-10-28 — VLR map order from the map tabs

Branch `vlr-map-order`, base `main` (89aa707). Map order now comes from VLR's numbered map tabs ("1 Ascent"), which follow the veto and play order; the stat sections can be listed differently. Found by the Kalshi–VLR cross-check: all 8 map-result mismatches (3 matches) were maps in the wrong order. Regression fixture 730547. Checks: pytest, ruff format/check.

## 2026-10-28 — VLR event tiers and map pool

Branch `vlr-events`, base `main` (56b502a). Added `promval vlr events` (VLR's event lists by tier: VCT, VCL, T3, GC, collegiate, offseason; refreshable cache), an `events` table with a primary tier, an international flag (VCT/GC/offseason names, qualifiers excluded) and JSON overrides, and map-pool history from seven-map vetoes (`veto_pools`, smoothed `map_pool_periods`, `map_pool` view). Checks: pytest (95 passed), ruff format/check; live crawl: 69 pages, 3,050 events; a DB build on the 403 cached matches joined every match to an event, flagged 30 events international (no T3 "Masters" cups) and found the Aug 2026 Breeze→Abyss pool change. Limits: VLR's VCT tier includes some tier-2 events (China Evolution Series, 2021 Challengers); refine with overrides.

## 2026-10-28 — Scheduled Kalshi collector

Branch `kalshi-schedule`, base `main` (56b502a). Added a sorted, atomic history manifest and local rebuild command, immutable gzip book files per pass, an S3 pull/push helper, and a six-hour GitHub Actions collector that downloads only the manifest, guards missing seeds, and uploads partial progress. Updated offline collector/workflow checks and deployment guidance. Checks: `UV_NO_SYNC=true uv run pytest -q` (72 passed, 3.74 s), ruff format/check and `bash -n scripts/kalshi_data.sh`. Plain `uv run` crashed in macOS system configuration; disabling dependency sync used the existing environment. Limits: workflow not run; secrets/variable not yet set. Actions runtime is estimated until the first live runs; no CI runtime baseline measured.

## 2026-10-28 — Edge comes from the model

Docs only. Recorded the decision that the edge must come from a better rating model (as in Prometheus), not from trading on the veto faster than Kalshi: map prices react to the veto immediately. Removed the veto-window timing task from Future work. Checks: pytest.

## 2026-10-28 — VLR crawler and parsers

Branch `vlr-scraper`, base `main` (156e8f7). Added a polite VLR fetcher (2 s, retries), a permanent gzip raw cache, an incremental results crawl (`--full` walks past cached pages to resume a backfill), pure parsers for results, match and economy pages, and `scripts/setup_db.sh` building `db/valorant.db` (matches, vetoes, maps, rounds, player_maps, economy). Drawn series (1–1 Bo2) store a null winner; the economy tab omits overtime rounds, so economy checks regulation rounds only (regression fixtures 29754, 582286). Checks: pytest (41 passed), ruff format/check; a live sample of 27 matches across 2021–2026 built with 0 parse errors (68 veto steps, every round with side and win type, 70 of 560 player rows without a rating). Limits: backfill not run; no event tiers, team aliases or bo3.gg check yet.

## 2026-10-28 — Kalshi collector

Branch: `kalshi-collector`; base: `main` (`156e8f7`). Added public HTTP pacing/retries/pagination, merged catalogs, atomic final trade/candle files, append-only active books, collector and timed-book CLI commands, and offline fixture tests. Historical-catalog markets use `/historical/trades` and `/historical/markets/{T}/candlesticks`; `/markets` wins overlaps and retains recent endpoints. Empty tapes for positive-volume markets and empty candles report errors without saving files, allowing retries; zero-volume empty tapes are complete. Raw fields are preserved. Updated layout, usage and status docs. Checks: pytest (26 passed), ruff format/check; live `collect --limit 12` saved 2025 historical tapes (20–277 trades) and candles with no errors, and 36 open books. Limits: full backfill not run; not scheduled.

## 2026-10-28 — Repo skeleton

Base: new repo. Created `valorant-model` with Prometheus's conventions: AGENTS.md, steering docs, work-log tooling and hook, steering test (budgets scaled down), ruff config, CI (ruff + pytest), Typer CLI `promval` with empty `kalshi` and `vlr` groups, the design plan PDF, and fixtures: Kalshi API responses and gzipped VLR pages (results pages 1/300/600/1500; matches 773441 Bo3, 654971 and 610432 Bo5, 163803 Bo1 2023, 6805 Bo1 2020, each with its economy tab), fetched 2026-10-28. Checks: `uv run pytest -q`, `uv run ruff format --check`, `uv run ruff check`.
