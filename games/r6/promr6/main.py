import typer

from promr6.kalshi.cli import app as kalshi_app
from promr6.liquipedia.cli import app as liquipedia_app
from promr6.siegegg.cli import app as siegegg_app

app = typer.Typer(no_args_is_help=True, help="Rainbow Six Siege model (r6).")
app.add_typer(liquipedia_app, name="liquipedia", help="Crawl Liquipedia R6 pages.")
app.add_typer(kalshi_app, name="kalshi", help="Collect Kalshi R6 markets.")
app.add_typer(siegegg_app, name="siegegg")


@app.callback()
def main() -> None:
    """Command groups are added as the playbook phases land."""
