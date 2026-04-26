#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

green() { printf "\033[32m%s\033[0m\n" "$1"; }
yellow() { printf "\033[33m%s\033[0m\n" "$1"; }

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required" >&2
  exit 1
fi

if [ ! -d .venv ]; then
  if command -v uv >/dev/null 2>&1; then
    uv venv .venv
  else
    python3 -m venv .venv
  fi
fi

if command -v uv >/dev/null 2>&1; then
  uv pip install --python .venv/bin/python -e .
else
  .venv/bin/pip install -U pip
  .venv/bin/pip install -e .
fi

if command -v npm >/dev/null 2>&1; then
  npm install --prefix surface/dashboard
else
  yellow "npm not found; dashboard dependencies were not installed"
fi

mkdir -p data/intel data/crypto data/store Intelligence

green "✓ Python environment ready"
green "✓ Dashboard dependencies checked"
green "✓ Data directories ready"
green "✓ Bootstrap complete"

