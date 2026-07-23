"""Knowledge models."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PackageInfo:
    title: str
    package: str
    repository: str
    command: str
    description: str
    wiki: str
    difficulty: str
    explanation: list[str]