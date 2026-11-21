from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse
from .config import API_KEY, STATIC
from .core import run_cycle, OLLAMA_URL, OLLAMA_MODEL
import json, urllib.request
from pathlib import Path

app=FastAPI(title="Autonomous AI Founder",version="1.0")
@app.get("/")
def home(): return FileResponse(STATIC/"index.html")
@app.get("/health")
def health(): return {"ok":True,"service":"Autonomous AI Founder"}
@app.get("/api/status")
def status():
    try:
        req=urllib.request.Request(OLLAMA_URL+"/api/tags")
        with urllib.request.urlopen(req,timeout=3) as r: data=json.loads(r.read())
        online=True; models=[m.get("name") for m in data.get("models",[])]
    except Exception: online=False; models=[]
    root=Path(__file__).resolve().parents[1]
    products=sorted(p.name for p in (root/"products").glob("*/index.html".replace("/index.html","")) if p.is_dir()) if (root/"products").exists() else []
    latest=root/"data"/"latest-cycle.json"
    return {"ollama_online":online,"model":OLLAMA_MODEL,"models":models,"products":products,"latest":json.loads(latest.read_text()) if latest.exists() else None}
@app.post("/api/run")
def run(x_api_key:str|None=Header(default=None)):
    if not API_KEY or x_api_key!=API_KEY: raise HTTPException(401,"Missing or incorrect X-API-Key. See .env")
    return run_cycle()
