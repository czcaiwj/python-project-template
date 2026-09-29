# Project Instructions

## Environment

- Python 3.13+
- uv
- Ruff
- pytest

## Dependency Management

Use uv for all dependency management.

Use:

uv add <package>

For development dependencies:

uv add --dev <package>

Do not use pip directly unless explicitly required.

## Code Quality

Before considering a task complete, run:

uv run ruff check .
uv run ruff format --check .
uv run pytest

## Coding Style

- Use type annotations for public functions.
- Prefer pathlib over os.path.
- Avoid unnecessary dependencies.
- Keep functions small and focused.
- Do not hardcode secrets.

## Security

- Never commit credentials or API keys.
- Never log passwords, tokens, or secrets.
- Validate external input.
- Use established cryptographic libraries.
- Avoid shell=True unless explicitly required.

## Change Policy

Before making significant changes:

1. Inspect the existing implementation.
2. Keep changes scoped.
3. Avoid unrelated refactoring.
4. Run tests after changes.
5. Review git diff before completion.
