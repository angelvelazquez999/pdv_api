"""crear tabla de productos

Revision ID: 2b8361c2a50b
Revises: 986defa70bcb
Create Date: 2025-11-27 15:43:10.738530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2b8361c2a50b'
down_revision: Union[str, Sequence[str], None] = '986defa70bcb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'productos',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('sku', sa.String(length=50), nullable=False, unique=True),
        sa.Column('nombre', sa.String(length=255), nullable=False),
        sa.Column('descripcion', sa.String(length=500), nullable=True),
        sa.Column('categoria_id', sa.Integer(), sa.ForeignKey('categorias_productos.id'), nullable=False),
        sa.Column('unidad_medida_id', sa.Integer(), sa.ForeignKey('unidades_medida.id'), nullable=False),
        sa.Column('precio_venta', sa.Numeric(10,2), nullable=False),
        sa.Column('precio_compra', sa.Numeric(10,2), nullable=False),
        sa.Column('codigo_barras', sa.String(length=100), nullable=True, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    )


def downgrade():
    op.drop_table('productos')