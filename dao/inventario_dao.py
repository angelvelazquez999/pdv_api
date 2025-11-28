from models.inventario import InventarioDB
from schemas.inventario import InventarioCreate
from services.main import AppCRUD
import datetime
from typing import Optional

class InventarioCRUD(AppCRUD):
    def get_all_stock(self, skip: int = 0, limit: int = 100) -> list[InventarioDB]:
        all_productos = self.db.query(
            InventarioDB
        ).filter(InventarioDB.deleted_at == None).order_by(InventarioDB.id.asc()).offset(skip).limit(limit)
        return all_productos
    
    def get_product_stock_by_id(self, id: int) -> InventarioDB:
        producto = self.db.query(InventarioDB).where(InventarioDB.id == id).one_or_none()
        if producto:
            return producto
        return None
    
    def get_producto_by_id_for_router(self, id: int) -> InventarioDB:
        producto = self.db.query(InventarioDB).where(InventarioDB.id == id).filter(InventarioDB.deleted_at == None).one_or_none()
        if producto:
            return producto
        return None
    
    def create_producto(self, item: InventarioCreate, sku: str) -> InventarioDB:
        producto = InventarioDB(
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
    
    # def update_producto(self, item: ProductosCreate, producto: ProductosDB, sku: Optional[str] = None):
    #     producto.sku = sku
    #     producto.nombre = item.nombre
    #     producto.descripcion = item.descripcion
    #     producto.categoria_id = item.categoria_id
    #     producto.unidad_medida_id = item.unidad_medida_id
    #     producto.precio_venta = item.precio_venta
    #     producto.precio_compra = item.precio_compra
    #     producto.codigo_barras = item.codigo_barras
    #     producto.updated_at = datetime.datetime.now()
    #     self.db.add(producto)
    #     self.db.commit()
    #     self.db.refresh(producto)
    #     return producto
        
    # def delete_producto(self, producto: ProductosDB):
    #     producto.deleted_at = datetime.datetime.now()
    #     self.db.add(producto)
    #     self.db.commit()
    #     self.db.refresh(producto)
    #     return producto