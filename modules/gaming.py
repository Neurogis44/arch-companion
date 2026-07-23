from core.screen import clear
from core.ui import show_title, show_menu, ask_choice
from modules.steam import SteamModule

class GamingModule:
    """Gaming module."""

    def __init__(self):
        self.steam = SteamModule()

    def open(self):

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

            choice = ask_choice()

            if choice == "0":
                break

            if choice == "1":
                self.steam.open()

            elif choice == "0":
                break

            else:
                print()
                print(f"'{choice}' is not implemented yet.")
                input("\nPress Enter to continue...")