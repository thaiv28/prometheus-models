# Work log

## 2026-11-02 — refresh-db: faster crawl and Kalshi linking

CI refresh-db took ~10 min hourly: crawl ~250 s, Kalshi linking ~190 s. The crawler now reads category members' revids from the category listing (500 per request) instead of ~95 batched revision queries; linking caches its pure string helpers (`normalize`, `_variants`, `_similar`). Checks: link tables, aliases and `link_report.txt` byte-identical before/after; local link 190 s → 28 s; real steady-state crawl 48 s (listed=4561, unchanged=4736, missing=363, as before); pytest, ruff. Runner timings to confirm after merge.

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
