from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
from services.productos import ProductosService
from schemas.productos import ProductosCreate, ProductosGet
from schemas.response_model import ResponseModel
from dependencies import get_current_user
from models.usuario import Usuario
from utils.service_result import handle_result
from typing import List

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


@router.get("/", status_code=200, summary="Obtiene todos los productos", response_model=List[ProductosGet])
async def get_all_productos(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Límite de registros"),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(ProductosService(db).get_all_productos(skip, limit))
    return result
    

@router.get("/{producto_id}", status_code=200, summary="Obtiene un producto por ID", response_model=ProductosGet)
async def get_producto_by_id(
    producto_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(ProductosService(db).get_producto_by_id(producto_id))
    return result

@router.get("/sku/{sku}", status_code=200, summary="Obtiene un producto por SKU", response_model=ProductosGet)
async def get_producto_by_sku(
    sku: str,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(ProductosService(db).get_producto_by_sku(sku))
    return result

@router.get("/codigo/{code}", status_code=200, summary="Obtiene un producto por código de barras", response_model=ProductosGet)
async def get_producto_by_code(
    code: str,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result = handle_result(ProductosService(db).get_producto_by_code(code))
    return result

@router.post("/", status_code=200, summary="Crea un nuevo producto", response_model=ProductosGet)
async def create_producto(
    item: ProductosCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    result, producto_id = handle_result(ProductosService(db).create_producto(item))
    return result


@router.put("/{id}", status_code=200, summary="Obtiene un objeto producto en la base de datos para poder editarlo", response_model=ProductosGet)
async def update_producto(id: int, item: ProductosCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    result = handle_result(ProductosService(db).update_producto(id, item))
    return result


@router.delete("/{id}", status_code=200, summary="Obtiene un objeto producto en la base de datos para posteriormente borrarlo", response_model=ResponseModel)
async def delete_producto(id: int, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    result = handle_result(ProductosService(db).delete_producto(id))
    return result