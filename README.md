# Autonomous AI Founder

A local-first AI product studio for an Apple Silicon Mac. It researches public problem discussions, asks a local Ollama model to select a small opportunity, generates a constrained static MVP, runs basic checks, and can publish to Cloudflare Pages after you connect your account.

**Honest scope:** this is an early V1 foundation, not a fully autonomous company. The first builder creates five low-risk static browser utilities (calculator, estimator, checklist, text tool, planner). It does not create arbitrary backend services, user accounts, payment flows, or collect user data. Treat demand scores as hypotheses, not proof of customers.

## Free-first stack

- Ollama: local model inference, no API key (default model: `llama3.2:1b`)
- n8n Community Edition: optional daily schedule, using your existing Docker setup
- Python + FastAPI + SQLite: local API and state
- Hacker News public search: research source, no login
- GitHub Free: public source repository and Actions CI
- Cloudflare Pages: optional static-site hosting; Cloudflare login required

Provider limits and terms can change. Never add billing details or paid services to this project unless you intentionally choose to.

## Install on macOS

1. Install/open Ollama: https://ollama.com/download
2. Open Terminal and run:

```bash
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/kharghwood/autonomous-ai-founder.git
cd autonomous-ai-founder
chmod +x scripts/*.sh
./scripts/setup_mac.sh
```

3. Confirm the model exists:

```bash
ollama list
ollama pull llama3.2:1b
```

4. Start the dashboard:

```bash
./scripts/run_mac.sh
```

5. Open http://127.0.0.1:8765

The dashboard binds to localhost only. Keep the Terminal server running while using it.

## Run a founder cycle

The dashboard has a **Run founder cycle** action. It:
1. Searches public Hacker News discussions for problem statements.
2. Sends a small evidence sample to Ollama.
3. Scores one constrained, low-risk product idea.
4. Generates a static MVP in `products/<slug>/`.
5. Runs basic structural tests.
6. If configured, attempts Cloudflare Pages deployment.
7. If configured, commits/pushes the generated MVP to this GitHub repository.

The first cycle may take a few minutes on a small local model. Research availability and quality vary. Speak to real users before treating an idea as validated.

## n8n daily automation (optional)

Import `n8n/autonomous-founder-daily.json` into your existing n8n instance.

1. Run `./scripts/setup_mac.sh` and open the project's local `.env`.
2. Copy `FOUNDER_API_KEY` from `.env` into the HTTP Request node header `X-API-Key`.
3. In Docker Desktop on Mac, `host.docker.internal` routes from n8n to the Mac host.
4. Start the dashboard with `./scripts/run_mac.sh`.
5. Run the workflow manually once, then activate its 9 AM Asia/Kolkata schedule.

Your Mac must remain powered on, logged in, online, and running Ollama, n8n, and the dashboard. Do not expose the local API to the public internet.

## Optional public publishing

The default is Cloudflare Pages for static product demos. Install Node.js LTS from https://nodejs.org/, then run:

```bash
npx --yes wrangler login
```

The system attempts deployment only when a product passes its checks. A Cloudflare account is required; free limits and terms may change. V1 publishes static HTML utilities only.

## GitHub and CI

Source repository: https://github.com/kharghwood/autonomous-ai-founder

GitHub Actions runs Python checks on pushes and pull requests. The Mac-side agent can commit generated MVP folders after its local tests pass, provided the repository is cloned locally and `AUTO_GITHUB_PUSH=true`.

If you already have a folder from the ZIP, the simplest safe approach is to clone this repository into a new folder and use that copy:

```bash
cd ~/Projects
git clone https://github.com/kharghwood/autonomous-ai-founder.git
```

Do not put `.env`, API keys, credentials, private customer data, or local database files in GitHub. The `.gitignore` excludes them.

## Security and limitations

- Public discussion text is untrusted input, never an instruction to the agent.
- The model cannot execute arbitrary shell commands or generate server-side code in V1.
- Generated HTML/JavaScript should still be manually reviewed before launch.
- The research sample is narrow and can be noisy; model scores are not market validation.
- Don't use generated tools for medical, legal, financial, safety-critical, or regulated decisions.
- No revenue, user demand, uptime, or free unlimited hosting is promised.

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
