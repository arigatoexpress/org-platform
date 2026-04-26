#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DASHBOARD_DIR="$ROOT/surface/dashboard"
SESSION_NAME="org-platform-dashboard"
LOG_FILE="/tmp/org-platform-dashboard.log"
PORT="${PORT:-3000}"
HOST="${HOST:-127.0.0.1}"

if lsof -ti "tcp:${PORT}" >/dev/null 2>&1; then
  echo "Dashboard already listening at http://${HOST}:${PORT}"
  exit 0
fi

if command -v screen >/dev/null 2>&1; then
  screen -S "$SESSION_NAME" -X quit >/dev/null 2>&1 || true
  screen -dmS "$SESSION_NAME" bash -lc \
    "cd '$DASHBOARD_DIR' && npm run dev -- --hostname '$HOST' --port '$PORT' >> '$LOG_FILE' 2>&1"
else
  nohup bash -lc \
    "cd '$DASHBOARD_DIR' && npm run dev -- --hostname '$HOST' --port '$PORT'" \
    >> "$LOG_FILE" 2>&1 < /dev/null &
fi

for _ in 1 2 3 4 5 6 7 8 9 10; do
  if curl -fsS "http://${HOST}:${PORT}" >/dev/null; then
    echo "Dashboard ready at http://${HOST}:${PORT}"
    echo "Log: ${LOG_FILE}"
    exit 0
  fi
  sleep 1
done

echo "Dashboard did not become ready. Last log lines:" >&2
tail -40 "$LOG_FILE" >&2 || true
exit 1

