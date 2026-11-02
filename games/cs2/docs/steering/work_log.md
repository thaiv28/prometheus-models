# Work log

## 2026-11-02 — Moved Liquipedia pages no longer break the DB build

`refresh-db` failed from 17:35 UTC on `UNIQUE constraint failed: events.event_id`: Liquipedia moved `Kleverr/A Lyga/…` to `Esporto A Lyga/…`, so four page ids were cached under both titles. `002_load_liquipedia.py` now keeps each page id's newest revision (`latest_titles`) and logs `moved=`. Checks: new test fails before the fix and passes after; real S3 cache: pages=4742 moved=4 events=4738 parse_errors=0; pytest, ruff.

## 2026-11-02 — Workflows run from prometheus-models

Scheduled workflows moved to root `.github/workflows/cs2-{feed,kalshi-collect,refresh-db}.yml` with working directory `games/cs2`, game-prefixed concurrency groups and repo-root cache/hash paths. Raw cache keys are game-prefixed; S3 prefixes are unchanged. Per-game ci.yml is replaced by root CI, which scopes game workflow changes to that game. Checks with `UV_OFFLINE=1 UV_NO_SYNC=1`: `uv run --frozen pytest -q` (363 passed), `uv run ruff format --check .` and `uv run ruff check .` passed. Root `python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('.github/workflows/*.yml')]"` passed; directory layout and six CI classification scenarios passed. `python3 scripts/work_log.py rotate` passed. Plain uv hit a macOS configuration panic; sandbox blocked git mv's index lock, so files were moved on disk.

## 2026-11-02 — Moved into prometheus-models

Imported with full history into `prometheus-models/games/cs2/` (branch `main`, base: this repo's local `main` merged with `origin/main`; unpushed `player-stats` merge kept). `tests/test_steering.py` now finds the git repo from a subfolder and checks only this game's paths; the work-log hook moved to the repo root and the CI to a root workflow that checks only changed games. Production workflows still run from the old repo until cutover. Checks: steering guard fails without this entry and passes with it; full pytest and ruff from `games/cs2/`.

## 2026-10-30 — feed: pipefail on the export step

Branch `pipefail`, base `origin/main`. The export step piped through `tee` under the default `bash -e`, so a crashed export passed and the upload step failed instead. The step now uses `shell: bash` (pipefail). Checks: full pytest, ruff, YAML parse.

## 2026-10-30 — feed: cached schedule when Liquipedia rate-limits

Branch `liquipedia-429`, base `origin/main`. About 2 of 15 Site feed runs failed with Liquipedia `HTTP 429` after the fetcher's 75 s of retries. `promcs export` now falls back to the last raw snapshot (`upcoming/latest.json.gz`, restored from S3) on a URL/timeout error; the summary reports `liquipedia_stale=1`. A missing snapshot still fails. Checks: new feed test, full pytest, ruff.

## 2026-10-29 — refresh-db: fresh AWS login before uploads

Branch `game-candidates`, base `main`. A long Valorant rebuild outlasted the hour-long OIDC session and its snapshot upload failed with `ExpiredToken`; this workflow now logs in to AWS again before the snapshot and artifact uploads too. Checks: workflow tests, YAML parse.

## 2026-10-29 — refresh-db: no Liquipedia S3 listing on a cache hit

Branch `game-candidates`, base `main`. The Liquipedia `aws s3 sync` from S3 now runs only on a raw-cache miss (only this workflow writes those objects, so a restored cache is current); Kalshi data, written by the collector, still syncs every run. Matches valorant-model, where the same listing took 7.5 min. Checks: workflow tests, YAML parse.

## 2026-10-29 — Refresh speed (requested branch `refresh-speed`, base `main`)

Added an exact input-hash DB cache and state `inputs` metadata check: unchanged hours skip rebuilds and snapshots. Cold raw-cache misses try `cs2-model/seed/raw.tar.zst` before sync; successful raw-cache saves refresh missing or week-old seeds. Rebuilds publish the walk-forward artifact to `cs2-model/feed/blend_artifact.json` for Prometheus. Raw saves precede DB builds; summaries report cache results, crawl, build seconds and snapshot count. Added offline workflow safeguards.

Checks: 300 pytest tests passed with offline/no-sync uv; Ruff format/check passed. System PyYAML parse, nine shell syntax checks and four skip-check cases passed. Requested uvx validation was blocked by sandbox/uv failure. Runner timings and CI before/after durations must be measured after merge. Sandbox blocked the requested git fetch/branch setup; no commit made.

Newest first. Each entry: what changed, checks run, remaining limits. At most 150 words. The DB cache key hashes file contents (not sizes), so a same-size page revision still rebuilds. Workflow tests updated for the content hash.

## 2026-10-29 — Execution inputs

Branch `game-candidates`, base `main`. Added frozen `promcs/blend_artifact.json`, private atomic candidates with Kalshi rules names/start checks and raw series provenance; shared benchmark helpers are unchanged. Feed uploads `cs2-model/feed/candidates.json` for Prometheus's Lambda. Real artifact: 8 snapshots; latest a=1.243027236, b=0.653439642, n=4136. Checks: pytest 297 passed/15.06 s versus 283 existing tests/13.60 s (+1.46 s locally); 14 new tests alone 0.18 s; ruff format/check, diff check and helper syntax-tree equality passed. Artifact, feed-state (8.33 s) and snapshot no-fetch export (0.42 s, candidates=0, skipped_candidates=0) passed. Used UV_NO_SYNC/UV_OFFLINE after plain uv's macOS panic. Limits: GitHub/S3/Lambda execution and runner timings unverified. No network or commits.

## 2026-10-29 — Kaggle fetch in refresh-db

Branch `player-stats`, base `9466aea`. `promcs kaggle fetch` now checks at most once per UTC day (`last_checked` marker) and stores a new dated zip only when the bytes changed (the dataset updates weekly). refresh-db syncs `cs2-model/kaggle/` from S3, fetches, syncs back, then rebuilds; a failed download warns and uses the cached archive. Checks: pytest 345, ruff, workflow YAML parse (ruby). Limits: not yet run on GitHub; Kaggle's anonymous download from runners is unverified; seed S3 with `aws s3 sync data/kaggle s3://$BUCKET/cs2-model/kaggle`.

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
