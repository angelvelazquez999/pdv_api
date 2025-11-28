from pydantic import BaseModel, Field
from typing import Optional

from schemas.response_model import SafeDelete


class UpdateModel(BaseModel):
    class Config:
        extra = "forbid"

class InventarioGet(SafeDelete):
    producto_id: int
    stock_actual: int
    stock_minimo: int
    
class InventarioCreate(UpdateModel):
    producto_id: int
    stock_actual: int
    stock_minimo: int

