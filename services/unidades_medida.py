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
    
    def update_unidad_medida(self, id: int, item: UnidadesMedidaCreate) -> ServiceResult:

        exist_unidad_medida = UnidadMedidaCRUD(self.db).get_unidad_medida_by_id(id)
        if not exist_unidad_medida:
            return ServiceResult(AppException.UpdateProveedor({"Message": f"No se ha encontrado un proveedor con el id: {id}"}))

        UnidadMedidaCRUD(self.db).update_unidad_medida(item, exist_unidad_medida)
        result = handle_result(self.get_unidad_medida_by_id(id))

        return ServiceResult(result)

    def delete_unidad_medida(self, id: int) -> ServiceResult:
        unidad_medida = UnidadMedidaCRUD(self.db).get_unidad_medida_by_id(id)
        if not unidad_medida:
            return ServiceResult(AppException.DeleteProveedor({"Message": f"No se ha encontrado un proveedor con el id: {id}"}))

        UnidadMedidaCRUD(self.db).delete_unidad_medida(unidad_medida)
        return ServiceResult({"Message": f"La unidad de medida {unidad_medida.nombre} fue eliminada exitosamente"})