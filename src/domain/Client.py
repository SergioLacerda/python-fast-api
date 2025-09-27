from pydantic import BaseModel, EmailStr

class Client(BaseModel):
    id: int | None = None
    name: str
    email: EmailStr
