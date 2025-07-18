from fastapi import APIRouter, Depends
from typing import List

from src.services.bookings import list_bookings
from src.domain.booking import Booking
from src.infra.pms_client import PMSApiClient, get_pms_client

router = APIRouter(prefix="/api/integrations/pms/bookings")

@router.get("/", response_model=List[Booking])
async def get_bookings(
    client: PMSApiClient = Depends(get_pms_client),
):
    return await list_bookings(client)