from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the PMS Integration Service"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}
