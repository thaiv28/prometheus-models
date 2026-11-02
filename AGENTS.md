# AGENTS.md

Esports trading models priced against Kalshi, one folder per game. League of Legends lives in the separate `Prometheus` repo (model, website and the shared execution service).

| Path | Game | Package |
|---|---|---|
| `games/cs2/` | Counter-Strike 2 | `promcs` |
| `games/dota2/` | Dota 2 | `promdota` |
| `games/valorant/` | Valorant | `promval` |

Each game is its own uv project with its own `AGENTS.md`, steering docs, work log, data and tests. **Work in one game at a time:** `cd games/<game>`, read only that game's `AGENTS.md`, and run its commands from there. Don't read another game's docs unless you are porting code from it.

## Rules for every game

- Work in a separate worktree from the repo root: `git worktree add ../prometheus-models-<branch> -b <branch> <base>`, then `cd games/<game> && uv sync`. Gitignored state (`data/`, `db/`, `.env`) is per game; set it up as that game's `AGENTS.md` says, with `MAIN` meaning the main checkout's `games/<game>`.
- Enable the hooks once per clone: `git config core.hooksPath .githooks`. The pre-commit hook rotates the work log of each game a commit touches.
- A change to one game updates that game's work log. A change to the repo root (CI, hooks, this file) adds a short entry to the work log of each game it affects.
- Scheduled jobs set up through `.github/actions/setup-game`, Kalshi collection uses one matrix workflow, CI runs actionlint, and feeds dispatch Prometheus only when feed content (excluding `generated`) changes.
- CI (`.github/workflows/ci.yml`) checks only the games whose files changed; a change under `.github/workflows/<game>-*.yml` checks only that game; other changes under `.github/` check all of them.

## Status

Imported with history on 2026-11-02 from `cs2-model`, `dota2-model` and `valorant-model`. The scheduled workflows run from this repo as `.github/workflows/<game>-<workflow>.yml` (since 2026-11-02); S3 prefixes keep the old repo names (`cs2-model/`, `dota2-model/`, `valorant-model/`), which Prometheus and the execution Lambda read; the old repos are archived. Next: move shared code (Kalshi, quotes, blend, evaluation, backtest, trading, linking, Liquipedia) into one `core/` package.
