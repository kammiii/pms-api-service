import httpx
from fastapi import Depends
from typing import AsyncGenerator
from src.infra.config import AppConfig, get_config

class PMSApiError(Exception):
    """Raised when the PMS API call fails or returns unexpected data."""
    pass

class PMSApiClient(httpx.AsyncClient):
    def __init__(self, base_url: str, timeout: float):
        super().__init__(base_url=base_url, timeout=timeout)

    async def get_bookings(self) -> httpx.Response:
        resp = httpx.Response(
            status_code=200,
            json=[
              {
                "pms_id": "123e4567-e89b-12d3-a456-426614174000",
                "guest_name": "John Doe",
                "room_number": "101",
                "check_in": "2023-10-01",
                "check_out": "2023-10-05",
                "status": "confirmed"
              },
              {
                "pms_id": "123e4567-e89b-12d3-a456-426614174001",
                "guest_name": "Jane Smith",
                "room_number": "102",
                "check_in": "2023-10-02",
                "check_out": "2023-10-06",
                "status": "checked_in"
              }
            ],
            request=self.build_request("GET", "/api/bookings")
        )
        resp.raise_for_status()
        return resp



async def get_pms_client(
    config: AppConfig = Depends(get_config)
) -> AsyncGenerator[PMSApiClient, None]:
    async with PMSApiClient(
        base_url=config.PMS_BASE_URL,
        timeout=config.PMS_TIMEOUT
    ) as client:
        yield client
