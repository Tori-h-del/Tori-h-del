from app import create_app


def test_home_page() -> None:
    app = create_app()
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    assert "新手美食平台" in response.get_data(as_text=True)


def test_create_dish() -> None:
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/dishes",
        data={"name": "鱼香肉丝", "category": "川菜", "price": "28"},
        follow_redirects=False,
    )
    assert response.status_code == 302


def test_dishes_api() -> None:
    app = create_app()
    client = app.test_client()

    response = client.get("/api/dishes")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
