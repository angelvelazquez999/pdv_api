from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
from services.unidades_medida import UnidadesMedidaService
from schemas.unidades_medida import UnidadMedidaGet, UnidadesMedidaCreate
from schemas.response_model import ResponseModel
from dependencies import get_current_user
from models.usuario import Usuario
from utils.service_result import handle_result
from typing import List

router = APIRouter(
    prefix="/unidades_medida",
    tags=["Unidades de Medida"]
)


@router.get("/", status_code=200, summary="Obtiene todas las unidades de medida", response_model=List[UnidadMedidaGet])
async def get_all_unidades_medida(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Límite de registros"),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(UnidadesMedidaService(db).get_all_unidades_medida(skip, limit))
    return result


@router.get("/{unidad_medida_id}", status_code=200, summary="Obtiene una unidad de medida por ID", response_model=UnidadMedidaGet)
async def get_unidad_medida(
    unidad_medida_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(UnidadesMedidaService(db).get_unidad_medida_by_id(unidad_medida_id))
    return result


@router.post("/", status_code=200, summary="Crea una nueva unidad de medida", response_model=UnidadMedidaGet)
async def create_unidad_medida(
    item: UnidadesMedidaCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result, unidad_medida_id = handle_result(UnidadesMedidaService(db).create_unidad_medida(item))
    return result