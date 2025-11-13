FROM python:3.11-slim

# Instalar dependencias base
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl gnupg unixodbc unixodbc-dev apt-transport-https ca-certificates && \
    # Descargar clave GPG Microsoft
    curl https://packages.microsoft.com/keys/microsoft.asc \
        | gpg --dearmor \
        | tee /usr/share/keyrings/microsoft-prod.gpg > /dev/null && \
    # Crear repositorio Microsoft para Debian 12 manualmente (fix definitivo)
    echo "deb [signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
        > /etc/apt/sources.list.d/mssql-release.list && \
    # Actualizar repos y instalar ODBC 18
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    # Limpiar
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
