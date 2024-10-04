from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Configurações globais do projeto, usando variáveis de ambiente.
    """
    # URL base da API do Lichess
    LICHESS_API_BASE_URL: str = "https://lichess.org/api"

    # Configurações do aplicativo FastAPI
    APP_NAME: str = "Chess Data Analysis API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "API para análise de dados de xadrez usando a Lichess API."

    # Configurações de ambiente
    ENVIRONMENT: str = "development"
    DEBUG_MODE: bool = True

    class Config:
        env_file = ".env"  # Define que as variáveis de ambiente serão carregadas a partir de um arquivo .env

# Instância global das configurações
settings = Settings()
