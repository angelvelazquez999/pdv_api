from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
from services.usuario import UsuarioService
from schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioGet
from dependencies import get_current_user
from models.usuario import Usuario
from utils.service_result import handle_result
from typing import List

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


@router.get("/me", response_model=UsuarioGet)
def get_current_usuario(
    current_user: Usuario = Depends(get_current_user)
):
    return current_user


@router.get("/", status_code=200, summary="Obtiene todos los usuarios", response_model=List[UsuarioGet])
async def get_all_usuarios(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Límite de registros"),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(UsuarioService(db).get_all_usuarios(skip, limit))
    return result


@router.get("/{usuario_id}", status_code=200, summary="Obtiene un usuario por ID", response_model=UsuarioGet)
async def get_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(UsuarioService(db).get_usuario_by_id(usuario_id))
    return result


@router.post("/", status_code=200, summary="Crea un nuevo usuario", response_model=UsuarioGet)
async def create_usuario(
    item: UsuarioCreate,
    db: Session = Depends(get_db)
):
    result, usuario_id = handle_result(UsuarioService(db).create_usuario(item))
    return result


@router.put("/{usuario_id}", status_code=200, summary="Actualiza un usuario existente", response_model=UsuarioGet)
async def update_usuario(
    usuario_id: int,
    item: UsuarioUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(UsuarioService(db).update_usuario(usuario_id, item))
    return result


@router.delete("/{usuario_id}", status_code=200, summary="Elimina un usuario")
async def delete_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(UsuarioService(db).delete_usuario(usuario_id))
    return result
