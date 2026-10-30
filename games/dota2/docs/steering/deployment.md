# Deployment

## CI

`ci.yml` runs Ruff and pytest on pushes and pull requests. All fetchers are injectable and tests are offline.

## Site feed workflows

Configure cron-job.org dispatches on main: feed every 15 minutes, refresh every 3 hours. GitHub backups are `37 * * * *` and `41 */6 * * *`; both accept manual dispatch and serialize without cancellation. Feed times out after 10 minutes; refresh after 45. External setup and live GitHub timings remain unverified.

Refresh restores raw caches or the cold seed, then tops up S3. Liquipedia uses `--listing none`, except full listings during 03:00–05:59 UTC. OpenDota bulk covers three months; keyed runs fetch missing games (limit 1,800) between rebuilds. Raw caches/seeds exclude books. Sorted input hashes plus code/lockfile key the DB cache; matching published `inputs` metadata skips rebuild and snapshots. Rehash after enrichment.

Feed's sparse checkout runs a stdlib gate before uv installation. Cached page revision IDs and open Kalshi event tickers detect changes; passed starts, request failures, missing state, or two hours since export force a run. Successful candidate publication advances `last_export_at`, leaving an hour below Prometheus's three-hour candidate age limit. Full runs restore ratings/predictions, export without a DB, and persist the upcoming snapshot. Missing ratings fail. SHA-256 S3 metadata skips identical uploads; deterministic feed gzip supports comparison. Prediction saves retain ETag concurrency checks. Dispatch Prometheus only when the public feed hash changes. uv caches use `uv.lock`; production installs exclude dev dependencies.

## Credentials and storage

Set secret `AWS_ROLE_ARN` for GitHub OIDC and repository variable `DATA_BACKUP_BUCKET`; region is `us-west-2`. Optional secret `OPENDOTA_API_KEY` enables per-game top-ups. Optional `PROMETHEUS_DISPATCH_TOKEN` dispatches `thaiv28/Prometheus`'s `games.yml`; missing tokens skip dispatch and dispatch failures do not fail publication. No long-lived AWS keys are needed.

S3 objects under `dota2-model/`:

- `feed/state.pkl.gz`: trusted internal replay snapshot, with input-hash metadata.
- `feed/predictions.json`: frozen prediction log.
- `feed/dota2.json.gz`: public Prometheus feed, JSON content type.
- `feed/candidates.json`: private execution candidates; Dota is disabled in Prometheus execution.
- `feed/blend_artifact.json`: frozen monthly coefficients.
- `feed/upcoming/`: current Liquipedia revision responses.
- `liquipedia/`, `opendota/`, `kalshi/`: raw caches.
- `seed/raw.tar.zst`: cold-start raw archive, refreshed when missing or older than seven days after successful raw-cache save.

Syncs never delete remote objects. Keep candidates, state and raw inputs private; Prometheus publishes only the public feed.

## Kalshi collection

`kalshi-collect.yml` runs every six hours (`23 */6 * * *`) or manually, on main, with a 30-minute timeout. It downloads `kalshi/manifest.json`; missing manifest fails unless dispatch sets `allow_full=true`. It uploads partial progress even after collection failure. Seed a completed local archive using `promdota kalshi manifest` and `scripts/kalshi_data.sh push`; `pull` restores it. These commands are operator actions, not run during implementation.

## Cost

The repo is public (since 2026-10-30), so standard-runner Actions minutes are free; the rules still apply for Liquipedia/OpenDota politeness and the CI time budget. Method if it ever goes private: runs/month × billed minutes/run, each job rounded up to a whole minute.

Runs per 30 days: feed 2,880 cron-job.org dispatches (15 min) + 720 hourly backups; refresh 240 (3 h) + 120 backups (6 h); Kalshi collection 120. Duplicates are cheap: the feed gate and the refresh input hash skip unchanged work.

Measured locally 2026-10-30 (live APIs): cold export 220 s with 64 Liquipedia page fetches; warm export 4.2 s with 0 fetches (one revisions request per 50 pages); unchanged gate 3 s, then the run stops before `uv sync`. GitHub run timings are unmeasured. S3 requests/storage and OpenDota calls ($0.01 per 100) are billed separately.
