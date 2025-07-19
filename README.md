# PMS Integration Service

A lightweight FastAPI microservice that fetches booking data from a (mocked) Property Management System (PMS), validates it with Pydantic, and exposes it via a REST endpoint.

## Key Features

- **Clean, layered architecture**  
  - **API** (`src/api/…`)  
  - **Application** (`src/services/…`)  
  - **Domain models** (`src/domain/…`)  
  - **Infrastructure** (`src/infra/…`)
- **Configuration** via `.env` and `pydantic-settings`  
- **Header-based authorization** (X-API-Key) on the `/bookings` route
- **Swagger/OpenAPI UI** at [`/docs`](http://localhost:8000/docs)
- **Docker & Docker Compose** for easy local setup  
- **Comprehensive pytest suite**, with public vs. private client fixtures

---

## Quickstart

### 1. Clone & install dependencies

```bash
git clone https://github.com/kammiii/pms-api-service.git
cd pms-api-service
poetry install
```

### 2. Configuration
Copy the example environment files and set your keys:
```bash
cp .env.example .env
cp .env.example .env.mock
```

### 3. Run with Docker Compose
This will start both the API and a mock PMS endpoint:
```bash
docker-compose up --build
```
- API listens on: `http://localhost:8000`
- Mock PMS listens on: `http://localhost:9000/bookings`

## Testing
Run all tests with:
```bash
poetry run pytest
```
