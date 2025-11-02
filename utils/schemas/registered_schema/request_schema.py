from pydantic import BaseModel


class RegisteredRequestSchema(BaseModel):
    clientName: str
    clientEmail: str