from fastapi import FastAPI
from src.api.bookings import router as bookings_router

app = FastAPI()
app.include_router(bookings_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the PMS Integration Service"}

@app.get("/health")
async def health():
    return {"status": "ok"}
