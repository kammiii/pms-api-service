# PMS Integration Service

A lightweight FastAPI microservice that fetches booking data from a (mocked) Property Management System (PMS), validates it against a Pydantic `Booking` model, and exposes it via a REST endpoint.

## Features

- Four-layer architecture: **API** → **Application** → **Domain** → **Infrastructure**
- Async HTTP client for PMS with FastAPI dependency injection  
- Full test coverage with pytest and FastAPI’s TestClient  

---

## Quickstart

### 1. Clone & install dependencies

```bash
git clone <repo-url>
cd pms-integration-service
poetry install
```

### 2. Configure
Copy the sample environment files:

```bash
cp .env.test .env
```

### 3. Run the app
```bash
uvicorn main:app --reload --port 8000
```

### 4. Run tests
```bash
poetry run pytest
```