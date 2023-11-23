#!/bin/sh

pre-commit install
py -m pip install --no-cache-dir -r /usr/local/requirements-dev.txt
py -m playwright install --with-deps

# List the vscode-codespaces extensions
ls ~/.vscode-remote/extensions

# Define the extensions to be deleted
extension1="rebornix.ruby"
extension2="wingrunr21.vscode-ruby"
extension3="Shopify.ruby-lsp"

# Check if the extension directories exist and delete them
for extension in $extension1 $extension2 $extension3
do
  if [ -d ~/.vscode-remote/extensions/$extension-* ]; then
    echo "Deleting $extension"
    rm -rf ~/.vscode-remote/extensions/$extension-*
  else
    echo "$extension does not exist"
  fi
done
