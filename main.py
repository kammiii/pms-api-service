from fastapi import FastAPI
from src.api.bookings import router as bookings_router

app = FastAPI(
    title="PMS Integration Service",
    version="1.0.0",
    description="Resiliently fetch bookings from PMS",
    openapi_tags=[{"name": "bookings", "description": "Booking operations"}],
)
app.include_router(bookings_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the PMS Integration Service"}

@app.get("/health")
async def health():
    return {"status": "ok"}
