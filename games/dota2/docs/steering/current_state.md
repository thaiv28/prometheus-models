# Current state

## Status

Playbook phase: **4 (refinement ladder)**. 2026-10-30: 45,645 series, 91,503 games (84,091 with players). Kalshi links: series 1,380/1,870, games 1,882/2,564. Base pinned: player_glicko (k 24, rd_new 280, rd_info 0.0625, fixed); stage-2 look 1 is level with Kalshi (ledger). Stage-2 looks: 1.

## Known limits

- Liquipedia terms do not address betting/trading use.
- OpenDota's bulk explorer is thin from June 2026; per-game top-ups are rate-limited.
- Games without OpenDota data have no players.
- Players are keyed by Steam account; roster names are only for display.

## Future work

1. Run the real Phase 2 crawl and inspect coverage, orphans, winner conflicts and links.
2. Build the real DB, run stage 1 team Elo vs player Glicko, pin its winner, then validate on stage 2 before opening holdout.
