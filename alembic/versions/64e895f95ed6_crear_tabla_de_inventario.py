"""crear tabla de inventario

Revision ID: 64e895f95ed6
Revises: 2b8361c2a50b
Create Date: 2025-11-27 15:44:11.063519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64e895f95ed6'
down_revision: Union[str, Sequence[str], None] = '2b8361c2a50b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'inventario',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('producto_id', sa.Integer(), sa.ForeignKey('productos.id', ondelete='CASCADE'), nullable=False),
        sa.Column('stock_actual', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('stock_minimo', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('inventario')
