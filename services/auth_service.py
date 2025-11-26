from datetime import timedelta
from sqlalchemy.orm import Session
from dao.usuario_dao import UsuarioCRUD
from schemas.usuario import UsuarioLogin, Token
from utils.security import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import HTTPException, status


class AuthService:

    @staticmethod
    def authenticate_user(db: Session, login_data: UsuarioLogin) -> Token:
        crud = UsuarioCRUD(db)
        usuario = crud.get_usuario_by_correo(login_data.correo)
        
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Correo o contraseña incorrecta",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        if not verify_password(login_data.password, usuario.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Correo o contraseña incorrecta",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": usuario.correo, "id": usuario.id},
            expires_delta=access_token_expires
        )
        
        return Token(access_token=access_token, token_type="bearer")
