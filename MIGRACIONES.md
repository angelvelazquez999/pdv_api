# Guía de Migraciones con Alembic

## ¿Qué es Alembic?
Alembic es una herramienta de migración de bases de datos para SQLAlchemy. Permite:
- **Versionar** los cambios del esquema de la base de datos
- **Sincronizar** automáticamente los modelos Python con la base de datos
- **Rastrear** el historial de cambios
- **Revertir** cambios si es necesario

## Estructura de Archivos

```
alembic/
├── versions/          # Carpeta con todas las migraciones
│   └── xxxxx_inicial.py
├── env.py            # Configuración de conexión y modelos
├── README
└── script.py.mako    # Template para nuevas migraciones
alembic.ini           # Configuración principal
```

## Comandos Principales

### 1. Crear una nueva migración (autogenerada)
```bash
poetry run alembic revision --autogenerate -m "descripción del cambio"
```
Detecta automáticamente cambios entre tus modelos y la base de datos actual.

### 2. Crear una migración vacía (manual)
```bash
poetry run alembic revision -m "descripción del cambio"
```
Crea un archivo vacío para escribir la migración manualmente.

### 3. Aplicar migraciones
```bash
# Aplicar todas las migraciones pendientes
poetry run alembic upgrade head

# Aplicar hasta una versión específica
poetry run alembic upgrade <revision_id>

# Aplicar solo la siguiente migración
poetry run alembic upgrade +1
```

### 4. Revertir migraciones
```bash
# Revertir la última migración
poetry run alembic downgrade -1

# Revertir hasta una versión específica
poetry run alembic downgrade <revision_id>

# Revertir todas las migraciones
poetry run alembic downgrade base
```

### 5. Ver historial
```bash
# Ver migraciones actuales
poetry run alembic current

# Ver historial de migraciones
poetry run alembic history

# Ver migraciones pendientes
poetry run alembic history --verbose
```

## Flujo de Trabajo Típico

### Escenario 1: Agregar un nuevo campo a Usuario
```python
# 1. Modificar el modelo en models/usuario.py
class Usuario(Base):
    # ... campos existentes ...
    telefono = Column(String(20), nullable=True)  # NUEVO CAMPO
```

```bash
# 2. Crear la migración
poetry run alembic revision --autogenerate -m "agregar campo telefono a usuario"

# 3. Revisar el archivo generado en alembic/versions/
# 4. Aplicar la migración
poetry run alembic upgrade head
```

### Escenario 2: Crear una nueva tabla
```python
# 1. Crear el modelo en models/producto.py
class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
```

```bash
# 2. Importar el modelo en alembic/env.py
# from models.producto import Producto

# 3. Crear la migración
poetry run alembic revision --autogenerate -m "crear tabla productos"

# 4. Aplicar
poetry run alembic upgrade head
```

### Escenario 3: Renombrar una columna
```python
# En la migración generada, Alembic podría detectarlo como:
# - Eliminar columna antigua
# - Crear columna nueva

# CORREGIR MANUALMENTE para no perder datos:
def upgrade():
    op.alter_column('usuarios', 'nombre_antiguo',
                    new_column_name='nombre_nuevo')

def downgrade():
    op.alter_column('usuarios', 'nombre_nuevo',
                    new_column_name='nombre_antiguo')
```

## Buenas Prácticas

1. **Siempre revisar las migraciones autogeneradas** antes de aplicarlas
2. **Probar las migraciones en desarrollo** antes de producción
3. **Hacer commits** después de cada migración exitosa
4. **Nombres descriptivos**: `agregar_campo_telefono` mejor que `actualizacion`
5. **Una migración por cambio lógico**: No mezclar cambios no relacionados
6. **Implementar `downgrade()`**: Siempre permitir revertir cambios
7. **No modificar migraciones ya aplicadas**: Crear nuevas migraciones

## Comandos Útiles

```bash
# Ver SQL que se ejecutará sin aplicarlo
poetry run alembic upgrade head --sql

# Marcar la base de datos como si estuviera en cierta versión (sin ejecutar SQL)
poetry run alembic stamp head

# Ver diferencias entre modelos y base de datos
poetry run alembic check
```

## Troubleshooting

### Error: "Can't locate revision"
```bash
# La base de datos no tiene el historial de migraciones
poetry run alembic stamp head
```

### Error: "Target database is not up to date"
```bash
# Aplicar migraciones pendientes
poetry run alembic upgrade head
```

### Resetear todo (PELIGRO: borra datos)
```bash
# 1. Revertir todas las migraciones
poetry run alembic downgrade base

# 2. Borrar la carpeta versions/
# 3. Crear migración inicial
poetry run alembic revision --autogenerate -m "inicial"

# 4. Aplicar
poetry run alembic upgrade head
```

## Ejemplo de Archivo de Migración

```python
"""agregar campo telefono a usuario

Revision ID: abc123def456
Revises: xyz789abc012
Create Date: 2025-11-26 14:30:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'abc123def456'
down_revision = 'xyz789abc012'
branch_labels = None
depends_on = None

def upgrade():
    # Cambios a aplicar
    op.add_column('usuarios', sa.Column('telefono', sa.String(20), nullable=True))

def downgrade():
    # Revertir los cambios
    op.drop_column('usuarios', 'telefono')
```

## Integración con Git

```bash
# Después de crear una migración
git add alembic/versions/xxxxx_descripcion.py
git commit -m "Migración: descripción del cambio"

# Antes de hacer merge/pull
poetry run alembic upgrade head
```
