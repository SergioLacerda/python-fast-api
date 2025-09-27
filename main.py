from fastapi import FastAPI
from src.routes import ClientRoutes

app = FastAPI()

app.include_router(ClientRoutes.router)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is healthy 🚀"}
