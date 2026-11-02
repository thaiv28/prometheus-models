# Deployment

## CI

Root `.github/workflows/ci.yml` runs Ruff and pytest for `games/r6` when its files change. Tests are offline.

## Credentials and storage

No secrets of its own yet. The repo's `AWS_ROLE_ARN`, `DATA_BACKUP_BUCKET` and `PROMETHEUS_DISPATCH_TOKEN` cover it; it writes only under `r6-model/` in the artifacts bucket.

## Cost

No scheduled workflows yet.
