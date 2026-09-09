#!/usr/bin/env bash
set -e

echo "=== ruff format --check ==="
py -m ruff format --check .

echo "=== ruff check ==="
py -m ruff check .

echo "=== pytest ==="
py -m pytest
