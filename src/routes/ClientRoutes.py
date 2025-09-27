from fastapi import APIRouter
from src.controller import ClientController
from src.domain.Client import Client

router = APIRouter(
    prefix="/clients", tags=["Clients"]
)

# GET endpoints
router.get("/")(ClientController.get_all_clients)
router.get("/{client_id}")(ClientController.get_client_by_id)

# POST endpoint
router.post("/", response_model=Client)(ClientController.create_client)