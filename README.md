# Siembra Microservice

Microservicio FastAPI para gestión de información de siembra (proyectos, ofertas y demandas) conectado a SQL Server.

## 🚀 Características

- API RESTful con FastAPI
- Conexión a SQL Server mediante SQLAlchemy y pyODBC
- Endpoints paginados con filtros avanzados
- Búsqueda normalizada (sin tildes) para especies
- Headers de rango HTTP (Content-Range, X-Total-Count)
- Dockerizado y listo para producción

## 📋 Requisitos Previos

- **Docker** ≥ 20.x
- **Docker Compose** ≥ 2.x
- La red Docker `agrosavia-network` creada
- Acceso a una instancia de SQL Server con la base de datos `db_siembra`

### Crear la red Docker

```bash
docker network create agrosavia-network
```

## ⚙️ Configuración

### 1. Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto basado en:

```env
SQLSERVER_URL=mssql+pyodbc://usuario:contraseña@host:puerto/db_siembra?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes
```

**Ejemplo:**
```env
SQLSERVER_URL=mssql+pyodbc://admin:MiPassword123@192.168.1.100:1433/db_siembra?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes
```

> **Nota:** Ajusta `usuario`, `contraseña`, `host`, `puerto` según tu configuración de SQL Server.

## 🐳 Ejecución con Docker

### Levantar el servicio

```bash
docker-compose up -d
```

### Ver logs

```bash
docker-compose logs -f siembra-service
```

### Detener el servicio

```bash
docker-compose down
```

## 📚 Endpoints Disponibles

El servicio estará disponible en `http://localhost:8002` (puerto configurado en docker-compose.yml)

### Documentación interactiva

- **Swagger UI**: http://localhost:8002/docs
- **ReDoc**: http://localhost:8002/redoc

## 🛠️ Tecnologías

- **FastAPI** 0.115.6 - Framework web moderno
- **SQLAlchemy** 2.0.29 - ORM para bases de datos
- **pyODBC** 5.1.0 - Driver ODBC para SQL Server
- **Pydantic** 2.11.3 - Validación de datos
- **Uvicorn** 0.32.0 - Servidor ASGI
- **Docker** - Containerización

## 📝 Notas

- El puerto expuesto es `8002` (configurable en docker-compose.yml)
- La búsqueda por especies es **case-insensitive** y normalizada (ignora tildes)
- Los filtros por `departamento`, `ciudad` y `region` son por **coincidencia exacta** (ID)
- El límite máximo de registros por petición es **200**
