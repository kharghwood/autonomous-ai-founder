#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI missing. Install it with: brew install gh"
  exit 1
fi
if ! gh auth status >/dev/null 2>&1; then
  gh auth login
fi
gh auth setup-git
echo "GitHub CLI authentication ready."
echo "Current repository remote:"
git remote get-url origin
echo "Generated MVPs can now push to the connected GitHub repository after tests pass."