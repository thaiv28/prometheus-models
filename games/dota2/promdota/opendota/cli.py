"""Fetch OpenDota history into the raw cache."""

from pathlib import Path
from typing import Annotated

import typer

from promdota.opendota import cache, fetch
from promdota.opendota.http import DAILY_BUDGET, Fetcher

app = typer.Typer(no_args_is_help=True)
DEFAULT_DB = Path("db/dota2.db")


@app.command()
def bulk(
    from_month: str = typer.Option("2019-01", "--from"),
    to_month: str | None = typer.Option(None, "--to"),
    limit: int = typer.Option(DAILY_BUDGET, min=0),
):
    """Fetch monthly Explorer matches and players."""
    try:
        counts = fetch.bulk(Fetcher(limit=limit), from_month, to_month)
    except ValueError as exc:
        raise typer.BadParameter("months must have YYYY-MM format") from exc
    typer.echo(" ".join(f"{key}={value}" for key, value in sorted(counts.items())))


@app.command()
def games(
    limit: int = typer.Option(DAILY_BUDGET, min=0),
    db: Annotated[Path, typer.Option()] = DEFAULT_DB,
):
    """Fetch missing finished games referenced by SQLite."""
    counts = fetch.games(db, Fetcher(limit=limit))
    typer.echo(" ".join(f"{key}={value}" for key, value in sorted(counts.items())))


@app.command()
def status():
    """Count cached months, single games and retry records."""
    root = cache.data_dir()
    months = len(list((root / "explorer/matches").glob("*.json.gz")))
    singles = len(list((root / "matches").glob("*/*.json.gz")))
    typer.echo(
        f"months={months} games={singles} missing={len(cache.read(root / 'missing.json', {}))}"
    )
