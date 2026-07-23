"""Confirmation helpers."""


def ask_confirmation() -> bool:
    """Ask the user to confirm an action."""

    while True:
        answer = input("Continue? [y/N]: ").strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("", "n", "no"):
            return False

        print("Please answer with y or n.")