from pydantic import BaseModel, Field
from typing import Optional

from schemas.response_model import SafeDelete


class UpdateModel(BaseModel):
    class Config:
        extra = "forbid"

class CategoriasProductosGet(SafeDelete):
    id: int
    nombre: str
    
class CategoriasProductosCreate(UpdateModel):
    nombre: str = Field(..., max_length=100, description="Nombre de la categoría de producto")