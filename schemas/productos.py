from pydantic import BaseModel, Field
from typing import Optional

from schemas.response_model import SafeDelete


class UpdateModel(BaseModel):
    class Config:
        extra = "forbid"

class ProductosGet(SafeDelete):
    id: int
    sku: str
    nombre: str
    descripcion: Optional[str] = None
    categoria_id: int
    unidad_medida_id: int
    precio_venta: float
    precio_compra: float
    codigo_barras: Optional[str] = None
    
class ProductosCreate(UpdateModel):
    nombre: str
    descripcion: Optional[str] = None
    categoria_id: int
    unidad_medida_id: int
    precio_venta: float
    precio_compra: float
    codigo_barras: Optional[str] = None


    # TODO:
    # sku se generara automaticamente al crear el producto en base a la abreviacion de la categoria y un numero secuencial