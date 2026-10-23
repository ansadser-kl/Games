#!/usr/bin/env sh
set -eu
# Minimal local launcher for the static browser prototype.
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$ROOT"
PORT="${PORT:-8000}"
if command -v python3 >/dev/null 2>&1; then
  echo "BATTLEZONE: FIRESTORM → http://localhost:$PORT"
  exec python3 -m http.server "$PORT"
fi
echo "Python 3 is required for this helper. Open index.html via any static web server." >&2
exit 1
