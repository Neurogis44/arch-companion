"""Custom exceptions for Arch Companion."""


class ArchCompanionError(Exception):
    """Base exception for the application."""


class PacmanNotFoundError(ArchCompanionError):
    """Raised when pacman is unavailable."""