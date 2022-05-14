from fastapi.testclient import TestClient

from auth import AuthHandler
from main import app

client = TestClient(app)


def test_get_users_without_token():
    response = client.get("/users/")
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}


def test_get_users_with_token():
    auth = AuthHandler()
    token = auth.encode_token(user_id=1)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/", headers=headers)
    assert response.status_code == 200
