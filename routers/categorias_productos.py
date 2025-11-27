from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
from services.categorias_productos import CategoriasProductosService
from schemas.categorias_productos import CategoriasProductosCreate, CategoriasProductosGet
from schemas.response_model import ResponseModel
from dependencies import get_current_user
from models.usuario import Usuario
from utils.service_result import handle_result
from typing import List

router = APIRouter(
    prefix="/categorias_productos",
    tags=["Categorías de Productos"]
)


@router.get("/", status_code=200, summary="Obtiene todas las categorías de productos", response_model=List[CategoriasProductosGet])
async def get_all_categorias_productos(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Límite de registros"),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(CategoriasProductosService(db).get_all_categorias_productos(skip, limit))
    return result


@router.get("/{categoria_producto_id}", status_code=200, summary="Obtiene una categoría de producto por ID", response_model=CategoriasProductosGet)
async def get_categoria_producto(
    categoria_producto_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(CategoriasProductosService(db).get_categoria_producto_by_id(categoria_producto_id))
    return result


@router.post("/", status_code=200, summary="Crea una nueva categoría de producto", response_model=CategoriasProductosGet)
async def create_categoria_producto(
    item: CategoriasProductosCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result, categoria_producto_id = handle_result(CategoriasProductosService(db).create_categoria_producto(item))
    return result