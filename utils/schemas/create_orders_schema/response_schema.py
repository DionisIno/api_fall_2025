from pydantic import BaseModel


class CreateOrderResponseSchema(BaseModel):
    created: bool
    orderId: str