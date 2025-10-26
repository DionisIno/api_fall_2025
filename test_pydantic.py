import requests
from pydantic import BaseModel, Field


class UserRegisteredSchema(BaseModel):
    clientName: str
    clientEmail: str

class TokenResponseSchema(BaseModel):
    access_token: str = Field(..., alias='accessToken')

def test1():
    url = "https://simple-books-api.click/api-clients"
    data = {
           "clientName": "Kenya-704",
           "clientEmail": "Eliseo_Feil8@gmail.com"
        }
    response = requests.post(
        url=url,
        json=data
    )
    print(response.json())

def test2():
    url = "https://simple-books-api.click/api-clients"
    data = {
           "clientName": "Kenya-706",
           "clientEmail": "Eliseo_Feil89@gmail.com"
        }
    response = requests.post(
        url=url,
        json=data
    )
    try:
        TokenResponseSchema.model_validate(response.json())
    except ValueError as e:
        raise ValueError(f"Неверный формат тела ответа. {e}")