from pydantic import BaseModel, Field
from typing import Optional

from schemas.response_model import SafeDelete


class UpdateModel(BaseModel):
    class Config:
        extra = "forbid"

class ProveedoresGet(SafeDelete):
    id: int
    nombre: str
    telefono: Optional[int] = None
    correo: Optional[str] = None

class ProveedoresCreate(UpdateModel):
    nombre: str = Field(..., max_length=100, description="Nombre del proveedor")
    telefono: Optional[int] = Field(None, description="Teléfono del proveedor")
    correo: Optional[str] = Field(None, max_length=100, description="Correo electrónico del proveedor")