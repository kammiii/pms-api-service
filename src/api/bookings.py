from fastapi import APIRouter, Depends
from typing import List
from src.services.bookings import list_bookings
from src.domain.booking import Booking
from src.infra.pms_client import get_pms_client, PMSApiClient
from src.api.dependencies import validate_api_key

router = APIRouter(prefix="/api/integrations/pms/bookings")

@router.get(
  "/",
  response_model=List[Booking],
  summary="List bookings from PMS",
  responses={
      401: {"description": "Invalid API key"},
      502: {"description": "PMS API error"},
  },
  dependencies=[Depends(validate_api_key)]
)
async def get_bookings(
    client: PMSApiClient = Depends(get_pms_client)
):
    return await list_bookings(client)