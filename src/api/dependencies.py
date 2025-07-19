from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from src.infra.config import config

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)

def validate_api_key(api_key: str = Security(api_key_header)) -> str:
    if api_key != config.PMM_INTEGRATION_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return api_key
