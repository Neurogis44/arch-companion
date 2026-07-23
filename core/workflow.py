"""Reusable workflows for Arch Companion."""

from knowledge.models import PackageInfo
from core.explanation import show_explanation
from core.confirm import ask_confirmation
from core.messages import success, info, error
from services.pacman import PacmanService


def install_package(package: PackageInfo):
    """Run the educational installation workflow."""

    show_explanation(package)

    if not ask_confirmation():
        info(f"{package.title} installation cancelled.")
        return

    result = PacmanService.install(package.package)

    if result == 0:
        success(f"{package.title} installed successfully.")
    else:
        error(f"Installation failed (exit code {result}).")