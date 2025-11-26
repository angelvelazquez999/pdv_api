from pydantic import BaseModel, Field
from typing import Optional

from schemas.response_model import SafeDelete


class UpdateModel(BaseModel):
    class Config:
        extra = "forbid"

class UnidadMedidaGet(SafeDelete):
    id: int
    nombre: str
    abreviacion: Optional[str] = None
    
class UnidadesMedidaCreate(UpdateModel):
    nombre: str = Field(..., max_length=100, description="Nombre de la unidad de medida")
    abreviacion: Optional[str] = Field(None, max_length=255, description="Abreviación de la unidad de medida")