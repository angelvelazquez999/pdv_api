from sqlalchemy.orm import Session
from dao.proveedores_dao import ProveedoresCRUD
from schemas.proveedores import ProveedoresCreate, ProveedoresGet
from services.main import AppService
from utils.service_result import ServiceResult, handle_result
from utils.app_exceptions import AppException


class ProveedoresService(AppService):

    def get_all_proveedores(self, skip: int = 0, limit: int = 100) -> ServiceResult:
        proveedores = ProveedoresCRUD(self.db).get_all_proveedores(skip, limit)
        return ServiceResult(proveedores)
    

    def get_proveedor_by_id(self, proveedor_id: int) -> ServiceResult:
        proveedor = ProveedoresCRUD(self.db).get_proveedor_by_id_for_router(proveedor_id)
        if not proveedor:
            return ServiceResult(AppException.UpdateProveedor({"Message": f"No se ha encontrado un proveedor con el id: {proveedor_id}"}))
        return ServiceResult(proveedor)


    def create_proveedor(self, item: ProveedoresCreate) -> ServiceResult:
        
        proveedor = ProveedoresCRUD(self.db).create_proveedor(item)
        
        result = handle_result(self.get_proveedor_by_id(proveedor.id))
        
        return ServiceResult((result, proveedor.id))
    
    
    def update_proveedor(self, id: int, item: ProveedoresCreate) -> ServiceResult:

        exist_proveedor = ProveedoresCRUD(self.db).get_proveedor_by_id(id)
        if not exist_proveedor:
            return ServiceResult(AppException.UpdateProveedor({"Message": f"No se ha encontrado un proveedor con el id: {id}"}))

        ProveedoresCRUD(self.db).update_proveedor(item, exist_proveedor)

        result = handle_result(self.get_proveedor_by_id(id))

        return ServiceResult(result)

    def delete_proveedor(self, id: int) -> ServiceResult:
        proveedor = ProveedoresCRUD(self.db).get_proveedor_by_id(id)
        if not proveedor:
            return ServiceResult(AppException.DeleteProveedor({"Message": f"No se ha encontrado un proveedor con el id: {id}"}))

        ProveedoresCRUD(self.db).delete_proveedor(proveedor)
        return ServiceResult({"Message": f"El proveedor {proveedor.nombre} fue eliminado exitosamente"})
    
    