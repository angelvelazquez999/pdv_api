from sqlalchemy.orm import Session
from dao.metodos_pago_dao import MetodosPagoCRUD
from schemas.metodos_pago import MetodosPagoCreate
from services.main import AppService
from utils.service_result import ServiceResult, handle_result
from utils.app_exceptions import AppException


class MetodosPagoService(AppService):

    def get_all_metodos_pago(self, skip: int = 0, limit: int = 100) -> ServiceResult:
        metodos_pago = MetodosPagoCRUD(self.db).get_all_metodos_pago(skip, limit)
        return ServiceResult(metodos_pago)
    

    def get_metodo_pago_by_id(self, metodo_pago_id: int) -> ServiceResult:
        metodo_pago = MetodosPagoCRUD(self.db).get_metodo_pago_by_id(metodo_pago_id)
        if not metodo_pago:
            return ServiceResult(AppException.GetPanaSeccion({"Message": f"No se ha encontrado un método de pago con el id: {metodo_pago_id}"}))
        return ServiceResult(metodo_pago)


    def create_metodo_pago(self, item: MetodosPagoCreate) -> ServiceResult:
        
        metodo_pago = MetodosPagoCRUD(self.db).create_metodo_pago(item)
        
        result = handle_result(self.get_metodo_pago_by_id(metodo_pago.id))
        
        return ServiceResult((result, metodo_pago.id))