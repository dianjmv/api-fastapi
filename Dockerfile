# Usa una imagen base oficial de Python
FROM python:3.11-alpine

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de configuración de Poetry
COPY pyproject.toml poetry.lock /app/

# Instala Poetry
RUN pip install poetry

# Instala las dependencias del proyecto
RUN poetry install --no-root

# Copia el código fuente de la aplicación
COPY ./app /app/app

# Comando para ejecutar la aplicación
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
