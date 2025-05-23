import sys
from pathlib import Path

import typer
from streamlit.web import cli as stcli

from . import work

HERE = Path(__file__).parent
app = typer.Typer()


@app.command()
def run_app():
    """Run streamlit application"""
    app_file = str(HERE / "app.py")
    sys.argv = ["streamlit", "run", app_file]
    sys.exit(stcli.main())


@app.command()
def hello(name: str = "world"):
    typer.secho(f"Hello {name}!", fg="red")


@app.command()
def bottles(num: int = 10, beverage: str = "coke"):
    work.bottles(num, beverage)
