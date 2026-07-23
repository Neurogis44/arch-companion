"""Pacman service."""

from __future__ import annotations

import shutil
import subprocess

from core.exceptions import PacmanNotFoundError


class PacmanService:
    """Service for interacting with pacman."""

    @staticmethod
    def is_available() -> bool:
        """Return True if pacman is available."""

        return shutil.which("pacman") is not None

    @staticmethod
    def is_installed(package: str) -> bool:
        """Return True if a package is installed."""

        if not PacmanService.is_available():
            raise PacmanNotFoundError("pacman is not available.")

        result = subprocess.run(
            ["pacman", "-Q", package],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )

        return result.returncode == 0

    @staticmethod
    def install(package: str) -> int:
        """Install a package."""

        if not PacmanService.is_available():
            raise PacmanNotFoundError("pacman is not available.")

        result = subprocess.run(
            ["sudo", "pacman", "-S", package],
            check=False,
        )

        return result.returncode

    @staticmethod
    def remove(package: str) -> int:
        """Remove a package."""

        if not PacmanService.is_available():
            raise PacmanNotFoundError("pacman is not available.")

        result = subprocess.run(
            ["sudo", "pacman", "-R", package],
            check=False,
        )

    @staticmethod
    def update() -> int:
        """Update the system."""

        if not PacmanService.is_available():
            raise PacmanNotFoundError("pacman is not available.")

        result = subprocess.run(
            ["sudo", "pacman", "-Syu"],
            check=False,
        )

        return result.returncode