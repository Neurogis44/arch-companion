"""
Navigation manager.

Responsible for dispatching menu choices.
"""


class Navigation:
    """Handle menu navigation."""

    def __init__(self):
        """Initialize the navigation routes."""

        self.routes = {}

    def register(self, key, action):
        """Register a new menu action."""

        self.routes[key] = action

    def execute(self, key):
        """Execute the action associated with a menu choice."""

        action = self.routes.get(key)

        if action:
            action()
        else:
            print()
            print("Invalid choice.")