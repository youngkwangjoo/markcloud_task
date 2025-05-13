from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import json

router = APIRouter()
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# JSON 데이터 불러오기 (앱 시작 시 1번만)
DATA_PATH = Path(__file__).parent / "data" / "trademark_sample.json"
with open(DATA_PATH, encoding="utf-8") as f:
    trademarks = json.load(f)

@router.get("/", response_class=HTMLResponse)
async def search_view(request: Request, q: str = ""):
    results = []

    if q:
        q_lower = q.lower()
        for item in trademarks:
            name_kr = item.get("productName") or ""
            name_en = item.get("productNameEng") or ""

            if q_lower in name_kr.lower() or q_lower in (name_en or "").lower():
                results.append(item)

    return templates.TemplateResponse("search.html", {
        "request": request,
        "query": q,
        "results": results
    })
