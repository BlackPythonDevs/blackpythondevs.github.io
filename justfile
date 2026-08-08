# Black Python Devs Website - Just recipes
# Run tasks with: just <task-name>

# Preserve quoting on *ARGS recipes so values with spaces survive (e.g. "Valentina Ariza Gómez")
set positional-arguments

# Display all available commands
help:
    @just --list

# Install dependencies
sync:
    uv sync --all-extras

# Run development server
serve:
    uv run --no-dev --prerelease=allow render-engine serve

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
    uv run python scripts/add_conference.py "$@"

# Add a BPD Council member (data, image, announcement post)
# Usage: just add-council-member --name "First Last" --image tmp/photo.jpg --bio-file tmp/profile.md [--linkedin URL] [--date YYYY-MM-DD]
add-council-member *ARGS:
    uv run python scripts/add_council_member.py "$@"

# Verify _posts frontmatter authors are well-formed
check-authors:
    uv run python scripts/check_author_list.py

# Regenerate assets/map.html from _data/map_data.json
generate-map:
    uv run python scripts/map.py

# Print the slug for a name (e.g. just slugify "Valentina Ariza Gómez" -> valentina-ariza-gomez)
slugify NAME:
    @uvx --from python-slugify slugify "$1"

# Optimize an image in place for web use (resize to 512px square, convert to webp)
# Usage: just optimize-image tmp/photo.jpg  ->  writes tmp/photo.webp, removes the original
optimize-image SRC:
    #!/usr/bin/env bash
    set -euo pipefail
    src="{{SRC}}"
    dest="${src%.*}.webp"
    magick "$src" -resize '512x512^' -gravity center -extent 512x512 -strip -quality 82 "$dest"
    if [ "$src" != "$dest" ]; then rm -f "$src"; fi
    echo "✓ wrote $dest"

# Run full development workflow
dev: sync lint test build
    @echo "✓ Development workflow complete"
