# Current state

## Status

Playbook phase: **6 (trading wiring)**. 2026-10-30: the holdout gate failed narrowly; the user overrode it on the significant log-loss edge, so Phase 6 proceeds with Dota disabled in execution (candidate-only). Holdout opened once 2026-10-30: adopted `player_glicko_rw_tier_revert` + `form` beats Kalshi on series log loss (blended −0.0290, significant, every month), but the gate, blended depth-capped series flat ROI, is +14.5% [−0.4, +31.4].  Stage-2 looks: 2. Data: 45,645 series, 91,503 games (84,091 with players); Kalshi links series 1,380/1,870.

## Known limits

- Liquipedia terms do not address betting/trading use.
- OpenDota's bulk explorer is thin from June 2026; per-game top-ups are rate-limited.
- Games without OpenDota data have no players.
- Players are keyed by Steam account; roster names are only for display.

## Future work

1. Run the real Phase 2 crawl and inspect coverage, orphans, winner conflicts and links.
2. Build the real DB, run stage 1 team Elo vs player Glicko, pin its winner, then validate on stage 2 before opening holdout.
