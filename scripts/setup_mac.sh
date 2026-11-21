#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
if [ ! -f .env ]; then cp .env.example .env; KEY=$(python -c 'import secrets;print(secrets.token_urlsafe(36))'); sed -i '' "s/change-this-to-a-long-random-secret/$KEY/" .env; fi
mkdir -p data products
echo "Setup complete. Ensure Ollama is running and llama3.2:1b is installed."
