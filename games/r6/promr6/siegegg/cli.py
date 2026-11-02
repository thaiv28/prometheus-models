"""Fetch siege.gg pages or inspect their cache without network access."""

import json
from dataclasses import asdict
from pathlib import Path
from typing import Annotated

import typer

from promr6.siegegg import cache
from promr6.siegegg.fetch import fetch_matches
from promr6.siegegg.parse import parse_match

app = typer.Typer(no_args_is_help=True, pretty_exceptions_show_locals=False)


@app.command()
def fetch(
    ids: Annotated[list[int] | None, typer.Argument()] = None,
    from_file: Annotated[Path | None, typer.Option()] = None,
    refresh: bool = False,
    limit: Annotated[int | None, typer.Option(min=0)] = None,
):
    """Cache match IDs, optionally reading one ID per line from a file."""
    match_ids = list(ids or [])
    if from_file is not None:
        try:
            match_ids.extend(
                int(line.strip())
                for line in from_file.read_text().splitlines()
                if line.strip()
            )
        except (OSError, ValueError) as exc:
            raise typer.BadParameter(str(exc), param_hint="--from-file") from exc
    if not match_ids or any(i <= 0 for i in match_ids):
        raise typer.BadParameter("supply positive match IDs or --from-file")
    summary = fetch_matches(match_ids, refresh=refresh, limit=limit)
    typer.echo(" ".join(f"{key}={value}" for key, value in asdict(summary).items()))


@app.command()
def status():
    """Show cache counts and newest fetch timestamp."""
    index = cache.read_index()
    finished = sum(bool(row["finished"]) for row in index.values())
    missing = sum(row["status"] == 404 for row in index.values())
    newest = max((row["fetched_at"] for row in index.values()), default="none")
    typer.echo(
        f"cached={len(index)} finished={finished} "
        f"unfinished={len(index) - finished - missing} not_found={missing} newest={newest}"
    )


@app.command()
def show(match_id: Annotated[int, typer.Argument(min=1)]):
    """Print parsed teams and rosters from a cached match page."""
    body = cache.read_match(match_id)
    if body is None:
        typer.echo("Match is not cached.")
        raise typer.Exit(1)
    match = parse_match(body)
    if match is None:
        typer.echo("Cached page has no match (404).")
        raise typer.Exit(1)
    typer.echo(json.dumps(asdict(match), indent=2, ensure_ascii=False))
