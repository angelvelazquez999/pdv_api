from models.productos import ProductosDB
from models.unidades_medida import UnidadMedidaDB
from models.categorias_productos import CategoriasProductosDB
from schemas.productos import ProductosCreate
from services.main import AppCRUD
import datetime
from typing import Optional

class ProductosCRUD(AppCRUD):
    def get_all_productos_for_consecutivo(self) -> ProductosDB:
        return self.db.query(ProductosDB.id).count()
    
    # def get_all_productos(self, skip: int = 0, limit: int = 100) -> list[ProductosDB]:
    #     all_productos = self.db.query(
    #         ProductosDB
    #     ).filter(ProductosDB.deleted_at == None).order_by(ProductosDB.id.asc()).offset(skip).limit(limit)
    #     return all_productos
    
    def get_all_productos(self, skip: int = 0, limit: int = 100) -> list[ProductosDB]:
        return self.db.query(
            ProductosDB.id,
            ProductosDB.sku,
            ProductosDB.nombre,
            ProductosDB.descripcion,
            ProductosDB.categoria_id,
            CategoriasProductosDB.id.label("categoria_producto_id"),
            CategoriasProductosDB.nombre.label("categoria_producto"),
            ProductosDB.unidad_medida_id,
            UnidadMedidaDB.id.label("unidad_medida_id"),
            UnidadMedidaDB.nombre.label("unidad_medida"),
            ProductosDB.precio_venta,
            ProductosDB.precio_compra,
            ProductosDB.codigo_barras,
        ).join(
            CategoriasProductosDB, 
            ProductosDB.categoria_id == CategoriasProductosDB.id
        ).join(
            UnidadMedidaDB, 
            ProductosDB.unidad_medida_id == UnidadMedidaDB.id
        ).order_by(
            ProductosDB.id.asc()
        ).offset(skip).limit(limit).all()
    
    def get_producto_by_id(self, id: int) -> ProductosDB:
        producto = self.db.query(ProductosDB).where(ProductosDB.id == id).one_or_none()
        if producto:
            return producto
        return None
    
    # def get_producto_by_id_for_router(self, id: int) -> ProductosDB:
    #     producto = self.db.query(ProductosDB).where(ProductosDB.id == id).filter(ProductosDB.deleted_at == None).one_or_none()
    #     if producto:
    #         return producto
    #     return None
    
    def get_producto_by_id_for_router(self, id: int) -> ProductosDB:
        return self.db.query(
            ProductosDB.id,
            ProductosDB.sku,
            ProductosDB.nombre,
            ProductosDB.descripcion,
            ProductosDB.categoria_id,
            CategoriasProductosDB.id.label("categoria_producto_id"),
            CategoriasProductosDB.nombre.label("categoria_producto"),
            ProductosDB.unidad_medida_id,
            UnidadMedidaDB.id.label("unidad_medida_id"),
            UnidadMedidaDB.nombre.label("unidad_medida"),
            ProductosDB.precio_venta,
            ProductosDB.precio_compra,
            ProductosDB.codigo_barras,
        ).join(
            CategoriasProductosDB, 
            ProductosDB.categoria_id == CategoriasProductosDB.id
        ).join(
            UnidadMedidaDB, 
            ProductosDB.unidad_medida_id == UnidadMedidaDB.id
        ).where(
            ProductosDB.id == id,
            ProductosDB.deleted_at == None
        ).order_by(
            ProductosDB.id.asc()
        ).first()
    
    def create_producto(self, item: ProductosCreate, sku: str) -> ProductosDB:
        producto = ProductosDB(
            sku=sku,
            nombre=item.nombre,
            descripcion=item.descripcion,
            categoria_id=item.categoria_id,
            unidad_medida_id=item.unidad_medida_id,
            precio_venta=item.precio_venta,
            precio_compra=item.precio_compra,
            codigo_barras=item.codigo_barras,
        )
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto
    
    def update_producto(self, item: ProductosCreate, producto: ProductosDB, sku: Optional[str] = None):
        producto.sku = sku
        producto.nombre = item.nombre
        producto.descripcion = item.descripcion
        producto.categoria_id = item.categoria_id
        producto.unidad_medida_id = item.unidad_medida_id
        producto.precio_venta = item.precio_venta
        producto.precio_compra = item.precio_compra
        producto.codigo_barras = item.codigo_barras
        producto.updated_at = datetime.datetime.now()
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto
        
    def delete_producto(self, producto: ProductosDB):
        producto.deleted_at = datetime.datetime.now()
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto