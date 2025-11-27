import datetime
from models.categorias_productos import CategoriasProductosDB
from schemas.categorias_productos import CategoriasProductosCreate
from services.main import AppCRUD

from typing import Optional

class CategoriasProductosCRUD(AppCRUD):
    def get_all_categorias_productos(self, skip: int = 0, limit: int = 100) -> list[CategoriasProductosDB]:
        all_categorias_productos = self.db.query(
            CategoriasProductosDB
        ).filter(CategoriasProductosDB.deleted_at == None).order_by(CategoriasProductosDB.id.asc()).offset(skip).limit(limit)
        return all_categorias_productos
    
    def get_categoria_producto_by_id(self, id: int) -> CategoriasProductosDB:
        categoria_producto = self.db.query(CategoriasProductosDB).where(CategoriasProductosDB.id == id).one_or_none()
        if categoria_producto:
            return categoria_producto
        return None
    
    def get_categoria_producto_by_id_for_router(self, id: int) -> CategoriasProductosDB:
        categoria_producto = self.db.query(CategoriasProductosDB).where(CategoriasProductosDB.id == id).filter(CategoriasProductosDB.deleted_at == None).one_or_none()
        if categoria_producto:
            return categoria_producto
        return None
    
    def create_categoria_producto(self, item: CategoriasProductosCreate) -> CategoriasProductosDB:
        categoria_producto = CategoriasProductosDB(
            nombre=item.nombre,
        )
        self.db.add(categoria_producto)
        self.db.commit()
        self.db.refresh(categoria_producto)
        return categoria_producto
    
    def update_categoria_producto(self, item: CategoriasProductosCreate, categoria_producto: CategoriasProductosDB):
        categoria_producto.nombre = item.nombre
        categoria_producto.updated_at = datetime.datetime.now()
        self.db.add(categoria_producto)
        self.db.commit()
        self.db.refresh(categoria_producto)
        return categoria_producto
    
    
    def delete_categoria_producto(self, categoria_producto: CategoriasProductosDB):
        categoria_producto.deleted_at = datetime.datetime.now()
        self.db.add(categoria_producto)
        self.db.commit()
        self.db.refresh(categoria_producto)
        return categoria_producto