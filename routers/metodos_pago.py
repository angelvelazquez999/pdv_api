from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
from services.metodos_pago import MetodosPagoService
from schemas.metodos_pago import MetodosPagoCreate, MetodosPagoGet
from schemas.response_model import ResponseModel
from dependencies import get_current_user
from models.usuario import Usuario
from utils.service_result import handle_result
from typing import List

router = APIRouter(
    prefix="/metodos_pago",
    tags=["Métodos de Pago"]
)


@router.get("/", status_code=200, summary="Obtiene todos los métodos de pago", response_model=List[MetodosPagoGet])
async def get_all_metodos_pago(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Límite de registros"),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(MetodosPagoService(db).get_all_metodos_pago(skip, limit))
    return result


@router.get("/{metodo_pago_id}", status_code=200, summary="Obtiene un método de pago por ID", response_model=MetodosPagoGet)
async def get_metodo_pago(
    metodo_pago_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(MetodosPagoService(db).get_metodo_pago_by_id(metodo_pago_id))
    return result


@router.post("/", status_code=200, summary="Crea un nuevo método de pago", response_model=MetodosPagoGet)
async def create_metodo_pago(
    item: MetodosPagoCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result, metodo_pago_id = handle_result(MetodosPagoService(db).create_metodo_pago(item))
    return result