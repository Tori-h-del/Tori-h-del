from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="物品名称")
    description: str | None = Field(None, max_length=200, description="物品描述")


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
