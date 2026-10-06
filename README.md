# Python Project Template

A minimal Python project template built around `uv`, Ruff, pytest, and a `src/` package layout.

The repository is designed to work consistently across macOS, Linux, and WSL and to support both human development and AI-assisted coding workflows.

## Requirements

- Python 3.13 or later
- `uv`
- Git

VS Code is recommended but not required.

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd <project>
```

Synchronize the Python environment from the lock file:

```bash
uv sync --locked
```

This creates the project-local `.venv` when required.

## Development

Run the application:

```bash
uv run python-project-template
```

Run tests:

```bash
uv run pytest
```

Run lint checks:

```bash
uv run ruff check .
```

Check formatting:

```bash
uv run ruff format --check .
```

Format the project:

```bash
uv run ruff format .
```

## Dependency management

Add a runtime dependency:

```bash
uv add <package>
```

Add a development dependency:

```bash
uv add --dev <package>
```

Remove a dependency:

```bash
uv remove <package>
```

Commit both `pyproject.toml` and `uv.lock` when dependency resolution changes.

## Project structure

```text
.
├── src/
│   └── python_project_template/
├── tests/
├── .vscode/
├── .env.example
├── .python-version
├── AGENTS.md
├── pyproject.toml
└── uv.lock
```

Application code belongs under `src/` and tests under `tests/`.

## Environment variables

Use `.env` for local environment-specific values and secrets.

`.env` is ignored by Git.

Use `.env.example` to document required variable names and safe example values. Never put real credentials in `.env.example`.

## VS Code

The repository includes workspace settings and recommended extensions under `.vscode/`.

The project environment should be the repository-local `.venv`. Avoid committing machine-specific interpreter paths.

## AI-assisted development

Repository-level instructions for coding agents are defined in [`AGENTS.md`](AGENTS.md).

Those instructions describe the supported development workflow, validation commands, and repository safety constraints.