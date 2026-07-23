# Architecture

## Layers

UI
↓
Workflow
↓
Services
↓
Operating System

Knowledge
↑
Shared by all workflows

---

## Responsibilities

core/
Application engine.

modules/
Menus only.

knowledge/
Educational content.

services/
System actions.

config/
Application settings.

tests/
Automated tests.

---

## Rules

- Services never print.
- Knowledge never executes commands.
- Modules never call Linux commands directly.
- Workflows orchestrate everything.