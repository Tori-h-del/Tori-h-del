from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    description="一个适合新手理解的 FastAPI 项目骨架。",
)


@app.get("/health", tags=["system"], summary="健康检查")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(api_router)
