from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Tender Sniper API"
    DATABASE_URL: str = "sqlite:///./tender.db"
    TINYFISH_API_KEY: str = ""
    OPENAI_API_KEY: str = ""

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
