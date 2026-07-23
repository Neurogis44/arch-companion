"""Reusable explanation screen."""

from knowledge.models import PackageInfo

from core.card import Card

from core.icons import (
    PACKAGE,
    COMMAND,
    BOOK,
    LEARN,
    GLOBE,
)


def show_explanation(info: PackageInfo):
    """Display a standardized explanation."""

    card = Card(info.title)

    card.add_field("Description", info.description)
    card.add_field("Difficulty", info.difficulty)

    card.add_blank()

    card.add_field(f"{PACKAGE} Package", info.package)
    card.add_field(f"{BOOK} Repository", info.repository)
    card.add_field(f"{COMMAND} Command", info.command)

    card.add_blank()

    card.add_section(f"{LEARN} Explanation")
    card.add_list(info.explanation)

    card.add_blank()

    card.add_field(f"{GLOBE} Official documentation", info.wiki)

    card.render()