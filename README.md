# API PDV

API REST para PDV, esta  bonita la neta

## Estructura del Proyecto

```
api-pdv/
├── main.py                 # Aplicación principal FastAPI
├── database.py            # Configuración de SQLAlchemy
├── dependencies.py        # Dependencies para FastAPI
├── models/               # Modelos de SQLAlchemy
│   └── usuario.py
├── schemas/              # Schemas de Pydantic
│   └── usuario.py
├── dao/                  # Data Access Objects (operaciones DB)
│   └── usuario_dao.py
├── services/             # Lógica de negocio
│   ├── usuario.py
│   └── auth_service.py
├── routers/              # Endpoints FastAPI
│   ├── usuario.py
│   └── auth_router.py
└── utils/                # Utilidades
    └── security.py       # Funciones de seguridad y JWT
```


## Instalación

### Rerequisitos

- Python 3.13+
- PostgreSQL 12+
- Poetry

### Instalar dependencias

```bash
poetry install

```

## Correr proyecto
```bash

poetry run uvicorn main:app --reload

```

## Producción

Para producción, asegúrate de:

1. Cambiar `SECRET_KEY` a un secret key de vdd y no el de jochis
2. Configurar CORS con orígenes específicos xd
3. Usar HTTPS
4. Configurar variables de entorno de forma segura
5. Deshabilitar `echo=True` en el engine de SQLAlchemy
6. Usar un servidor ASGI de producción como Gunicorn con Uvicorn workers

```bash
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

