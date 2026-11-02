# Tech

## Stack

Python 3.12, uv, SQLite (raw SQL), typer CLI `promr6`, pytest, ruff. Ported from `../dota2` and `../cs2` as each phase needs it.

## Layout

| Path | Contents |
|---|---|
| `promr6/main.py` | CLI entry point |
| `scripts/work_log.py` | Work-log reader and rotation (pre-commit hook) |
| `tests/test_steering.py` | Work-log and doc-budget guard |

## Model change rules

Do not tune or select on holdout. Stage 1 tunes on outcomes only, [2023-01-01,2026-01-01). Stage 2 freezes parameters and validates outcomes and Kalshi's tradeable quote, [2026-01-01,2026-07-01). Holdout is 2026-07-01 on, opened once. Tradeable quote: first hourly bid/ask at least 30 minutes after listing and at least 2 hours before start, spread ≤0.06. Use paired match-clustered intervals; require significant stage-1 gain and no stage-2 regression, including guarded sections: all, tier1, tier2, tier3, international.

- An added parameter, feature or layer also needs a stage-1 gain of at least 0.0005 log loss.
- A stage-2 gain is reported but never rescues a change that failed stage 1; don't tune on stage 2 to pass it.
- Removals ship when every guarded section's interval stays below +0.0005 on both stages (non-inferior).
- Every tested model idea goes in the [research ledger](../research/README.md), adopted or not, with its numbers; count the tests run against stage 2.
- Trading results are reported, not gates. Data fixes ship when correct and the benchmark doesn't get significantly worse.
