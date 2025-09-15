# backend/app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Cria o "motor" de conexão com o banco de dados
engine = create_engine(
    settings.get_database_url(),
    # pool_pre_ping=True é recomendado para conexões que podem ficar ociosas
    pool_pre_ping=True 
)

# Cria uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os nossos modelos ORM
Base = declarative_base()

# Dependência para injeção no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()