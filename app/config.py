from pathlib import Path
import os
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")
DATA = ROOT / "data"
PRODUCTS = ROOT / "products"
STATIC = ROOT / "static"
DATA.mkdir(exist_ok=True)
PRODUCTS.mkdir(exist_ok=True)
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
API_KEY = os.getenv("FOUNDER_API_KEY", "")
AUTO_BUILD = os.getenv("AUTO_BUILD", "true").lower() == "true"
AUTO_PUBLISH = os.getenv("AUTO_PUBLISH", "true").lower() == "true"
AUTO_GITHUB_PUSH = os.getenv("AUTO_GITHUB_PUSH", "true").lower() == "true"
MIN_SCORE = int(os.getenv("MIN_IDEA_SCORE", "45"))
