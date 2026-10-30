# Current state

## Status

Playbook phase: **live** (2026-10-30 19:54 UTC). The user overrode the narrowly failed holdout gate and, after the cron-job.org jobs were confirmed firing, skipped the week-long candidate-only run: Prometheus execution has `dota2` enabled with a $50 starting bankroll (`ACCOUNT#dota2`), series markets only. Adopted model: `player_glicko_rw_tier_revert` + `form` (holdout blended series −0.0290 vs Kalshi; depth-capped flat ROI +14.5% [−0.4, +31.4]). Schedules: cron-job.org feed every 15 min, refresh-db every 3 h (UTC), GitHub backups hourly / 6-hourly. Data: 45,684 series, 91,550 games.

## Known limits

- Liquipedia terms do not address betting/trading use.
- OpenDota's bulk explorer is thin from June 2026; per-game top-ups are rate-limited.
- Games without OpenDota data have no players.
- Players are keyed by Steam account; roster names are only for display.

## Future work

1. Deploy and seed feed workflows, configure cron-job.org dispatches, and measure runner costs.
2. Inspect live feed coverage and candidates before considering execution enablement.
