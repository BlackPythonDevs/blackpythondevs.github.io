# Build and serve the Black Python Devs website

# Default recipe to display help
default:
    @just --list

# Install dependencies
install:
    uv sync

# Build the site
build:
    uv run render-engine build

# Serve the site locally
serve:
    uv run render-engine serve

# Build and serve (watch mode)
dev: build
    uv run render-engine serve

# Clean build output
clean:
    rm -rf output

# Run tests
test:
    uv run pytest

# Lint with ruff
lint:
    uv run ruff check src

# Format code with ruff
format:
    uv run ruff format src

# Run all checks (lint, format, test)
check: lint format test

# Full development workflow: install, build, and serve
all: install build serve
