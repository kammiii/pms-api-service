import pytest
from fastapi.testclient import TestClient

from main import app
from src.infra.config import config

@pytest.fixture(scope="session")
def app_client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def public_client(app_client):
    return app_client

@pytest.fixture
def private_client(app_client):
    headers = app_client.headers.copy()
    headers.update({"X-API-Key": config.PMM_INTEGRATION_API_KEY})
    app_client.headers = headers
    return app_client
