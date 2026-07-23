def show_title(title: str):
    """Display a standardized page title."""

    print("=" * 40)
    print(title.upper().center(40))
    print("=" * 40)
    print()


def show_menu(options: list[str]):
    """Display a standardized numbered menu."""

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    print()
    print("0. Back")
    print()