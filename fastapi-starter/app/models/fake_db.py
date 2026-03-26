from app.schemas.item import Item, ItemCreate


class FakeItemDB:
    """教学用内存数据库：重启服务后数据会清空。"""

    def __init__(self) -> None:
        self._items: list[Item] = []
        self._next_id = 1

    def list_items(self) -> list[Item]:
        return self._items

    def create_item(self, item_in: ItemCreate) -> Item:
        item = Item(id=self._next_id, **item_in.model_dump())
        self._items.append(item)
        self._next_id += 1
        return item

    def get_item(self, item_id: int) -> Item | None:
        return next((item for item in self._items if item.id == item_id), None)


db = FakeItemDB()
