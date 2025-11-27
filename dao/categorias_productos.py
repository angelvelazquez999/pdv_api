import datetime
from models.categorias_productos import CategoriasProductos
from schemas.categorias_productos import CategoriasProductosCreate
from schemas.metodos_pago import MetodosPagoCreate
from services.main import AppCRUD

from typing import Optional

class CategoriasProductosCRUD(AppCRUD):
    def get_all_categorias_productos(self, skip: int = 0, limit: int = 100) -> list[CategoriasProductos]:
        all_categorias_productos = self.db.query(
            CategoriasProductos
        ).filter(CategoriasProductos.deleted_at == None).order_by(CategoriasProductos.id.asc()).offset(skip).limit(limit)
        return all_categorias_productos
    
    def get_categoria_producto_by_id(self, id: int) -> CategoriasProductos:
        categoria_producto = self.db.query(CategoriasProductos).where(CategoriasProductos.id == id).one_or_none()
        if categoria_producto:
            return categoria_producto
        return None
    
    def get_categoria_producto_by_id_for_router(self, id: int) -> CategoriasProductos:
        categoria_producto = self.db.query(CategoriasProductos).where(CategoriasProductos.id == id).filter(CategoriasProductos.deleted_at == None).one_or_none()
        if categoria_producto:
            return categoria_producto
        return None
    
    def create_categoria_producto(self, item: CategoriasProductosCreate) -> CategoriasProductos:
        categoria_producto = CategoriasProductos(
            nombre=item.nombre,
        )
        self.db.add(categoria_producto)
        self.db.commit()
        self.db.refresh(categoria_producto)
        return categoria_producto
    
    def update_categoria_producto(self, item: CategoriasProductosCreate, categoria_producto: CategoriasProductos):
        categoria_producto.nombre = item.nombre
        categoria_producto.updated_at = datetime.datetime.now()
        self.db.add(categoria_producto)
        self.db.commit()
        self.db.refresh(categoria_producto)
        return categoria_producto
    
    
    def delete_categoria_producto(self, categoria_producto: CategoriasProductos):
        categoria_producto.deleted_at = datetime.datetime.now()
        self.db.add(categoria_producto)
        self.db.commit()
        self.db.refresh(categoria_producto)
        return categoria_producto