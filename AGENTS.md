# AGENTS.md

## Repository purpose

This repository is a reusable Python project template intended for development with both human contributors and coding agents.

Keep the repository portable across macOS, Linux, and WSL. Do not introduce machine-specific paths or local environment assumptions.

## Source of truth

Before changing code, inspect the existing repository configuration.

Use these files as the authoritative source for project behavior:

- `pyproject.toml` — Python version requirements, dependencies, pytest, Ruff, and build configuration.
- `.python-version` — default project Python version.
- `uv.lock` — locked dependency resolution.
- `.editorconfig` — editor-independent formatting defaults.
- `.gitattributes` — Git text and line-ending behavior.
- `.vscode/` — repository-level VS Code integration.

Do not duplicate configuration in another file when an existing tool-specific configuration already defines it.

## Python environment

Use `uv` for Python version, dependency, virtual environment, and command execution workflows.

Preferred commands:

```bash
uv sync --locked
uv add <package>
uv add --dev <package>
uv remove <package>
uv run <command>
```

Do not use `pip install` directly unless the task explicitly requires it.

Do not create or commit another virtual environment format. The repository-local environment is `.venv/`.

## Development workflow

Before making changes:

1. Inspect the relevant implementation and configuration.
2. Check `git status`.
3. Keep the change scoped to the requested task.
4. Avoid unrelated refactoring.

When changing behavior:

- Add or update tests when practical.
- Preserve existing public behavior unless the task explicitly changes it.
- Prefer standard-library functionality over adding unnecessary dependencies.
- Use `pathlib` for filesystem paths.
- Use type annotations for public functions and interfaces.

## Planning

For small, localized changes, inspect the relevant code and proceed directly.

Use a written implementation plan when a task involves substantial complexity, such as:

- changes spanning multiple subsystems or architectural boundaries;
- public API or persistent-data migrations;
- security-sensitive changes;
- significant refactoring;
- substantial uncertainty that requires investigation or prototyping;
- work that needs multiple independently verifiable milestones.

Do not create planning documents for routine fixes or narrowly scoped changes.

If the repository later defines a project-specific planning standard, follow that standard.

## Validation

Before considering a code change complete, run:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

If dependency metadata changed, also verify:

```bash
uv sync --locked
```

Review the final diff:

```bash
git diff --check
git diff
git status
```

Do not report the task as complete if relevant checks fail. If a check cannot be run, state why.
The local validation commands should match the repository CI checks. Do not change CI merely to bypass a local failure.

## Security

Never commit credentials, API keys, tokens, private keys, passwords, or other secrets.

Use `.env` for local secrets and keep `.env.example` limited to safe example values and variable names.

Do not log secrets.

Treat external input as untrusted.

Avoid `shell=True` unless it is explicitly justified.

Use established security and cryptographic libraries instead of custom implementations.

## Change discipline

Prefer the smallest correct change.

Do not:

- modify unrelated files;
- rewrite working code only for stylistic preference;
- change dependency versions without a reason;
- modify `uv.lock` unless dependency resolution actually needs to change;
- introduce OS-specific absolute paths;
- bypass failing tests or lint rules merely to make checks pass.

## Documentation

Update `README.md` when developer-facing setup or usage changes.

Keep detailed project knowledge in appropriate repository documentation instead of expanding this file indefinitely.

If the project becomes large enough to require architectural or design documentation, add structured documentation under `docs/` and link to it from this file.