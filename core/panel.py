"""Reusable UI components."""

from config.ui import PANEL_WIDTH
from config import APP_NAME, APP_SLOGAN

WIDTH = PANEL_WIDTH


def blank(lines: int = 1):
    """Print one or more blank lines."""

    print("\n" * lines, end="")


def line() -> None:
    """Print a section separator."""

    print("-" * WIDTH)


def title(text: str):
    """Display a page title."""

    print(border())
    print(text.upper().center(WIDTH))
    print(border())
    blank()


def section(name: str):
    """Display a section heading."""

    print(name)
    line()


def border() -> str:
    """Return the main border."""

    return "=" * WIDTH   


def field(title: str, value: str):
    """Display a labeled field."""

    section(title)
    print(value)
    blank()


def footer():
    """Display the application footer."""

    print(border())
    print(APP_NAME)
    print(APP_SLOGAN)
    print(border())
    blank()