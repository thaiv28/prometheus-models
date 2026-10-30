"""The `promdota` command line."""

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


if __name__ == "__main__":
    app()
