from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine
from app.api.router import api_router  # 🔹 Import del router central

# 🚀 Inicialización de la aplicación FastAPI
app = FastAPI(
    title="Siembra Service",
    version="1.0.0",
    description="Microservicio base para conexión y servicios sobre SQL Server (Siembra DB)"
)

# 🔍 Ruta de prueba de conexión
@app.get("/test-db", tags=["Siembra"])
def test_db():
    """Verifica conexión con SQL Server."""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT name FROM sys.databases"))
            dbs = [row[0] for row in result]
        return {"status": "✅ Connected", "databases": dbs}
    except Exception as e:
        return {"status": "❌ Error", "details": str(e)}

# 🧩 Registrar routers de módulos
app.include_router(api_router)
