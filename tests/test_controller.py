import pytest
from fastapi import HTTPException
from src.controller import ClientController
from src.service.ClientService import ClientService
from src.domain.Client import Client

def test_get_all_clients():
    clients = ClientController.get_all_clients()
    assert isinstance(clients, list)

def test_get_client_by_id_found():
    ClientService.add_client(Client(name="Alice", email="alice@example.com"))

    client = ClientController.get_client_by_id(1)
    assert client["name"] == "Alice"

def test_get_client_by_id_not_found():
    try:
        ClientController.get_client_by_id(999)
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "Client not found"
