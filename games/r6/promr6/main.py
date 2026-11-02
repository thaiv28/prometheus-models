import typer

app = typer.Typer(no_args_is_help=True, help="Rainbow Six Siege model (r6).")


@app.callback()
def main() -> None:
    """Command groups are added as the playbook phases land."""
