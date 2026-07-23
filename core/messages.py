"""Application messages."""

from core.icons import SUCCESS, ERROR, INFO


def success(message: str):
    print()
    print(f"{SUCCESS} {message}")
    print()


def error(message: str):
    print()
    print(f"{ERROR} {message}")
    print()


def info(message: str):
    print()
    print(f"{INFO} {message}")
    print()