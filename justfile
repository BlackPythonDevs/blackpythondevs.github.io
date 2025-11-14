# Black Python Devs Website - Just recipes

# Display all available commands
help:
    @just --list

# Install dependencies
install:
    uv sync

# Run development server
serve:
    uv run render-engine serve

# Build static site
build:
    uv run --no-dev --prerelease=allow render-engine build

# Run tests
test:
    uv run pytest

# Run tests with verbose output
test-verbose:
    uv run pytest -v

# Run tests and generate coverage
test-coverage:
    uv run pytest --cov

# Run linting and formatting checks
lint:
    uv run ruff check .
    uv run ruff format . --check

# Format code
format:
    uv run ruff format .
    uv run ruff check . --fix

# Run pre-commit hooks
pre-commit-run:
    uv run pre-commit run --all-files

# Clean build artifacts
clean:
    rm -rf output/
    find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true

# Full development workflow (install, lint, test, build)
dev: install lint test build
    @echo "✓ Development workflow complete"
