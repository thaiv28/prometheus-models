# AGENTS.md

Guidance for AI coding agents (and humans) working in this repo.

## Read before work

Read only what your change touches. If a task names files and docs, read those and skip this list.

- **Always:** newest work-log entries, `python3 scripts/work_log.py recent 5`.
- **Data sources, tables, layout:** [Tech](docs/steering/tech.md).
- **Status and future work:** [Current state](docs/steering/current_state.md).
- **Goals and model plan:** [Product](docs/steering/product.md).
- **Schedules, storage, AWS:** [Deployment](docs/steering/deployment.md).
- **Before a model change:** tech.md, Model change rules, and the [research ledger](docs/research/README.md).

Read large docs by section (`grep -n '^## '`), not whole. Code and built data are the source of truth; if a doc disagrees, verify and fix it. The user's latest instructions override these docs.

## Required document updates

- Every substantive code or behavior change: dated entry at the top of `docs/steering/work_log.md`, what changed, checks actually run, remaining limit; at most 150 words.
- Feature status and limits: `current_state.md`; sources, tables, algorithms and layout: `tech.md`; schedules, storage, secrets and AWS: `deployment.md`.
- Every tested model idea: `docs/research/README.md` with stage-1 and stage-2 numbers. Model or benchmark changes also regenerate `docs/elo_backtest.md` when the benchmark exists.

`uv run pytest -q` includes `tests/test_steering.py`, which requires a work-log update for code changes and enforces doc budgets. The repo-root pre-commit hook rotates the work log. Enable once per clone: `git config core.hooksPath .githooks`.

## What this is

A pre-match trading model for Rainbow Six Siege esports: player-based map Elo priced against Kalshi's R6 series (`KXR6GAME`) and map-winner (`KXR6MAP`) markets. Built by following Prometheus's `docs/playbooks/new_game.md` (the sibling `Prometheus` repo); it reuses Dota 2's (`../dota2`) and CS2's Liquipedia, Kalshi, linking and benchmark code. The playbook phase is in Current state.

## Quick commands

```bash
uv sync
uv run pytest -q
uv run ruff format && uv run ruff check
uv run promr6 --help
```

`data/` and `db/` are build artifacts; never commit them.

### Worktrees

Share raw caches by symlink (`data/liquipedia`, `data/siegegg` and `data/kalshi`); never share `db/`.

## Conventions

- **Network is polite and cached.** Liquipedia MediaWiki API (`https://liquipedia.net/rainbowsix/api.php`) only via `action=query` wikitext; never `action=parse` or scrape HTML pages. At most one request per 2 s, gzip, User-Agent naming this repo with a contact. Credit Liquipedia (CC BY-SA 3.0). siege.gg match pages (`https://siege.gg/matches/<id>`, robots allows; the ID comes from Liquipedia's `siegegg=` field) for five-player rosters: at most one request per 2 s, never re-fetch a finished match. Every fetcher takes an injectable `get`, so tests never touch the network.
- Changing parser output requires bumping `PARSER_VERSION`.
- **Raw first, parse later.** Save raw responses unchanged (gzip); rebuild the DB from them; parsers never fetch.
- **Data access is raw SQL** on SQLite; no ORM. Schema changes use a new numbered `scripts/NNN_*.sql`; rebuild from scratch, no migrations.
- **Times are UTC** (ISO 8601 with `Z`).
- **Model changes need a significant stage-1 gain and no stage-2 regression**, judged with the two-stage benchmark. Windows: seed before 2023, stage 1 [2023-01-01, 2026-01-01), stage 2 [2026-01-01, 2026-07-01), holdout 2026-07-01 on. Full rules: tech.md, Model change rules.
- **Trading** reuses Prometheus's executor rules and limits from a $50 seed; no new orders once capital (seed + settled profit − open stakes) is $0 or less.
- **CI time is a budget.** Measure added CI work and record before/after in the work log.
- **Token use is a budget.** Keep docs short; scripts print summaries, not per-row logs.
- Formatting and linting: `ruff` (configured in `pyproject.toml`).

## Before you finish a change

1. `uv run pytest -q` and `uv run ruff format --check && uv run ruff check` pass.
2. Inspect the diff and keep docs aligned with code. State anything not verified.
