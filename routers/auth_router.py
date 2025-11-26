from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from services.auth_service import AuthService
from services.usuario import UsuarioService
from schemas.usuario import UsuarioLogin, UsuarioCreate, UsuarioResponse, Token

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)


@router.post("/register", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def register(
    usuario_data: UsuarioCreate,
    db: Session = Depends(get_db)
):
    return UsuarioService.create_usuario(db, usuario_data)


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    login_data = UsuarioLogin(
        correo=form_data.username,  
        password=form_data.password
    )
    return AuthService.authenticate_user(db, login_data)
