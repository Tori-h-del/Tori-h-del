from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from app.extensions import db
from app.models import Dish, Order

bp = Blueprint("food", __name__)


@bp.get("/")
def home():
    return render_template("home.html")


@bp.get("/dishes")
def dish_list_page():
    dishes = Dish.query.order_by(Dish.id.asc()).all()
    return render_template("dishes.html", dishes=dishes)


@bp.get("/dishes/new")
def dish_create_page():
    return render_template("new_dish.html")


@bp.post("/dishes")
def create_dish():
    name = request.form.get("name", "").strip()
    category = request.form.get("category", "").strip()
    price_raw = request.form.get("price", "0").strip()

    if not name or not category:
        return "菜名和分类不能为空", 400

    try:
        price = float(price_raw)
    except ValueError:
        return "价格必须是数字", 400

    db.session.add(Dish(name=name, price=price, category=category))
    db.session.commit()
    return redirect(url_for("food.dish_list_page"))


@bp.get("/orders")
def order_list_page():
    orders = Order.query.order_by(Order.id.asc()).all()
    return render_template("orders.html", orders=orders)


@bp.get("/orders/new")
def order_create_page():
    dishes = Dish.query.order_by(Dish.id.asc()).all()
    return render_template("new_order.html", dishes=dishes)


@bp.post("/orders")
def create_order():
    customer_name = request.form.get("customer_name", "").strip()
    dish_id_raw = request.form.get("dish_id", "0").strip()
    quantity_raw = request.form.get("quantity", "1").strip()

    if not customer_name:
        return "下单人不能为空", 400

    try:
        dish_id = int(dish_id_raw)
        quantity = int(quantity_raw)
    except ValueError:
        return "菜品和数量必须是整数", 400

    dish = Dish.query.get(dish_id)
    if dish is None:
        return "菜品不存在", 404

    db.session.add(Order(customer_name=customer_name, dish_id=dish_id, quantity=quantity))
    db.session.commit()
    return redirect(url_for("food.order_list_page"))


@bp.get("/api/dishes")
def dish_list_api():
    dishes = Dish.query.order_by(Dish.id.asc()).all()
    data = [
        {"id": dish.id, "name": dish.name, "price": dish.price, "category": dish.category}
        for dish in dishes
    ]
    return jsonify(data)


@bp.get("/api/orders")
def order_list_api():
    orders = Order.query.order_by(Order.id.asc()).all()
    data = [
        {
            "id": order.id,
            "customer_name": order.customer_name,
            "dish_id": order.dish_id,
            "dish_name": order.dish.name,
            "quantity": order.quantity,
        }
        for order in orders
    ]
    return jsonify(data)
