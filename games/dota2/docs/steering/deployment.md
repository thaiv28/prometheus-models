# Deployment

## CI

`ci.yml` runs Ruff and pytest on pushes and pull requests. All fetchers are injectable and tests are offline.

## Site feed workflows

`refresh-db.yml` runs hourly; `feed.yml` publishes every ten minutes through cron-job.org workflow dispatches on main. Configure those external jobs after deployment. GitHub schedules (`41 * * * *` and `7 * * * *`) are hourly backups; both workflows also accept manual dispatch and serialize without cancellation. Workflows have not run on GitHub yet; runner times and cron-job.org setup remain unverified.

Refresh restores raw caches or tries the cold seed `dota2-model/seed/raw.tar.zst`, then tops up S3 caches. Liquipedia uses `--listing none` hourly, `--listing full` during the 03:xx UTC run. OpenDota bulk refresh covers the current month and two preceding months. With an API key, rebuild then fetch missing games (`--limit 1800`) and rebuild again; without a key, skip single-game top-ups to preserve the daily free budget. Raw caches and weekly seed exclude Kalshi books. Cache database inputs by sorted content hashes plus scripts, package and lockfile. An exact DB-cache hit and matching published state `inputs` metadata skip rebuild and snapshots. Rehash after game enrichment before saving DB cache and state metadata.

Refresh builds `feed-state` and the blend artifact and uploads both. Feed downloads the trusted ratings state, prediction log and upcoming snapshot, exports without a DB, uploads public compressed JSON and private candidates, persists upcoming responses and conditionally saves predictions by ETag. A missing state fails with instructions to run refresh first. Conditional writes skip a concurrently changed prediction log.

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

Planning estimate: 720 refreshes/month × 3–10 minutes plus 4,320 exports × 0.5–1 minute ≈ 4,320–11,520 Actions minutes/month, before cache savings and included quotas. S3 is storage plus small GET/PUT/transfer charges, likely dollars/month at this cache size; measure after deployment. OpenDota paid single-game ceiling is 1,800/hour × $0.01/100 ≈ $129.60/month; completed games are cached, so actual top-ups should be much lower. No live workflow cost has been measured.
