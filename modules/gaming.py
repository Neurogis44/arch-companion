from core.screen import clear
from core.ui import show_title, show_menu


class GamingModule:
    """Gaming module."""

    def open(self):
        """Open the Gaming menu."""

        gaming_apps = [
            "Steam",
            "Heroic Games Launcher",
            "Lutris",
            "MangoHud",
            "Gamescope",
        ]

        while True:

            clear()

            show_title("Gaming")
            show_menu(gaming_apps)

            choice = input("Your choice: ")

            if choice == "0":
                break

            print()
            print(f"'{choice}' is not implemented yet.")
            input("\nPress Enter to continue...")