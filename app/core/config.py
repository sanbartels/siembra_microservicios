from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLSERVER_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
