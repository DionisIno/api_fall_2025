from pydantic import BaseModel

class CreateOrdesRequestSchema(BaseModel):
    bookId: int
    customerName: str