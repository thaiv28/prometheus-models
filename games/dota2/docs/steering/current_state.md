# Current state

## Status

Playbook phase: **5 (holdout verdict)**. Adopted 2026-10-30: `player_glicko_rw_tier_revert` + `form` layer (rookie 600/800, online and tier-3 K 0.75, tier-target reversion 0.1 each October). Stage 2 vs Kalshi: blended series −0.0080 n.s., flat +12.1% [−5.7, +32.0]. Ladder done; trade set: series markets, all tiers. Stage-2 looks: 2. Data: 45,645 series, 91,503 games (84,091 with players); Kalshi links series 1,380/1,870.

## Known limits

- Liquipedia terms do not address betting/trading use.
- OpenDota's bulk explorer is thin from June 2026; per-game top-ups are rate-limited.
- Games without OpenDota data have no players.
- Players are keyed by Steam account; roster names are only for display.

## Future work

1. Run the real Phase 2 crawl and inspect coverage, orphans, winner conflicts and links.
2. Build the real DB, run stage 1 team Elo vs player Glicko, pin its winner, then validate on stage 2 before opening holdout.
