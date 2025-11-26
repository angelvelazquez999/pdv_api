from sqlalchemy.orm import Session
from dao.unidades_medida_dao import UnidadMedidaCRUD
from schemas.unidades_medida import UnidadMedidaGet, UnidadesMedidaCreate
from services.main import AppService
from utils.service_result import ServiceResult, handle_result
from utils.app_exceptions import AppException


class UnidadesMedidaService(AppService):

    def get_all_unidades_medida(self, skip: int = 0, limit: int = 100) -> ServiceResult:
        unidades_medida = UnidadMedidaCRUD(self.db).get_all_unidades_medida(skip, limit)
        return ServiceResult(unidades_medida)
    

    def get_unidad_medida_by_id(self, unidad_medida_id: int) -> ServiceResult:
        unidad_medida = UnidadMedidaCRUD(self.db).get_unidad_medida_by_id(unidad_medida_id)
        if not unidad_medida:
            return ServiceResult(AppException.GetPanaSeccion({"Message": f"No se ha encontrado una unidad de medida con el id: {unidad_medida_id}"}))
        return ServiceResult(unidad_medida)


    def create_unidad_medida(self, item: UnidadesMedidaCreate) -> ServiceResult:
        
        unidad_medida = UnidadMedidaCRUD(self.db).create_unidad_medida(item)
        
        result = handle_result(self.get_unidad_medida_by_id(unidad_medida.id))
        
        return ServiceResult((result, unidad_medida.id))