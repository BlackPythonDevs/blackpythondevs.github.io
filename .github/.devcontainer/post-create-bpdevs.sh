#!/bin/sh

# Get the directory of the current script
DIR=$(dirname "$0")

# Navigate to the root directory
BPD_DIR= "$DIR/../.."

pre-commit install
py -m pip install --no-cache-dir -r ${BPD_DIR}/requirements-dev.txt
py -m playwright install --with-deps

# List the vscode-codespaces extensions
ls ~/.vscode-remote/extensions

# Define the extensions to be deleted
extensions=("rebornix.ruby" "wingrunr21.vscode-ruby")

for extension in "${extensions[@]}"; do
  # Check if the extension directory exists
  if [ -d "~/.vscode-remote/extensions/$extension"* ]; then
    echo "Deleting $extension"
    rm -rf ~/.vscode-remote/extensions/$extension-*
  else
    echo "$extension does not exist"
  fi
done
