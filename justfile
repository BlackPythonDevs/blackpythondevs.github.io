# Black Python Devs Website - Just recipes
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

# Add a sponsored conference and regenerate the activity map
# Usage: just add-conference --title "PyCon Brazil" --year 2026 --continent "South America" --country "Brazil"
add-conference *ARGS:
    uv run python scripts/add_conference.py {{ARGS}}

# Run full development workflow
dev: sync lint test build
    @echo "✓ Development workflow complete"
