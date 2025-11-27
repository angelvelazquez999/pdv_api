from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
from services.proveedores import ProveedoresService
from schemas.proveedores import ProveedoresCreate, ProveedoresGet
from schemas.response_model import ResponseModel
from dependencies import get_current_user
from models.usuario import Usuario
from utils.service_result import handle_result
from typing import List

router = APIRouter(
    prefix="/proveedores",
    tags=["Proveedores"]
)


@router.get("/", status_code=200, summary="Obtiene todos los proveedores", response_model=List[ProveedoresGet])
async def get_all_proveedores(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Límite de registros"),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(ProveedoresService(db).get_all_proveedores(skip, limit))
    return result


@router.get("/{proveedor_id}", status_code=200, summary="Obtiene un proveedor por ID", response_model=ProveedoresGet)
async def get_proveedor(
    proveedor_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(ProveedoresService(db).get_proveedor_by_id(proveedor_id))
    return result


@router.post("/", status_code=200, summary="Crea un nuevo proveedor", response_model=ProveedoresGet)
async def create_proveedor(
    item: ProveedoresCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result, proveedor_id = handle_result(ProveedoresService(db).create_proveedor(item))
    return result

@router.put("/{id}", status_code=200, summary="Obtiene un objeto de proveedor en la base de datos para poder editarlo", response_model=ProveedoresGet)
async def update_proveedor(id: int, proveedor: ProveedoresCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    result = handle_result(ProveedoresService(db).update_proveedor(id, proveedor))
    return result

@router.delete("/{id}", status_code=200, summary="Obtiene un objeto de proveedor en la base de datos para posteriormente borrarlo", response_model=ResponseModel)
async def delete_proveedor(id: int, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    result = handle_result(ProveedoresService(db).delete_proveedor(id))
    return result