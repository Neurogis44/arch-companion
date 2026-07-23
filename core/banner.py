"""Application banner."""

from config import APP_NAME, APP_SLOGAN, VERSION
from config.ui import PANEL_WIDTH


def show():
    """Display the application banner."""

    print("=" * PANEL_WIDTH)
    print(APP_NAME.upper().center(PANEL_WIDTH))
    print(APP_SLOGAN.center(PANEL_WIDTH))
    print()
    print(f"Version {VERSION}".center(PANEL_WIDTH))
    print("=" * PANEL_WIDTH)
    print()