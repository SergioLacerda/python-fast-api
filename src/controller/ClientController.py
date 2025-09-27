from fastapi import HTTPException
from src.service.ClientService import ClientService
from src.domain.Client import Client

def get_all_clients():
    return ClientService.get_all_clients()

def get_client_by_id(client_id: int):
    client = ClientService.get_client_by_id(client_id)
    if client:
        return client
    raise HTTPException(status_code=404, detail="Client not found")

def create_client(client: Client):
    return ClientService.add_client(client)