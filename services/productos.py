from sqlalchemy.orm import Session
from dao.productos_dao import ProductosCRUD
from dao.categorias_productos_dao import CategoriasProductosCRUD
from schemas.productos import ProductosCreate
from services.main import AppService
from utils.service_result import ServiceResult, handle_result
from utils.app_exceptions import AppException
from utils.abreviacion import abreviacion


class ProductosService(AppService):

    def get_all_productos(self, skip: int = 0, limit: int = 100) -> ServiceResult:
        productos = ProductosCRUD(self.db).get_all_productos(skip, limit)
        return ServiceResult(productos)
    

    def get_producto_by_id(self, producto_id: int) -> ServiceResult:
        producto = ProductosCRUD(self.db).get_producto_by_id_for_router(producto_id)
        if not producto:
            return ServiceResult(AppException.GetProducto({"Message": f"No se ha encontrado un producto con el id: {producto_id}"}))
        return ServiceResult(producto)
    
    def get_producto_by_sku(self, sku: str) -> ServiceResult:
        producto = ProductosCRUD(self.db).get_producto_by_sku_for_router(sku)
        if not producto:
            return ServiceResult(AppException.GetProducto({"Message": f"No se ha encontrado un producto con el sku: {sku}"}))
        return ServiceResult(producto)

    def get_producto_by_code(self, code: str) -> ServiceResult:
        producto = ProductosCRUD(self.db).get_producto_by_code_for_router(code)
        if not producto:
            return ServiceResult(AppException.GetProducto({"Message": f"No se ha encontrado un producto con el código: {code}"}))
        return ServiceResult(producto)

    def create_producto(self, item: ProductosCreate) -> ServiceResult:
        
        categoria = CategoriasProductosCRUD(self.db).get_categoria_producto_by_id(item.categoria_id)
        if not categoria:
            return ServiceResult(AppException.CreateProducto({"Message": f"No se ha encontrado una categoría con el id: {item.categoria_id}"}))
        
        sku = f"{abreviacion(categoria.nombre)}-{ProductosCRUD(self.db).get_all_productos_for_consecutivo() + 1:05d}"
        
        producto = ProductosCRUD(self.db).create_producto(item, sku)
        
        result = handle_result(self.get_producto_by_id(producto.id))
        
        return ServiceResult((result, producto.id))
        

    def update_producto(self, id: int, item: ProductosCreate) -> ServiceResult:

        exist_producto = ProductosCRUD(self.db).get_producto_by_id(id)
        if not exist_producto:
            return ServiceResult(AppException.UpdateProducto({"Message": f"No se ha encontrado un producto con el id: {id}"}))
        
        abreviacion_categoria = CategoriasProductosCRUD(self.db).get_abreviacion_by_id(item.categoria_id)
        if not abreviacion_categoria:
            return ServiceResult(AppException.CreateProducto({"Message": f"No se ha encontrado una categoría con el id: {item.categoria_id}"}))
        
        sku = f"{abreviacion_categoria}-{ProductosCRUD(self.db).get_all_productos_for_consecutivo() + 1:05d}"
        
        ProductosCRUD(self.db).update_producto(item, exist_producto, sku)
        result = handle_result(self.get_producto_by_id(id))

        return ServiceResult(result)

    def delete_producto(self, id: int) -> ServiceResult:
        producto = ProductosCRUD(self.db).get_producto_by_id(id)
        if not producto:
            return ServiceResult(AppException.DeleteProducto({"Message": f"No se ha encontrado un producto con el id: {id}"}))

        ProductosCRUD(self.db).delete_producto(producto)
        return ServiceResult({"Message": f"El producto {producto.nombre} fue eliminado exitosamente"})