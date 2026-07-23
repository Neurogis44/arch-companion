from core.screen import clear
from core.ui import show_title, show_menu, ask_choice


class SteamModule:
    """Steam module."""

    def open(self):
        """Open the Steam menu."""

        steam_options = [
            "Install Steam",
            "Remove Steam",
            "Check installation",
        ]

        while True:
            clear()

            show_title("Steam")
            show_menu(steam_options)

            choice = ask_choice()

            if choice == "0":
                break

            print()
            print(f"'{choice}' is not implemented yet.")
            input("\nPress Enter to continue...")