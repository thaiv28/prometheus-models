# Work log

Newest first. Each entry: what changed, checks run, remaining limits. At most 150 words.

## 2026-10-29 — Player identity splits

Branch `player-stats`, base `f22f6ef`. Bare Liquipedia keys move to a unique disambiguated sibling seen on the same team within 365 days (8,729 map/roster rows, 60 players; e.g. lucky → lucky (french player)). Kaggle sides pair unmatched slots with similarly spelled roster players (containment, same-initial subsequence, or difflib ≥0.6), fall back to a unique existing player by team then globally, and unify each Kaggle ID onto one player. New Kaggle players 31→3 (ruggah, gatsby: not in Liquipedia; nbl: two Liquipedia players); split Kaggle IDs 16→5, only on retained conflicting sides. Adopted model vs f22f6ef DB: stage 1 +0.00003 (n.s.; tier1 −0.0010 significant, tier3 +0.00016 significant, within +0.0005), stage 2 −0.00017 (n.s.). Checks: pytest 345 (11.3 s), ruff, rebuild; foreign keys clean, all game IDs kept.

## 2026-10-29 — Team aliases and Kaggle lineups (data fix)

Branch `player-stats`, base `837e570`. Loader resolves template keys to roster cards (navi→Natus Vincere; 102 aliases) and merges split teams (534 keys → 259; parenthetical qualifiers stay apart); match/map IDs unchanged. Kaggle-linked maps use actual lineups: 17,295 sides, 617 changed (stand-ins), 31 new players; spelling variants (device/dev1ce) map to existing players. Teams 7,781→7,345; 2024+ matches with full rosters 42,817→48,764; Kalshi links series 5,138→5,389, maps 9,131→9,568. Adopted model, new vs old DB: stage 1 −0.0012 [−0.0017, −0.0007], stage 2 −0.0013 [−0.0022, −0.0004]; raw series vs Kalshi −0.0054 (was −0.0041). Perf bonus retest still n.s. `docs/elo_backtest.md`, series temperatures refreshed. Checks: pytest 328, ruff, rebuild 132 s. Limit: a few variants (baz/baaaaZzz) still split.

## 2026-10-29 — Kaggle player stats; performance bonus rejected

Branch `player-stats`, base `main` (7446fb5). `promcs kaggle fetch` caches the weekly ektarr/counter-strike-pro-matches zip (CC BY-SA 4.0); `006_load_kaggle.py` links map rows (times UTC+3) to Liquipedia by map, score, ±12 h, and per-side agreement (≥3 nicknames or team name incl. Kalshi aliases) into `kaggle_links`/`player_stats`: 8,942/12,322 linked (72.6%), 68,680 player rows; 15 sampled weak links all correct. Off-by-default zero-sum bonus perf_k·(stat − side mean), KDA and ADR variants. Benchmark: stage 1 KDA −0.00006, ADR −0.00011 (n.s.); on maps with stats −0.0005/−0.0007 (n.s.); stage 2 n.s. Rejected; left off. Checks: pytest 283 → 314 (40.3 s → 12.4 s, timing noise), ruff, benchmark (5.5 min). Codex wrote most code.

## 2026-10-29 — Actions site feed snapshots

Branch `game-feed`, base phase-1 `f31f2fe`. Split DB/candle replay into a versioned gzip-pickle snapshot; export accepts it without SQLite. Added hourly refresh and frequent feed workflows with OIDC, raw caches, conditional prediction-log persistence and optional Prometheus dispatch. S3: `cs2-model/{liquipedia/,kalshi/,feed/{state.pkl.gz,predictions.json,cs2.json.gz,upcoming/}}`. Checks: 261 tests passed/12.93 s (phase-1: 255/14.99 s; six added guards); ruff format/check, bash syntax and normalized feed cmp passed. Offline state: 6,164,779 bytes/7.84 s; export 0.44 s versus DB 8.47 s. Used UV_NO_SYNC/UV_OFFLINE for uv’s local macOS panic. Limits: workflows not yet run on GitHub; runner times unmeasured; raw caches must be seeded in S3 once. No network or commits. Merged main: the feed replays the adopted `player_round_glicko_rookie_weights`; `evaluate_elo.py --write-weights` (report to scratch; docs/elo_backtest.md unchanged) reproduced its parameters and stored stage-1 series temperatures Bo3 0.86, Bo5 0.68.

## 2026-10-29 — Prometheus game feed

