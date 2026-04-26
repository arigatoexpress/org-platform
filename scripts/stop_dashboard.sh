#!/usr/bin/env bash
set -euo pipefail

SESSION_NAME="org-platform-dashboard"
PORT="${PORT:-3000}"

if command -v screen >/dev/null 2>&1; then
  screen -S "$SESSION_NAME" -X quit >/dev/null 2>&1 || true
fi

if pids="$(lsof -ti "tcp:${PORT}" 2>/dev/null)" && [ -n "$pids" ]; then
  kill $pids
  echo "Stopped dashboard listener on port ${PORT}"
else
  echo "No dashboard listener found on port ${PORT}"
fi

