from pydantic import BaseModel, Field
from typing import Optional

from schemas.response_model import SafeDelete


class UpdateModel(BaseModel):
    class Config:
        extra = "forbid"

class MetodosPagoGet(SafeDelete):
    id: int
    nombre: str
    
class MetodosPagoCreate(UpdateModel):
    nombre: str = Field(..., max_length=100, description="Nombre del método de pago")