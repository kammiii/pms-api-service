from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    PMS_BASE_URL: str = Field("https://mocked-pms.example.com", env="PMS_BASE_URL")
    PMS_TIMEOUT: float = 10.0

def get_config() -> AppConfig:
    return AppConfig()