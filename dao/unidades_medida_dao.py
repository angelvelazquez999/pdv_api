from models.unidades_medida import UnidadMedida
from schemas.unidades_medida import UnidadesMedidaCreate
from services.main import AppCRUD

from typing import Optional


class UnidadMedidaCRUD(AppCRUD):
    def get_all_unidades_medida(self, skip: int = 0, limit: int = 100) -> list[UnidadMedida]:
        all_unidades_medida = self.db.query(
            UnidadMedida
        ).order_by(UnidadMedida.id.asc()).offset(skip).limit(limit)

        return all_unidades_medida
    
    def get_unidad_medida_by_id(self, id: int) -> UnidadMedida:
        unidad_medida = self.db.query(UnidadMedida).where(UnidadMedida.id == id).one_or_none()
        if unidad_medida:
            return unidad_medida
        return None
    
    def create_unidad_medida(self, item: UnidadesMedidaCreate) -> UnidadMedida:
        unidad_medida = UnidadMedida(
            nombre=item.nombre,
            abreviacion=item.abreviacion,
        )
        self.db.add(unidad_medida)
        self.db.commit()
        self.db.refresh(unidad_medida)
        return unidad_medida
