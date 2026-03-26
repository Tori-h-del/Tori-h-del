from dataclasses import dataclass


@dataclass
class Dish:
    id: int
    name: str
    price: float
    category: str


@dataclass
class Order:
    id: int
    customer_name: str
    dish_id: int
    quantity: int


class FoodStore:
    """新手练习用内存数据仓库，服务重启后会清空。"""

    def __init__(self) -> None:
        self._dishes: list[Dish] = [
            Dish(id=1, name="宫保鸡丁", price=26.0, category="川菜"),
            Dish(id=2, name="番茄鸡蛋面", price=16.0, category="面食"),
        ]
        self._orders: list[Order] = []
        self._next_dish_id = 3
        self._next_order_id = 1

    def list_dishes(self) -> list[Dish]:
        return self._dishes

    def add_dish(self, name: str, price: float, category: str) -> Dish:
        dish = Dish(id=self._next_dish_id, name=name, price=price, category=category)
        self._dishes.append(dish)
        self._next_dish_id += 1
        return dish

    def list_orders(self) -> list[Order]:
        return self._orders

    def add_order(self, customer_name: str, dish_id: int, quantity: int) -> Order:
        order = Order(
            id=self._next_order_id,
            customer_name=customer_name,
            dish_id=dish_id,
            quantity=quantity,
        )
        self._orders.append(order)
        self._next_order_id += 1
        return order


store = FoodStore()