Branch `game-feed`, base `main`. Added `promcs export`: upcoming/live calls, replayed results, current Kalshi series mids and cached prestart closes. Stored existing stage-1 weights; benchmark exports string-keyed series temperatures. Calls refresh until their saved start, then freeze; results consume closest team-pair calls once, correcting orientation. Nine offline tests cover scheduling, lifecycle, joins, batching, pagination and prices. Checks: existing suite 246 passed/13.13 s; added feed tests 9 passed/0.23 s; combined 255 passed/14.99 s (+1.86 s versus baseline); ruff format/check and diff check passed. Used `UV_NO_SYNC=1` for uv's sandbox macOS panic. Real offline export: 15,538 finals, 4,774 priced, 8.30 s; 6,280,217 bytes. Limits: ratings only as fresh as last crawl + setup_db; tournaments not yet in DB are not scanned for upcoming matches; TBD sides omitted. No network or commits.

## 2026-10-29 — Pin adopted model; regional retest

Branch `pin-adopted`, base `main` (4d7fa70). Pinned `player_round_glicko_rookie_weights` (rookie 200/400, tier-3 K 0.75) as `models.ADOPTED`; new `--baseline` (default ADOPTED) adds candidate − baseline paired tables by section in both stages; existing benchmark tests pass `--baseline team_elo`. Regional layer over the adopted model rejected: stage-2 maps −0.00044 (significant, below 0.0005), Kalshi blended unchanged (ledger). Run: 453 s for three models × two layers. Holdout not opened: no maps on or after 2026-11-01. Checks: ruff, `uv run pytest -q`.

## 2026-10-29 — Pinned base grid

Branch `bench-speed`, base `elo-candidates` (0cdba0a). `player_round_glicko` now scores its stage-1 winner (`models.PINNED`: K=32, τ=0.5, rd_new=350, info=0.125, teammates) instead of re-searching 640 combinations every run; `--full-grid` restores the search, and `--k-grid` still overrides K. Two-model run (`team_elo,player_round_glicko`) 517 s → 214 s with identical stage-2 results. Candidate verdicts in the ledger: rookie 200/400 + tier-3 K 0.75 adopted (stage 2 −0.0068 maps); calibration, online K, tier moves rejected; regional pending intervals. S3 seeded (82,216 objects). Checks: ruff, `uv run pytest -q` (267 passed).

## 2026-10-29 — CS2 Elo candidates

Branch `elo-candidates`, base `main` (0807b8c). Added tier×LAN calibration and online/tier3 K weighting candidates; anchored rookie/moves grids to the base stage-1 parameters. Replay carries online metadata; offline tests cover calibration, thresholds, neutral multipliers, compounded updates and invalid inputs. Checks: pytest 266 passed/12.56 s; 18 new calibration/multiplier cases 0.29 s (clean before-change timing unavailable); ruff format/check, CLI help, registry listing and diff check passed. Used `UV_NO_SYNC=1 UV_OFFLINE=1`: plain uv panics in macOS configuration. Updated the evaluation fixture for online metadata. Limit: benchmark run pending (run by reviewer). No weights or benchmark report written.

## 2026-10-29 — Full Kalshi backfill and validation

Branch `full-bench`, base `main` (c8a3138). Backfill finished (KXCS2GAME 15,815, KXCS2MAP 25,730 markets; 106 fetch errors left for the scheduled collector). Rebuilt DB: series links 5,138/7,907, map links 9,131/12,865, results agree 28,362/28,396. Benchmark (517 s): player_round_glicko blended series −0.0118 vs Kalshi (significant), raw +0.0003; maps n.s.; blended series flat ROI +8.0% [+3.7, +12.2]. Committed `docs/elo_backtest.md`; ledger updated. S3 seeding pending (AWS SSO expired). Checks: `uv run pytest -q`.

## 2026-10-29 — First Kalshi validation (preliminary)

Branch `ledger`, base `main` (4f689df). Ran `evaluate_elo.py --models team_elo,player_round_glicko --layers none` (320 s) with the Kalshi backfill ~40% done: player_round_glicko raw +0.0014 (n.s.), blended −0.0105 (significant) vs Kalshi's tradeable quote on 1,876 series; recorded in the research ledger. `docs/elo_backtest.md` not committed until the backfill completes. Checks: `uv run pytest -q`.

## 2026-10-29 — Benchmark reads Liquipedia alias column

Branch `alias-col`, base `main` (491154a). The parallel ratings and linking branches disagreed: `evaluate_elo.py` read `team_aliases.vlr_team_id`, which the CS2 link step names `liquipedia_team_id`; the Kalshi stage crashed. Renamed in the benchmark and its test. Checks: `uv run pytest -q`, ruff format/check.
