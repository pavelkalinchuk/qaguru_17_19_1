from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict


class Settings(BaseSettings):
    BROWSERSTACK_USER_NAME: str = Field(..., alias="BROWSERSTACK_USER_NAME")
    BROWSERSTACK_ACCESS_KEY: str = Field(..., alias="BROWSERSTACK_ACCESS_KEY")
    BROWSERSTACK_URL: str = Field(..., alias="BROWSERSTACK_URL")

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
