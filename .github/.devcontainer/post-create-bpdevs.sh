#!/bin/sh

# Get the directory of the current script
DIR=$(dirname "$0")

# Navigate to the root directory
BPD_DIR= "$DIR/../.."

pre-commit install
py -m pip install --no-cache-dir -r ${BPD_DIR}/requirements-dev.txt
py -m playwright install --with-deps
