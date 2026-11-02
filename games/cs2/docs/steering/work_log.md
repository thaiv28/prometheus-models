# Work log

## 2026-11-02 — refresh-db fails loudly; runner timings after the speed-up

A Liquipedia 429 on the first listing request crashed the crawl, and `| tee` without pipefail hid it: the run passed and rebuilt from cached pages. refresh-db now runs bash with pipefail; a failed crawl posts a warning and builds from cached pages; Kaggle's fallback warning now fires. Runner timings after the crawl/link speed-up (run of 22:41 UTC): crawl 48 s (was ~250 s), linking ~67 s (was ~190 s), whole run 5.2 min (was ~10). Checks: actionlint, pytest, ruff.

## 2026-11-02 — Feed gate before install

Added a stdlib pre-install gate and revision-aware versioned upcoming snapshot with match starts. Unchanged runs skip install/export/publication/dispatch; state ETag changes force export, marked only after uploads. Existing page scope, pricing and feed/candidate schema remain unchanged. Checks: full pytest, ruff format/check, system-python gate help, actionlint, work-log rotation and four differential cases against the original exporter (cold/warm/live, with Kalshi quotes) passed with byte-identical feed, candidates and predictions. Live runner savings remain unmeasured; warm fixtures use one revision probe and no content fetch.

## 2026-11-02 — CI: shared setup, one Kalshi workflow, actionlint, dispatch on change

Scheduled jobs use the shared setup-game composite with uv download caching; Kalshi collection uses one matrix with independent game concurrency and unchanged S3 prefixes. Feeds store content-sha256 metadata excluding the top-level generated timestamp and dispatch Prometheus only on content changes; Dota retains byte-hash upload skips and its early gate. CI runs actionlint for .github changes while preserving game scoping. Checks passed: actionlint 1.7.12; full pytest; ruff format/check; eight CI-scope and fifteen mocked feed-upload scenarios; work-log rotation. Plain uv triggers a macOS configuration panic, so checks use UV_OFFLINE=1 UV_NO_SYNC=1.

## 2026-11-02 — Moved Liquipedia pages no longer break the DB build

`refresh-db` failed from 17:35 UTC on `UNIQUE constraint failed: events.event_id`: Liquipedia moved `Kleverr/A Lyga/…` to `Esporto A Lyga/…`, so four page ids were cached under both titles. `002_load_liquipedia.py` now keeps each page id's newest revision (`latest_titles`) and logs `moved=`. Checks: new test fails before the fix and passes after; real S3 cache: pages=4742 moved=4 events=4738 parse_errors=0; pytest, ruff.

## 2026-11-02 — Workflows run from prometheus-models

Scheduled workflows moved to root `.github/workflows/cs2-{feed,kalshi-collect,refresh-db}.yml` with working directory `games/cs2`, game-prefixed concurrency groups and repo-root cache/hash paths. Raw cache keys are game-prefixed; S3 prefixes are unchanged. Per-game ci.yml is replaced by root CI, which scopes game workflow changes to that game. Checks with `UV_OFFLINE=1 UV_NO_SYNC=1`: `uv run --frozen pytest -q` (363 passed), `uv run ruff format --check .` and `uv run ruff check .` passed. Root `python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('.github/workflows/*.yml')]"` passed; directory layout and six CI classification scenarios passed. `python3 scripts/work_log.py rotate` passed. Plain uv hit a macOS configuration panic; sandbox blocked git mv's index lock, so files were moved on disk.

## 2026-11-02 — Moved into prometheus-models

Imported with full history into `prometheus-models/games/cs2/` (branch `main`, base: this repo's local `main` merged with `origin/main`; unpushed `player-stats` merge kept). `tests/test_steering.py` now finds the git repo from a subfolder and checks only this game's paths; the work-log hook moved to the repo root and the CI to a root workflow that checks only changed games. Production workflows still run from the old repo until cutover. Checks: steering guard fails without this entry and passes with it; full pytest and ruff from `games/cs2/`.

## 2026-11-02 — refresh-db: faster crawl and Kalshi linking

CI refresh-db took ~10 min hourly: crawl ~250 s, Kalshi linking ~190 s. The crawler now reads category members' revids from the category listing (500 per request) instead of ~95 batched revision queries; linking caches its pure string helpers (`normalize`, `_variants`, `_similar`). Checks: link tables, aliases and `link_report.txt` byte-identical before/after; local link 190 s → 28 s; real steady-state crawl 48 s (listed=4561, unchanged=4736, missing=363, as before); pytest, ruff. Runner timings to confirm after merge.

## 2026-10-30 — feed: pipefail on the export step

Branch `pipefail`, base `origin/main`. The export step piped through `tee` under the default `bash -e`, so a crashed export passed and the upload step failed instead. The step now uses `shell: bash` (pipefail). Checks: full pytest, ruff, YAML parse.

## 2026-10-30 — feed: cached schedule when Liquipedia rate-limits

Branch `liquipedia-429`, base `origin/main`. About 2 of 15 Site feed runs failed with Liquipedia `HTTP 429` after the fetcher's 75 s of retries. `promcs export` now falls back to the last raw snapshot (`upcoming/latest.json.gz`, restored from S3) on a URL/timeout error; the summary reports `liquipedia_stale=1`. A missing snapshot still fails. Checks: new feed test, full pytest, ruff.

## 2026-10-29 — refresh-db: fresh AWS login before uploads

Branch `game-candidates`, base `main`. A long Valorant rebuild outlasted the hour-long OIDC session and its snapshot upload failed with `ExpiredToken`; this workflow now logs in to AWS again before the snapshot and artifact uploads too. Checks: workflow tests, YAML parse.

## 2026-10-29 — refresh-db: no Liquipedia S3 listing on a cache hit

Branch `game-candidates`, base `main`. The Liquipedia `aws s3 sync` from S3 now runs only on a raw-cache miss (only this workflow writes those objects, so a restored cache is current); Kalshi data, written by the collector, still syncs every run. Matches valorant-model, where the same listing took 7.5 min. Checks: workflow tests, YAML parse.
