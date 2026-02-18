# Black Python Devs Website - Task Runner
# Run tasks with: just <task-name>

# Display all available commands
help:
    @just --list

# Install dependencies
sync:
    uv sync --all-extras

# Run development server
serve:
    uv run render-engine serve

# Build static site
build:
    uv run --no-dev --prerelease=allow render-engine build

# Run linters
lint:
    uv run ruff check .
    uv run ruff format --check .

# Install hooks
install-hooks:
    uv run pre-commit install

# Run pre-commit hooks
pre-commit:
    uv run pre-commit run --all-files

# Run tests
test:
    uv run --dev pytest

# Run tests with verbose output
test-verbose:
    uv run --dev pytest -v

# Run full development workflow
dev: sync lint test build
    @echo "✓ Development workflow complete"
