from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

@app.get("/bookings")
async def bookings(x_api_key: str = Header(..., alias="X-API-Key")):
    if x_api_key != "test-key":
        raise HTTPException(401, "Invalid API Key")
    return {
        "bookings": [
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
        ]
      }
