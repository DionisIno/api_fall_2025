import os
from urllib.parse import urlencode

import requests

from data.endpoints import Endpoints
from data.generator.generator import Generator
import pytest
from dotenv import load_dotenv

from modules.registered_module import RegisteredModule
from utils.schemas.registered_schema.request_schema import RegisteredRequestSchema

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
generator = Generator()
module = RegisteredModule()
endpoint = Endpoints()


@pytest.fixture(scope="session")
def get_auth_token():
    user_info = next(generator.registered_data())
    request_body = module.prepare_data(
            schema=RegisteredRequestSchema,
            data=user_info
        )
    response = requests.post(
            url=f"{endpoint.base_url}{endpoint.api_client_url}",
            data=request_body
        )
    token = response.json()["accessToken"]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    return headers

@pytest.fixture
def create_endpoint():

    def _build_endpoint(path: str, **kwargs):
        url = fr"{BASE_URL}{path}"
        params = {key: value for key, value in kwargs.items() if value is not None}
        return f"{url}?{urlencode(params, doseq=True)}" if params else url
    return _build_endpoint