import pytest
from fastapi import status
import httpx

from main import app
from src.infra.pms_client import PMSApiError, get_pms_client

class ApiClientMock:
    def __init__(self, response=None, error=None):
        self._response = response
        self._error = error

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        return False

    async def get_bookings(self):
        if self._error:
            raise self._error
        return self._response

@pytest.fixture(autouse=True)
def clear_overrides():
    """Clear dependency overrides before and after each test."""
    app.dependency_overrides.clear()
    yield
    app.dependency_overrides.clear()

class TestPMSBookingsApi:
    @pytest.fixture
    def override_pms_client(self):
      def _override(response=None, error=None):
          async def _get_pms_client():
              yield ApiClientMock(response=response, error=error)
          app.dependency_overrides[get_pms_client] = _get_pms_client
      return _override
    
    @pytest.fixture
    def booking(self):
        return {
            "pms_id": "123e4567-e89b-12d3-a456-426614174000",
            "guest_name": "John Doe",
            "room_number": "101",
            "check_in": "2023-10-01",
            "check_out": "2023-10-05",
            "status": "confirmed",
        }

    @pytest.fixture
    def resp(self,booking):
        return httpx.Response(
            status_code=200,
            json=[booking],
            request=httpx.Request("GET", "/api/bookings"),
        )

    @pytest.mark.asyncio
    async def test_success_override(self, override_pms_client, client, booking, resp):
        override_pms_client(response=resp)
        resp = client.get("/api/integrations/pms/bookings/")
        assert resp.status_code == status.HTTP_200_OK
        assert resp.json() == [booking]

    @pytest.mark.asyncio
    async def test_502_on_pms_error(self, client, override_pms_client):
        override_pms_client(error=PMSApiError("upstream down"))
        resp = client.get("/api/integrations/pms/bookings/")
        assert resp.status_code == status.HTTP_502_BAD_GATEWAY
        assert resp.json()["detail"] == "upstream down"

    @pytest.mark.asyncio
    async def test_500_on_unexpected_exception(self, client, override_pms_client):
        override_pms_client(error=RuntimeError("boom"))
        resp = client.get("/api/integrations/pms/bookings/")
        assert resp.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert resp.json()["detail"] == "Internal Server Error"
