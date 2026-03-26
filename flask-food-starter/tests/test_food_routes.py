from app import create_app
from app.extensions import db
from app.models import Dish


def make_app():
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite+pysqlite:///:memory:",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
    )

    with app.app_context():
        db.create_all()
        db.session.add_all(
            [
                Dish(name="宫保鸡丁", price=26.0, category="川菜"),
                Dish(name="番茄鸡蛋面", price=16.0, category="面食"),
            ]
        )
        db.session.commit()

    return app


def test_home_page() -> None:
    app = make_app()
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    assert "新手美食平台" in response.get_data(as_text=True)


def test_create_dish() -> None:
    app = make_app()
    client = app.test_client()

    response = client.post(
        "/dishes",
        data={"name": "鱼香肉丝", "category": "川菜", "price": "28"},
        follow_redirects=False,
    )
    assert response.status_code == 302


def test_dishes_api() -> None:
    app = make_app()
    client = app.test_client()

    response = client.get("/api/dishes")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
