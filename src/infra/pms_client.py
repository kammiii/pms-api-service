import httpx
from typing import AsyncGenerator
from src.infra.config import config

class PMSApiError(Exception):
    """Raised when the PMS API call fails or returns unexpected data."""
    pass

class PMSApiAuth(httpx.Auth):
    def auth_flow(self, request):
        request.headers["X-API-Key"] = config.PMS_API_KEY
        yield request

class PMSApiClient(httpx.AsyncClient):
    def __init__(self, **kwargs):
        super().__init__(
            auth=PMSApiAuth(),
            base_url=config.PMS_BASE_URL,
            **kwargs,
        )

    async def get_bookings(self) -> httpx.Response:
        resp = await self.get('/bookings')
        resp.raise_for_status()
        return resp

async def get_pms_client() -> AsyncGenerator[PMSApiClient, None]:
    async with PMSApiClient() as client:
        yield client
