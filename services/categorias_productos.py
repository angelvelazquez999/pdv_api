from sqlalchemy.orm import Session
from dao.categorias_productos import CategoriasProductosCRUD
from schemas.categorias_productos import CategoriasProductosCreate, CategoriasProductosGet
from services.main import AppService
from utils.service_result import ServiceResult, handle_result
from utils.app_exceptions import AppException


class CategoriasProductosService(AppService):

    def get_all_categorias_productos(self, skip: int = 0, limit: int = 100) -> ServiceResult:
        categorias_productos = CategoriasProductosCRUD(self.db).get_all_categorias_productos(skip, limit)
        return ServiceResult(categorias_productos)
    

    def get_categoria_producto_by_id(self, categoria_producto_id: int) -> ServiceResult:
        categoria_producto = CategoriasProductosCRUD(self.db).get_categoria_producto_by_id(categoria_producto_id)
        if not categoria_producto:
            return ServiceResult(AppException.GetPanaSeccion({"Message": f"No se ha encontrado una categoría de producto con el id: {categoria_producto_id}"}))
        return ServiceResult(categoria_producto)


    def create_categoria_producto(self, item: CategoriasProductosCreate) -> ServiceResult:
        
        categoria_producto = CategoriasProductosCRUD(self.db).create_categoria_producto(item)
        
        result = handle_result(self.get_categoria_producto_by_id(categoria_producto.id))
        
        return ServiceResult((result, categoria_producto.id))