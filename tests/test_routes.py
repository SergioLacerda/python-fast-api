import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# --- Existing tests ---
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_get_all_clients():
    response = client.get("/clients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_client_by_id_found():
    response = client.get("/clients/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

def test_get_client_by_id_not_found():
    response = client.get("/clients/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Client not found"

def test_create_client_valid():
    payload = {"name": "Charlie", "email": "charlie@example.com"}
    response = client.post("/clients", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Charlie"
    assert data["email"] == "charlie@example.com"
    assert "id" in data 

def test_create_client_missing_field():
    payload = {"name": "Charlie"}
    response = client.post("/clients", json=payload)
    assert response.status_code == 422

def test_create_client_invalid_email():
    payload = {"name": "Charlie", "email": "not-an-email"}
    response = client.post("/clients", json=payload)
    assert response.status_code == 422
