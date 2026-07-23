from core.banner import Banner
from core.menu import Menu
from core.navigation import Navigation
from modules.gaming import GamingModule
from core.screen import clear


class App:
    """Main application."""

    def __init__(self):
        """Initialize the application."""

        self.banner = Banner()
        self.menu = Menu()
        self.navigation = Navigation()
        self.gaming = GamingModule()

        self.navigation.register("1", self.open_gaming)
        self.navigation.register("5", self.open_settings)

    def run(self):
        """Start the application."""

        while True:

            clear()
            
            self.banner.show()
            self.menu.show()

            choice = self.menu.get_choice()

            if choice == "0":
                print()
                print("Thanks for using Arch Companion!")
                break

            self.navigation.execute(choice)


    def open_gaming(self):
        """Open the Gaming module."""

        self.gaming.open()

    def open_settings(self):
        """Open the Settings module."""

        print()
        print("⚙️ Settings coming soon!")