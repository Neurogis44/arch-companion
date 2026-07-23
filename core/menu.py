"""
Menu module.

Responsible for displaying the main menu.
"""


class Menu:
    """Main menu."""

    def show(self):
        print()
        print("1. Gaming")
        print("2. Development")
        print("3. Virtualization")
        print("4. System Information")
        print("5. Settings")
        print()
        print("0. Exit")
        print()

    def get_choice(self):
        return input("Your choice: ")