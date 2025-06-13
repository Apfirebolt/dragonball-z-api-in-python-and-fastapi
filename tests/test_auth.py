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


@pytest.fixture(scope="module")
def auth_token():
    response = client.post(
        "/api/auth/login", json={"email": "ash@gmail.com", "password": "pass123"}
    )
    assert response.status_code == 200
    return response.json().get("access_token") or response.json().get("token")


def test_register_user():
    response = client.post(
        "/api/auth/register",
        json={
            "email": "dummyuser@example.com",
            "password": "dummyPass123",
            "username": "dummyuser"
        }
    )
    # print error response if registration fails
    assert response.status_code == 400


def test_login():
    # Ensure the user exists (register if needed)
    response = client.post(
        "/api/auth/login", json={"email": "dummyuser@example.com", "password": "dummyPass123"}
    )
    # print error response if login fails
    if response.status_code != 200:
        print("Login failed:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data or "token" in data


def test_profile_data(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/api/auth/profile", headers=headers)
    assert response.status_code == 200
    data = response.json()


def test_all_users():
    response = client.get("/api/auth/users")
    if response.status_code != 200:
        print("All users error response:", response.json())
    else:
        print("All users response:", response.json())
    assert response.status_code == 200


def test_get_user_by_id():
    response = client.get("/api/auth/users/1")
    if response.status_code != 200:
        print("Get user by ID error response:", response.json())
    else:
        print("Get user by ID response:", response.json())
    assert response.status_code == 200
    data = response.json()

