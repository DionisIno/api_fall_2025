from pydantic import BaseModel


class TokenResponseSchema(BaseModel):
    accessToken: str