import datetime
from models.proveedores import ProveedoresDB
from schemas.proveedores import ProveedoresCreate
from services.main import AppCRUD

from typing import Optional

class ProveedoresCRUD(AppCRUD):
    def get_all_proveedores(self, skip: int = 0, limit: int = 100) -> list[ProveedoresDB]:
        all_proveedores = self.db.query(
            ProveedoresDB
        ).filter(ProveedoresDB.deleted_at.is_(None)).order_by(ProveedoresDB.id.asc()).offset(skip).limit(limit)
        return all_proveedores
    
    def get_proveedor_by_id(self, id: int) -> ProveedoresDB:
        proveedor = self.db.query(ProveedoresDB).where(ProveedoresDB.id == id).one_or_none()
        if proveedor:
            return proveedor
        return None
    
    def get_proveedor_by_id_for_router(self, id: int) -> ProveedoresDB:
        proveedor = self.db.query(ProveedoresDB).where(ProveedoresDB.id == id).filter(ProveedoresDB.deleted_at.is_(None)).one_or_none()
        if proveedor:
            return proveedor
        return None
    
    def create_proveedor(self, item: ProveedoresCreate) -> ProveedoresDB:
        proveedor = ProveedoresDB(
            nombre=item.nombre,
            telefono=item.telefono,
            correo=item.correo
        )
        self.db.add(proveedor)
        self.db.commit()
        self.db.refresh(proveedor)
        return proveedor
    
    def update_proveedor(self, item: ProveedoresCreate, proveedor: ProveedoresDB):
        proveedor.nombre = item.nombre
        proveedor.telefono = item.telefono
        proveedor.correo = item.correo
        proveedor.updated_at = datetime.datetime.now()
        self.db.add(proveedor)
        self.db.commit()
        self.db.refresh(proveedor)
        return proveedor
    
    
    def delete_proveedor(self, proveedor: ProveedoresDB):
        proveedor.deleted_at = datetime.datetime.now()

        self.db.add(proveedor)
        self.db.commit()
        self.db.refresh(proveedor)
        return proveedor