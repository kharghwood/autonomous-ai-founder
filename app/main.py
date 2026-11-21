from pathlib import Path
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import FileResponse
from .config import API_KEY, STATIC, OLLAMA_URL, OLLAMA_MODEL
from .core import run_cycle
import json, urllib.request

app = FastAPI(title="Autonomous AI Founder", version="1.0")
@app.get("/")
def home(): return FileResponse(STATIC / "index.html")
@app.get("/health")
def health(): return {"ok": True, "service": "Autonomous AI Founder"}
@app.get("/api/config")
def config(request: Request):
    host = request.client.host if request.client else ""
    if host not in {"127.0.0.1", "::1", "localhost", "testclient"}:
        raise HTTPException(status_code=403, detail="Local dashboard only")
    return {"api_key": API_KEY}
@app.get("/api/status")
def status():
    try:
        req = urllib.request.Request(OLLAMA_URL + "/api/tags")
        with urllib.request.urlopen(req, timeout=3) as response: data = json.loads(response.read())
        online = True; models = [model.get("name", "") for model in data.get("models", [])]
    except Exception:
        online = False; models = []
    root = Path(__file__).resolve().parents[1]
    products = sorted(path.name for path in (root / "products").glob("*") if path.is_dir())
    latest_file = root / "data" / "latest-cycle.json"
    latest = json.loads(latest_file.read_text()) if latest_file.exists() else None
    return {"ollama_online": online, "model": OLLAMA_MODEL, "models": models, "products": products, "latest": latest}
@app.post("/api/run")
def run(x_api_key: str | None = Header(default=None)):
    if not API_KEY or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Missing or incorrect X-API-Key. See local .env file.")
    return run_cycle()