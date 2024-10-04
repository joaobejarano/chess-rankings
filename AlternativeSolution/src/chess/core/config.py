from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Global project settings, using environment variables.
    """
    # Lichess API Base URL
    LICHESS_API_BASE_URL: str = "https://lichess.org/api"

    # FastAPI Application Settings
    APP_NAME: str = "Chess Data Analysis API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "API for analyzing chess data using the Lichess API."

    # Environment settings
    ENVIRONMENT: str = "development"
    DEBUG_MODE: bool = True

    class Config:
        env_file = ".env"

# Global instance of settings
settings = Settings()
