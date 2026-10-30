"""Fetch OpenDota history into the raw cache."""

from pathlib import Path
from typing import Annotated

import typer

from promdota.opendota import cache, fetch
from promdota.opendota.http import Fetcher

app = typer.Typer(no_args_is_help=True, pretty_exceptions_show_locals=False)
DEFAULT_DB = Path("db/dota2.db")
LIMIT_HELP = "Requests this run (default 1,800 free; 100,000 with OPENDOTA_API_KEY)."


@app.command()
def bulk(
    from_month: str = typer.Option("2019-01", "--from"),
    to_month: str | None = typer.Option(None, "--to"),
    limit: int | None = typer.Option(None, min=0, help=LIMIT_HELP),
):
    """Fetch monthly Explorer matches and players."""
    try:
        counts = fetch.bulk(Fetcher(limit=limit), from_month, to_month)
    except ValueError as exc:
        raise typer.BadParameter("months must have YYYY-MM format") from exc
    typer.echo(" ".join(f"{key}={value}" for key, value in sorted(counts.items())))


@app.command()
def games(
    limit: int | None = typer.Option(None, min=0, help=LIMIT_HELP),
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
