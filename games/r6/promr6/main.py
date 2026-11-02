import typer

from promr6.siegegg.cli import app as siegegg_app

app = typer.Typer(no_args_is_help=True, help="Rainbow Six Siege model (r6).")
app.add_typer(siegegg_app, name="siegegg")


@app.callback()
def main() -> None:
    """Command groups are added as the playbook phases land."""
