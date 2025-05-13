from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .views import router as search_router

app = FastAPI()

# 정적 파일 (선택)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 검색 라우터 등록
app.include_router(search_router)
