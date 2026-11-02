# r6-model

A pre-match trading model for Rainbow Six Siege esports: player-based map Elo, priced against Kalshi's R6 series and map-winner markets.
Agent guidance is in [AGENTS.md](AGENTS.md); project status and design live in `docs/steering/`.

```bash
uv sync
uv run pytest -q
uv run promr6 --help
```

Results source: Liquipedia, licensed under CC BY-SA 3.0. Rosters: siege.gg.
