# Current state

## Status

Playbook phase: **6 (trading wiring)**. 2026-10-30: the holdout gate failed narrowly; the user overrode it on the significant log-loss edge, so Phase 6 proceeds with Dota disabled in execution (candidate-only). Holdout opened once 2026-10-30: adopted `player_glicko_rw_tier_revert` + `form` beats Kalshi on series log loss (blended −0.0290, significant, every month), but the gate, blended depth-capped series flat ROI, is +14.5% [−0.4, +31.4].  Stage-2 looks: 2. Data: 45,645 series, 91,503 games (84,091 with players); Kalshi links series 1,380/1,870.

Site feed, private series candidates, frozen blend artifact and scheduled workflows are implemented, not yet deployed. Snapshots score the adopted model with its fitted form layer. Dota remains disabled in Prometheus execution.

## Known limits

- Liquipedia terms do not address betting/trading use.
- OpenDota's bulk explorer is thin from June 2026; per-game top-ups are rate-limited.
- Games without OpenDota data have no players.
- Players are keyed by Steam account; roster names are only for display.

## Future work

1. Deploy and seed feed workflows, configure cron-job.org dispatches, and measure runner costs.
2. Inspect live feed coverage and candidates before considering execution enablement.
