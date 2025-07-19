from typing import List
from fastapi import HTTPException
from pydantic import TypeAdapter, ValidationError

from src.infra.pms_client import PMSApiError, PMSApiClient
from src.domain.booking import Booking

BookingListAdapter = TypeAdapter(List[Booking])

async def list_bookings(
    client: PMSApiClient,
) -> List[Booking]:
    try:
        resp = await client.get_bookings()
    except PMSApiError as e:
        raise HTTPException(status_code=502, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    try:
        return BookingListAdapter.validate_python(resp.json().get("bookings", []))
    except ValidationError as e:
        raise HTTPException(status_code=502, detail=f"Validation failed: {e}")