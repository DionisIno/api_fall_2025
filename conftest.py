import os
from urllib.parse import urlencode

import pytest
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

@pytest.fixture
def create_endpoint():

    def _build_endpoint(path: str, **kwargs):
        url = fr"{BASE_URL}{path}"
        params = {key: value for key, value in kwargs.items() if value is not None}
        return f"{url}?{urlencode(params, doseq=True)}" if params else url
    return _build_endpoint