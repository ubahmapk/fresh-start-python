from sys import stderr
from typing import Annotated

import typer
from loguru import logger
from rich import print as rprint

from freshstartpy.__version__ import __version__


def set_logging_level(verbosity: int) -> None:
    """Set the global logging level"""

    # Default level
    log_level = "INFO"

    if verbosity is not None:
        if verbosity == 1:
            log_level = "INFO"
        elif verbosity > 1:
            log_level = "DEBUG"
        else:
            log_level = "ERROR"

    logger.remove(0)
    # noinspection PyUnboundLocalVariable
    logger.add(stderr, level=log_level)

    return None


app = typer.Typer(
    add_completion=False, context_settings={"help_option_names": ["-h", "--help"]}
)


def version_callback(value: bool) -> None:
    if value:
        print(f"freshstartpy version {__version__}")
        raise typer.Exit(0)

    return None


@app.command()
def main(
    verbosity: Annotated[
        int,
        typer.Option("--verbose", "-v", count=True, help="Repeat for extra verbosity"),
    ] = 0,
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-V",
            callback=version_callback,
            is_eager=True,
            show_default=False,
            help="Show the version and exit.",
        ),
    ] = False,
) -> None:
    rprint("[bold green]Template for fresh python projects[/bold green]")


if __name__ == "__main__":
    app()
