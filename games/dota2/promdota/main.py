"""The `promdota` command line."""

import os
import sqlite3
import time
from pathlib import Path

import typer

from promdota.kalshi.cli import app as kalshi_app
from promdota.liquipedia.cli import app as liquipedia_app
from promdota.opendota.cli import app as opendota_app

app = typer.Typer(no_args_is_help=True, pretty_exceptions_show_locals=False)
app.add_typer(opendota_app, name="opendota", help="Cache OpenDota games and players.")
app.add_typer(kalshi_app, name="kalshi", help="Collect Kalshi Dota 2 markets.")

app.add_typer(
    liquipedia_app, name="liquipedia", help="Crawl Liquipedia Dota 2 tournament pages."
)


@app.command("export")
def export_command(
    out: Path | None = None,
    no_fetch: bool = False,
    state: Path | None = None,
    candidates: Path | None = None,
):
    """Write the Prometheus site prediction feed."""
    from promdota.feed import export, load_state

    export(
        state=load_state(state) if state else None,
        out=out,
        no_fetch=no_fetch,
        candidates_path=candidates,
    )


@app.command("blend-artifact")
def blend_artifact_command(out: Path = Path("promdota/blend_artifact.json")):
    """Freeze monthly coefficients from the adopted benchmark's series rows."""
    import json
    from datetime import UTC, datetime

    from promdota.trading import adopted_series_rows, build_blend_artifact

    root = Path(os.environ.get("PROMDOTA_DATA", "data"))
    with sqlite3.connect("db/dota2.db") as conn:
        rows = adopted_series_rows(conn, root / "kalshi")
    artifact = build_blend_artifact(rows, "dota2", "KXDOTA2GAME", datetime.now(UTC))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(artifact, indent=2, allow_nan=False) + "\n")
    snapshots = artifact["snapshots"]
    latest = snapshots[-1] if snapshots else None
    print(
        f"snapshots={len(snapshots)}"
        + (
            f" latest_a={latest['market_slope']:.9f} latest_b={latest['gap_slope']:.9f} latest_n={latest['training_series']}"
            if latest
            else " latest=none"
        )
    )


@app.command("feed-state")
def feed_state_command(out: Path | None = None):
    """Build the ratings snapshot from the local database."""
    from promdota.feed import build_state, save_state

    started = time.monotonic()
    root = Path(os.environ.get("PROMDOTA_DATA", "data"))
    out = out or root / "feed/state.pkl.gz"
    with sqlite3.connect("db/dota2.db") as conn:
        state = build_state(conn, root)
    save_state(state, out)
    print(
        f"state={out} finals={len(state['rows'])} teams={len(state['seen'])} bytes={out.stat().st_size} seconds={time.monotonic() - started:.2f}"
    )


if __name__ == "__main__":
    app()
