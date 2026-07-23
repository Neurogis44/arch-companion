"""Reusable information cards."""

from core.panel import title, field, section, footer


class Card:
    """Display a generic information card."""

    def __init__(self, title_text: str):
        self.title = title_text
        self.items: list[tuple[str, str, str]] = []

    def add_field(self, name: str, value: str):
        """Add a field to the card."""

        self.items.append(("field", name, value))

    def add_section(self, name: str):
        """Add a section title."""

        self.items.append(("section", name, ""))

    def add_blank(self):
        """Add an empty line to the card."""

        self.items.append(("blank", "", ""))

    def render(self, show_footer: bool = True):
        """Display the card."""

        title(self.title)

        for item_type, name, value in self.items:

            if item_type == "field":
                field(name, value)

            elif item_type == "section":
                section(name)

            elif item_type == "blank":
                print()

            elif item_type == "list":
                print(f"• {value}")

        if show_footer:
            footer()

    def add_list(self, items: list[str]):
        """Add a bulleted list."""

        for item in items:
            self.items.append(("list", "", item))