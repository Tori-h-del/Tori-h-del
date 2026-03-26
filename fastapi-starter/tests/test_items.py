from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_item() -> None:
    create_response = client.post(
        "/api/v1/items",
        json={"name": "键盘", "description": "机械键盘"},
    )
    assert create_response.status_code == 201

    created_item = create_response.json()
    item_id = created_item["id"]

    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "键盘"
