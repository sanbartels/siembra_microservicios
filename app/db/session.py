from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# ⚙️ Crear motor de conexión
engine = create_engine(settings.SQLSERVER_URL)

# 🧩 Crear sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🧱 Base para los modelos ORM
Base = declarative_base()

# 🔁 Dependencia de sesión (para usar en endpoints)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
