from fastapi import APIRouter, HTTPException

from app.models.fake_db import db
from app.schemas.item import Item, ItemCreate

router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=list[Item], summary="获取全部物品")
def list_items() -> list[Item]:
    return db.list_items()


@router.post("", response_model=Item, status_code=201, summary="创建物品")
def create_item(item_in: ItemCreate) -> Item:
    return db.create_item(item_in)


@router.get("/{item_id}", response_model=Item, summary="按 ID 获取物品")
def get_item(item_id: int) -> Item:
    item = db.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
