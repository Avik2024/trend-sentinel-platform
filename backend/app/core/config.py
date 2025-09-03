import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Trend Sentinel Backend"
    DATABASE_URL: str = "sqlite:///./trends.db"

    class Config:
        env_file = ".env"

settings = Settings()
