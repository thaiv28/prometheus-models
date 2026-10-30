# Current state

## Status

Playbook phase: **3 (baseline)**, waiting on data. 2026-10-29: 45,645 series and 91,503 games built from Liquipedia + OpenDota; Kalshi links series 1,380/1,869, games 1,882/2,564. OpenDota per-game top-up (~15,000 games without players, 1,800/day free) started 2026-10-29, newest first; ~8 days. Stage-1 baseline on partial data: player_glicko 0.6294 vs team_elo 0.6501 game log loss (ledger). No stage-2 look yet: the first waits for the top-up and the Kalshi backfill.

## Known limits

- Liquipedia terms do not address betting/trading use.
- OpenDota's bulk explorer is thin from June 2026; per-game top-ups are rate-limited.
- Games without OpenDota data have no players.
- Players are keyed by Steam account; roster names are only for display.

## Future work

1. Run the real Phase 2 crawl and inspect coverage, orphans, winner conflicts and links.
2. Build the real DB, run stage 1 team Elo vs player Glicko, pin its winner, then validate on stage 2 before opening holdout.
