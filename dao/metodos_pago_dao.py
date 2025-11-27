from models.metodos_pago import MetodosPago
from schemas.metodos_pago import MetodosPagoCreate
from services.main import AppCRUD

from typing import Optional

class MetodosPagoCRUD(AppCRUD):
    def get_all_metodos_pago(self, skip: int = 0, limit: int = 100) -> list[MetodosPago]:
        all_metodos_pago = self.db.query(
            MetodosPago
        ).order_by(MetodosPago.id.asc()).offset(skip).limit(limit)
        return all_metodos_pago
    
    def get_metodo_pago_by_id(self, id: int) -> MetodosPago:
        metodo_pago = self.db.query(MetodosPago).where(MetodosPago.id == id).one_or_none()
        if metodo_pago:
            return metodo_pago
        return None
    
    def create_metodo_pago(self, item: MetodosPagoCreate) -> MetodosPago:
        metodo_pago = MetodosPago(
            nombre=item.nombre,
        )
        self.db.add(metodo_pago)
        self.db.commit()
        self.db.refresh(metodo_pago)
        return metodo_pago