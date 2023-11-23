#!/bin/sh

rbenv install
bundle config build.prism --enable-static

# List the vscode-codespaces extensions
ls ~/.vscode-remote/extensions

# Define the extensions to be deleted
extension1="rebornix.ruby"
extension2="wingrunr21.vscode-ruby"

# Check if the extension directories exist and delete them
for extension in $extension1 $extension2
do
  if [ -d ~/.vscode-remote/extensions/$extension-* ]; then
    echo "Deleting $extension"
    rm -rf ~/.vscode-remote/extensions/$extension-*
  else
    echo "$extension does not exist"
  fi
done
