# Proyecto de FastAPI con MongoDB

Este proyecto es un ejemplo de una API Backend-for-Frontend (BFF) desarrollada con FastAPI y MongoDB. La API se encarga de integrar datos de la colección `client-portfolio` y proporciona endpoints para acceder a estos datos.

## Estructura del Proyecto

El proyecto sigue una estructura de Clean Architecture para mantener el código organizado y modular. Aquí está la estructura del proyecto:
```
fastapi-mongo/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── config.py
│ ├── core/
│ │ ├── init.py
│ │ ├── models.py
│ │ ├── schemas.py
│ │ └── services.py
│ ├── api/
│ │ ├── init.py
│ │ └── routes.py
│ ├── repositories/
│ │ ├── init.py
│ │ └── client_portfolio_repository.py
│ └── tests/
│ ├── init.py
│ ├── test_client_portfolio.py
│ └── test_main.py
├── pyproject.toml
├── docker-compose.yml
└── init-mongo.js
```

### Descripción de los Directorios y Archivos

- **app/**: Contiene la lógica principal de la aplicación.
  - **main.py**: Archivo principal que inicia la aplicación.
  - **config.py**: Configuración de la conexión a MongoDB.
  - **core/**: Contiene los modelos, esquemas y servicios.
    - `models.py`: Define los modelos Pydantic.
    - `schemas.py`: Define los esquemas Pydantic.
    - `services.py`: Contiene la lógica de negocio.
  - **api/**: Define las rutas de la API.
    - `routes.py`: Define los endpoints de la API.
  - **repositories/**: Contiene la lógica de acceso a la base de datos.
    - `client_portfolio_repository.py`: Implementa las operaciones de MongoDB para `client-portfolio`.
  - **tests/**: Contiene los tests para la aplicación.
- **pyproject.toml**: Archivo de configuración de Poetry y dependencias.
- **docker-compose.yml**: Define los servicios Docker, incluyendo MongoDB y la aplicación FastAPI.
- **init-mongo.js**: Script de inicialización de MongoDB para poblar la colección `client-portfolio`.

## Configuración y Ejecución

### Prerrequisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Poetry](https://python-poetry.org/docs/#installation)

### Instrucciones para Ejecutar el Proyecto

1. **Clonar el Repositorio**

   ```sh
   git clone https://github.com/tu-usuario/fastapi-mongo.git
   cd fastapi-mongo
Instalar Dependencias

poetry install
Construir y Levantar los Contenedores

docker-compose up --build
Verificar la Inicialización de los Datos

Puedes verificar que los datos se han insertado correctamente en MongoDB utilizando la consola de MongoDB o cualquier cliente MongoDB como MongoDB Compass.

mongo --port 27018
use clientPortfolioDB
db["client-portfolio"].find().pretty()
Probar los Endpoints

Puedes usar curl o cualquier herramienta como Postman para probar los endpoints de la API.

curl http://localhost:8000/api/client-portfolio
curl http://localhost:8000/api/client-portfolio/6661c77b343c9f02ad846a9f
Pruebas
Ejecutar los Tests

Ejecuta los tests utilizando pytest:

poetry run pytest
Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.


Este `README.md` proporciona una descripción clara de la estructura del proyecto, cómo configurarlo y ejecutarlo, y cómo probar los endpoints. Si necesitas más detalles o ajustes específicos, no dudes en decírmelo.
