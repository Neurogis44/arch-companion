# ADR-0001 — Project Structure

## Status

Accepted

## Date

2026-07-23

## Context

Arch Companion is expected to grow into a modular educational application.

As the project expands, the directory structure must remain clear,
predictable and easy for contributors to navigate.

## Decision

The project is organized into distinct layers:

- config/
- core/
- knowledge/
- modules/
- services/
- tests/
- docs/

Each directory has a single responsibility.

## Consequences

### Positive

- Better maintainability
- Easier onboarding
- Clear separation of concerns
- Simpler navigation

### Negative

- Slightly more files
- Requires discipline when adding new modules

## Alternatives Considered

Keeping all Python files in a single directory.

Rejected because the project is expected to grow significantly.