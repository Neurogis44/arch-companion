class GamingModule:

    def open(self):
        """Display the Gaming menu."""

        gaming_apps = [
            "Steam",
            "Heroic Games Launcher",
            "Lutris",
            "MangoHud",
            "Gamescope",
        ]

        print()
        print("=" * 40)
        print("               GAMING")
        print("=" * 40)
        print()

        for number, app in enumerate(gaming_apps, start=1):
            print(f"{number}. {app}")

        print()
        print("0. Back")
        print()

        choice = input("Your choice: ")

        print()
        print(f"You selected: {choice}")