# Autonomous AI Founder

A local-first AI product studio for an Apple Silicon Mac. It researches public problem discussions, asks a local Ollama model to select a small opportunity, generates a constrained static MVP, runs basic checks, and can publish to Cloudflare Pages after you connect your account.

**Honest scope:** this is an early V1 foundation, not a fully autonomous company. The first builder creates five low-risk static browser utilities (calculator, estimator, checklist, text tool, planner). It does not create arbitrary backend services, user accounts, payment flows, or collect user data. Treat demand scores as hypotheses, not proof of customers.

## Free-first stack

- Ollama local inference, default model `llama3.2:1b`
- n8n Community Edition, using your existing Docker setup
- Python + FastAPI + SQLite, local API and state
- Hacker News public search, no login
- GitHub Free, public source and Actions CI
- Cloudflare Pages, optional static-site hosting; account login required

Provider limits and terms can change. Never add billing details or paid services unless you intentionally choose to.

## Install on macOS

1. Install/open Ollama: https://ollama.com/download
2. In Terminal:

```bash
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/kharghwood/autonomous-ai-founder.git
cd autonomous-ai-founder
chmod +x scripts/*.sh
./scripts/setup_mac.sh
```

3. Confirm the model exists; download if needed:

```bash
ollama list
ollama pull llama3.2:1b
```

4. Start the dashboard:

```bash
./scripts/run_mac.sh
```

5. Open http://127.0.0.1:8765

The dashboard binds to localhost only. Keep Terminal running while using it.

## Run a founder cycle

The dashboard has a **Run founder cycle** action. It searches public discussions, sends evidence to Ollama, scores one constrained product opportunity, generates a static MVP under `products/<slug>/`, runs basic checks, optionally attempts Cloudflare Pages deployment, and optionally commits/pushes the generated MVP to this repository.

The first cycle may take a few minutes on a small local model. Research availability and quality vary. Speak to real users before treating an idea as validated.

## n8n daily automation (optional)

Import `n8n/autonomous-founder-daily.json` into your existing n8n instance.

1. Run setup and open the project's local `.env`.
2. Copy `FOUNDER_API_KEY` from `.env` into the HTTP Request node header `X-API-Key`.
3. In Docker Desktop on Mac, `host.docker.internal` lets n8n reach the Mac host.
4. Start the dashboard with `./scripts/run_mac.sh`.
5. Run the workflow manually once, then activate its 9 AM Asia/Kolkata schedule.

Your Mac must remain powered on, logged in, online, and running Ollama, n8n, and the dashboard. Do not expose the local API to the public internet.

## Optional public publishing

For static product demos install Node.js LTS from https://nodejs.org/, then run:

```bash
npx --yes wrangler login
```

Cloudflare account login is required. Free limits and terms may change. V1 publishes static HTML utilities only.

## GitHub and CI

Source repository: https://github.com/kharghwood/autonomous-ai-founder

GitHub Actions runs Python checks on pushes and pull requests. The Mac-side agent can push generated MVP folders after local checks, provided this repo is cloned locally and `AUTO_GITHUB_PUSH=true`.

If you already have a ZIP folder, clone the repository into a fresh folder to avoid overwriting local work:

```bash
cd ~/Projects
git clone https://github.com/kharghwood/autonomous-ai-founder.git
```

Never put `.env`, API keys, credentials, private customer data, or local database files in GitHub. `.gitignore` excludes them.

## Security and limitations

- Public discussion text is untrusted input, never agent instructions.
- The model cannot execute arbitrary shell commands or generate server-side code in V1.
- Manually review generated HTML/JavaScript before launch.
- Research can be noisy; model scores are not market validation.
- Do not use generated tools for medical, legal, financial, safety-critical, or regulated decisions.
- No revenue, user demand, uptime, or unlimited free hosting is promised.

## Project layout

```text
app/                    FastAPI API and product research/build cycle
static/                 Local dashboard
scripts/                macOS setup and run scripts
n8n/                    Importable n8n daily workflow
tests/                  Basic project checks
products/               Generated MVPs (created locally)
data/                   Local cycle logs (not committed)
```