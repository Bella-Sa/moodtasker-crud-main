from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env (se existir)
load_dotenv()

# Variáveis de ambiente para conexão com o banco
DB_USER = os.getenv("DB_USER", "seu_usuario")
DB_PASSWORD = os.getenv("DB_PASSWORD", "sua_senha")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "seu_banco")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Cria engine de conexão com banco
engine = create_engine(DATABASE_URL, echo=True)


# Cria uma classe base para as entidades herdarem (ORM)
Base: DeclarativeMeta = declarative_base()

# Cria a factory de sessões (interação com o banco)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency para injetar sessão no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
