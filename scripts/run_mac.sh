#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
. .venv/bin/activate
if ! curl -fsS http://127.0.0.1:11434/api/tags >/dev/null 2>&1; then
  echo "Ollama is not reachable. Open the Ollama app, then try again."
  exit 1
fi
echo "Starting dashboard at http://127.0.0.1:8765"
echo "Keep this Terminal window open while running. Press Ctrl+C to stop."
exec uvicorn app.main:app --host 0.0.0.0 --port 8765