from models.metodos_pago import MetodosPago
from schemas.metodos_pago import MetodosPagoCreate
from services.main import AppCRUD
import datetime
from typing import Optional

class MetodosPagoCRUD(AppCRUD):
    def get_all_metodos_pago(self, skip: int = 0, limit: int = 100) -> list[MetodosPago]:
        all_metodos_pago = self.db.query(
            MetodosPago
        ).filter(MetodosPago.deleted_at == None).order_by(MetodosPago.id.asc()).offset(skip).limit(limit)
        return all_metodos_pago
    
    def get_metodo_pago_by_id(self, id: int) -> MetodosPago:
        metodo_pago = self.db.query(MetodosPago).where(MetodosPago.id == id).one_or_none()
        if metodo_pago:
            return metodo_pago
        return None
    
    def get_metodo_pago_by_id_for_router(self, id: int) -> MetodosPago:
        metodo_pago = self.db.query(MetodosPago).where(MetodosPago.id == id).filter(MetodosPago.deleted_at == None).one_or_none()
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
    
    def update_metodo_pago(self, item: MetodosPagoCreate, metodo_pago: MetodosPago):
        metodo_pago.nombre = item.nombre
        metodo_pago.updated_at = datetime.datetime.now()
        self.db.add(metodo_pago)
        self.db.commit()
        self.db.refresh(metodo_pago)
        return metodo_pago
    
    
    def delete_metodo_pago(self, metodo_pago: MetodosPago):
        metodo_pago.deleted_at = datetime.datetime.now()
        self.db.add(metodo_pago)
        self.db.commit()
        self.db.refresh(metodo_pago)
        return metodo_pago