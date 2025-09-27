from src.domain.Client import Client

FAKE_CLIENTS_DB = []

class ClientService:

    @staticmethod
    def get_all_clients():
        return FAKE_CLIENTS_DB

    @staticmethod
    def get_client_by_id(client_id: int):
        return next((c for c in FAKE_CLIENTS_DB if c["id"] == client_id), None)

    @staticmethod
    def add_client(client: Client):
        new_id = max((c["id"] for c in FAKE_CLIENTS_DB), default=0) + 1
        client_dict = client.model_dump()
        client_dict["id"] = new_id
        FAKE_CLIENTS_DB.append(client_dict)
        return client_dict