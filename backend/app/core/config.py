# backend/app/core/config.py
import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from google.cloud import secretmanager

class Settings(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    PROJECT_ID: str = os.getenv("PROJECT_ID", "meal-ai-development")
    
    # Configurações do Banco de Dados
    DB_USER: str = os.getenv("POSTGRES_USER", "user")
    DB_PASSWORD_SECRET_NAME: str = "mealia-db-password" # Nome do segredo no Secret Manager
    DB_NAME: str = os.getenv("POSTGRES_DB", "mealiadb")
    DB_HOST: str = os.getenv("DB_HOST", "db") # 'db' é o nome do serviço no docker-compose
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    
    # Cloud SQL (apenas para produção)
    INSTANCE_CONNECTION_NAME: str = f"{PROJECT_ID}:us-central1:mealia-db"

    DATABASE_URL_LOCAL: str = f"postgresql+psycopg2://{DB_USER}:{os.getenv('POSTGRES_PASSWORD')}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    def get_database_url(self) -> str:
        if self.ENVIRONMENT == "production":
            # Obtém a senha do Secret Manager
            password = self._get_secret(self.DB_PASSWORD_SECRET_NAME)
            
            # Conexão via Unix Socket para Cloud Run
            return f"postgresql+psycopg2://{self.DB_USER}:{password}@/{self.DB_NAME}?host=/cloudsql/{self.INSTANCE_CONNECTION_NAME}"
        else:
            return self.DATABASE_URL_LOCAL

    def _get_secret(self, secret_name: str) -> str:
        try:
            client = secretmanager.SecretManagerServiceClient()
            secret_version_name = f"projects/{self.PROJECT_ID}/secrets/{secret_name}/versions/latest"
            response = client.access_secret_version(request={"name": secret_version_name})
            return response.payload.data.decode("UTF-8")
        except Exception as e:
            # Em desenvolvimento, podemos não ter acesso, então retornamos um valor padrão
            if self.ENVIRONMENT != "production":
                return os.getenv('POSTGRES_PASSWORD', 'password')
            raise e

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()