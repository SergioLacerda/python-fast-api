import pytest
from src.service.ClientService import ClientService, FAKE_CLIENTS_DB
from src.domain.Client import Client

@pytest.fixture(autouse=True)
def clear_db():
    FAKE_CLIENTS_DB.clear()

def test_get_all_clients_empty():
    clients = ClientService.get_all_clients()
    assert clients == [] 

def test_add_client():
    client_data = Client(name="Alice", email="alice@example.com")
    result = ClientService.add_client(client_data)
    
    assert result["name"] == "Alice"
    assert result["email"] == "alice@example.com"
    assert "id" in result
    assert result["id"] == 1
    
    all_clients = ClientService.get_all_clients()
    assert len(all_clients) == 1
    assert all_clients[0]["id"] == result["id"]

def test_get_client_by_id_found():
    client_data = Client(name="Bob", email="bob@example.com")
    added = ClientService.add_client(client_data)
    
    client = ClientService.get_client_by_id(added["id"])
    assert client is not None
    assert client["name"] == "Bob"

def test_get_client_by_id_not_found():
    client = ClientService.get_client_by_id(999)
    assert client is None

def test_add_multiple_clients_ids_increment():
    c1 = ClientService.add_client(Client(name="C1", email="c1@example.com"))
    c2 = ClientService.add_client(Client(name="C2", email="c2@example.com"))
    
    assert c1["id"] == 1
    assert c2["id"] == 2
