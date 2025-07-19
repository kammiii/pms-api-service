from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    PMS_BASE_URL: str = Field("http://mock-pms:9000", env="PMS_BASE_URL")
    PMS_API_KEY: str = Field("test-key", env="PMS_API_KEY")
    PMM_INTEGRATION_API_KEY: str = Field('my-api', env="PMM_INTEGRATION_API_KEY")

config = AppConfig()
