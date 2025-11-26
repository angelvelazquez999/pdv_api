from pydantic import BaseModel, Field
from typing import Optional


class UsuarioBase(BaseModel):
    nombre: str = Field(..., max_length=100, description="Nombre del usuario")
    apellidos: str = Field(..., max_length=100, description="Apellidos del usuario")
    correo: str = Field(..., max_length=100, description="Correo electrónico del usuario")


class UsuarioCreate(UsuarioBase):
    password: str = Field(..., min_length=6, description="Contraseña del usuario")


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=100)
    apellidos: Optional[str] = Field(None, max_length=100)
    correo: Optional[str] = Field(None, max_length=100)
    password: Optional[str] = Field(None, min_length=6)


class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True


class UsuarioLogin(BaseModel):
    correo: str = Field(..., description="Correo electrónico del usuario")
    password: str = Field(..., description="Contraseña del usuario")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    correo: Optional[str] = None