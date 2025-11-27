import datetime
from models.unidades_medida import UnidadMedidaDB
from schemas.unidades_medida import UnidadesMedidaCreate
from services.main import AppCRUD

from typing import Optional


class UnidadMedidaCRUD(AppCRUD):
    def get_all_unidades_medida(self, skip: int = 0, limit: int = 100) -> list[UnidadMedidaDB]:
        all_unidades_medida = self.db.query(
            UnidadMedidaDB
        ).order_by(UnidadMedidaDB.id.asc()).offset(skip).limit(limit)

        return all_unidades_medida
    
    def get_unidad_medida_by_id(self, id: int) -> UnidadMedidaDB:
        unidad_medida = self.db.query(UnidadMedidaDB).where(UnidadMedidaDB.id == id).one_or_none()
        if unidad_medida:
            return unidad_medida
        return None
    
    def get_unidad_medida_by_id_for_router(self, id: int) -> UnidadMedidaDB:
        unidad_medida = self.db.query(UnidadMedidaDB).where(UnidadMedidaDB.id == id).filter(UnidadMedidaDB.deleted_at == None).one_or_none()
        if unidad_medida:
            return unidad_medida
        return None
    
    def create_unidad_medida(self, item: UnidadesMedidaCreate) -> UnidadMedidaDB:
        unidad_medida = UnidadMedidaDB(
            nombre=item.nombre,
            abreviacion=item.abreviacion,
        )
        self.db.add(unidad_medida)
        self.db.commit()
        self.db.refresh(unidad_medida)
        return unidad_medida
    
    def update_unidad_medida(self, item: UnidadesMedidaCreate, unidad_medida: UnidadMedidaDB):
        unidad_medida.nombre = item.nombre
        unidad_medida.abreviacion = item.abreviacion
        unidad_medida.updated_at = datetime.datetime.now()
        self.db.add(unidad_medida)
        self.db.commit()
        self.db.refresh(unidad_medida)
        return unidad_medida
    
    
    def delete_unidad_medida(self, unidad_medida: UnidadMedidaDB):
        unidad_medida.deleted_at = datetime.datetime.now()
        self.db.add(unidad_medida)
        self.db.commit()
        self.db.refresh(unidad_medida)
        return unidad_medida