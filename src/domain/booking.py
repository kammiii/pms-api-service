from uuid import UUID
from datetime import date
from pydantic import BaseModel

class Booking(BaseModel):
    pms_id: UUID
    guest_name: str
    room_number: str
    check_in: date
    check_out: date
    status: str
