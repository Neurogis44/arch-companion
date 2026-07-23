"""Steam knowledge."""

from knowledge.models import PackageInfo


STEAM = PackageInfo(
    difficulty="Beginner",
    title="Steam",
    package="steam",
    repository="extra",
    command="sudo pacman -S steam",
    description="Steam is Valve's official gaming platform for Linux.",
    wiki="https://wiki.archlinux.org/title/Steam",
    explanation=[
        "pacman is Arch Linux's package manager.",
        "-S installs packages from the official repositories.",
        "Dependencies are installed automatically.",
    ],
)