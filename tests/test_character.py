from fastapi.testclient import TestClient
import sys
import os
import pytest

# Get the absolute path to the project's root directory (one level up from the 'tests' folder)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the project root to sys.path if it's not already there
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from main import app


client = TestClient(app)

global_character_id = 1  # Default character ID for testing

@pytest.fixture(scope="module")
def auth_token():
    response = client.post(
        "/api/auth/login", json={"email": "ash@gmail.com", "password": "pass123"}
    )
    assert response.status_code == 200
    return response.json().get("access_token") or response.json().get("token")


def test_character_list():
    response = client.get("/api")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert "items" in data
    assert isinstance(data["items"], list)
    assert "total" in data
    assert "size" in data
    assert "page" in data
    assert "pages" in data

    for item in data["items"]:
        assert "id" in item
        assert "character" in item
        assert "power_level" in item
        assert isinstance(item["id"], int)
        assert isinstance(item["character"], str)
        assert isinstance(item["power_level"], str)


def test_character_get_by_id():
    response = client.get("/api/1")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert "id" in data
    assert "character" in data
    assert "power_level" in data
    assert isinstance(data["id"], int)
    assert isinstance(data["character"], str)
    assert isinstance(data["power_level"], str)


def test_character_create(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post(
        "/api",
        json={
            "character": "Test Character",
            "power_level": "9000",
            "saga_or_movie": "Saiyan Saga",
            "dragon_ball_series": "Dragon Ball Z"
        },
        headers=headers
    )
    assert response.status_code == 201
    data = response.json()
    assert isinstance(data, dict)
    assert "id" in data
    assert "character" in data
    assert "power_level" in data

    # set global character ID for further tests
    global global_character_id
    global_character_id = data["id"]


def test_character_update(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.put(
        f"/api/{global_character_id}",
        json={"character": "Updated Character", "power_level": "10000"},
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "id" in data
    assert "character" in data
    assert "power_level" in data
    assert data["id"] == global_character_id
    assert data["character"] == "Updated Character"
    assert data["power_level"] == "10000"


def test_character_delete(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.delete(f"/api/{global_character_id}", headers=headers)
    assert response.status_code == 204



