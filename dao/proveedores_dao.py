import datetime
from models.proveedores import Proveedores
from schemas.proveedores import ProveedoresCreate
from services.main import AppCRUD

from typing import Optional

class ProveedoresCRUD(AppCRUD):
    def get_all_proveedores(self, skip: int = 0, limit: int = 100) -> list[Proveedores]:
        all_proveedores = self.db.query(
            Proveedores
        ).filter(Proveedores.deleted_at.is_(None)).order_by(Proveedores.id.asc()).offset(skip).limit(limit)
        return all_proveedores
    
    def get_proveedor_by_id(self, id: int) -> Proveedores:
        proveedor = self.db.query(Proveedores).where(Proveedores.id == id).one_or_none()
        if proveedor:
            return proveedor
        return None
    
    def get_proveedor_by_id_for_router(self, id: int) -> Proveedores:
        proveedor = self.db.query(Proveedores).where(Proveedores.id == id).filter(Proveedores.deleted_at.is_(None)).one_or_none()
        if proveedor:
            return proveedor
        return None
    
    def create_proveedor(self, item: ProveedoresCreate) -> Proveedores:
        proveedor = Proveedores(
            nombre=item.nombre,
            telefono=item.telefono,
            correo=item.correo
        )
        self.db.add(proveedor)
        self.db.commit()
        self.db.refresh(proveedor)
        return proveedor
    
    def update_proveedor(self, item: ProveedoresCreate, proveedor: Proveedores):
        proveedor.nombre = item.nombre
        proveedor.telefono = item.telefono
        proveedor.correo = item.correo
        proveedor.updated_at = datetime.datetime.now()
        self.db.add(proveedor)
        self.db.commit()
        self.db.refresh(proveedor)
        return proveedor
    
    
    def delete_proveedor(self, proveedor: Proveedores):
        proveedor.deleted_at = datetime.datetime.now()

        self.db.add(proveedor)
        self.db.commit()
        self.db.refresh(proveedor)
        return proveedor