# Work log

## 2026-11-02 — CI: shared setup, one Kalshi workflow, actionlint, dispatch on change

Scheduled jobs use the shared setup-game composite with uv download caching; Kalshi collection uses one matrix with independent game concurrency and unchanged S3 prefixes. Feeds store content-sha256 metadata excluding the top-level generated timestamp and dispatch Prometheus only on content changes; Dota retains byte-hash upload skips and its early gate. CI runs actionlint for .github changes while preserving game scoping. Checks passed: actionlint 1.7.12; full pytest; ruff format/check; eight CI-scope and fifteen mocked feed-upload scenarios; work-log rotation. Plain uv triggers a macOS configuration panic, so checks use UV_OFFLINE=1 UV_NO_SYNC=1.

## 2026-11-02 — Workflows run from prometheus-models

Scheduled workflows moved to root `.github/workflows/dota2-{feed,kalshi-collect,refresh-db}.yml` with working directory `games/dota2`, game-prefixed concurrency groups and repo-root cache/hash paths. Raw cache keys are game-prefixed; S3 prefixes are unchanged. Per-game ci.yml is replaced by root CI, which scopes game workflow changes to that game. Checks with `UV_OFFLINE=1 UV_NO_SYNC=1`: `uv run --frozen pytest -q` (380 passed), `uv run ruff format --check .` and `uv run ruff check .` passed. Root `python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('.github/workflows/*.yml')]"` passed; directory layout and six CI classification scenarios passed. `python3 scripts/work_log.py rotate` passed. Plain uv hit a macOS configuration panic; sandbox blocked git mv's index lock, so files were moved on disk.

## 2026-11-02 — Moved into prometheus-models

Imported with full history into `prometheus-models/games/dota2/` (branch `main`, base: this repo's local `main` merged with `origin/main`). `tests/test_steering.py` now finds the git repo from a subfolder and checks only this game's paths; the work-log hook moved to the repo root and the CI to a root workflow that checks only changed games. Production workflows still run from the old repo until cutover. Checks: steering guard fails without this entry and passes with it; full pytest and ruff from `games/dota2/`.

## 2026-10-30 — feed: cached schedule when Liquipedia rate-limits

Branch `liquipedia-429`, base `origin/main`. Site feed run 41124259738 hit Liquipedia `HTTP 429` past the fetcher's retries; `| tee` without pipefail hid the crash until the upload step. `promdota export` now reuses the last snapshot on a URL/timeout error (snapshot left unchanged, summary `liquipedia_stale=1`; no snapshot still fails), and the export step runs with `shell: bash` (pipefail). Same fix as cs2-model. Checks: new feed test, full pytest, ruff, YAML parse.

## 2026-10-30 — Live

cron-job.org jobs confirmed: feed dispatched 19:49 UTC (run 39 s, candidates refreshed), refresh-db fired once at 19:52 via a temporary schedule, then restored to every 3 h. Prometheus execution: mode off → `games` gains `dota2` ($50; cs2/valorant unchanged) → live at 19:54 UTC; deployed Lambda source hash matches Prometheus main. Docs only.

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
