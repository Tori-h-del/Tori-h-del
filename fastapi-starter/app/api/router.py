from fastapi import APIRouter

from app.api.routes.items import router as items_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(items_router)
