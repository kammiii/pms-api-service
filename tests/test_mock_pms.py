import pytest
from fastapi import status
from fastapi.testclient import TestClient
from src.infra.mock_pms import app

class TestMockPMSAPI:
    API_KEY = 'test-key'

    @pytest.fixture
    def mock_pms_client(self):
        with TestClient(app) as c:
          yield c

    def test_mocked_bookings_success(self, mock_pms_client):
        resp = mock_pms_client.get("/bookings", headers={"X-API-Key": self.API_KEY})
        assert resp.status_code == status.HTTP_200_OK

    def test_mocked_bookings_unauthorized(self, mock_pms_client):
        resp = mock_pms_client.get("/bookings", headers={"X-API-Key": 'key'})
        assert resp.status_code == status.HTTP_401_UNAUTHORIZED
