from models.usuario import Usuario
from services.main import AppCRUD
from schemas.usuario import UsuarioCreate, UsuarioUpdate

from typing import Optional


class UsuarioCRUD(AppCRUD):

    def get_usuario(self, id: int) -> Usuario:
        usuario = self.db.query(Usuario).filter(Usuario.id == id).first()
        if usuario:
            return usuario
        return None

    def get_usuario_by_id_for_router(self, id: int) -> Usuario:
        usuario = self.db.query(
            Usuario
        ).where(
            Usuario.id == id
        ).one_or_none()
        if usuario:
            return usuario
        return None

    def get_usuario_by_id(self, id: int) -> Usuario:
        usuario = self.db.query(Usuario).where(Usuario.id == id).one_or_none()
        if usuario:
            return usuario
        return None

    def get_usuario_by_correo(self, correo: str) -> Usuario:
        usuario = self.db.query(Usuario).where(Usuario.correo == correo).one_or_none()
        if usuario:
            return usuario
        return None

    def get_all_usuarios(self, skip: int = 0, limit: int = 100) -> list[Usuario]:
        all_usuarios = self.db.query(
            Usuario
        ).order_by(Usuario.id.asc()).offset(skip).limit(limit)

        return all_usuarios

    def create_usuario(self, item: UsuarioCreate, password_hash: str) -> Usuario:
        usuario = Usuario(
            nombre=item.nombre,
            apellidos=item.apellidos,
            correo=item.correo,
            password_hash=password_hash,
        )
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def update_usuario(self, item: UsuarioUpdate, usuario: Usuario, password_hash: Optional[str] = None):
        if item.nombre is not None:
            usuario.nombre = item.nombre
        if item.apellidos is not None:
            usuario.apellidos = item.apellidos
        if password_hash is not None:
            usuario.password_hash = password_hash

        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def delete_usuario(self, usuario: Usuario):
        self.db.delete(usuario)
        self.db.commit()
        return True

    def exists_correo(self, correo: str) -> bool:
        return self.db.query(Usuario).filter(Usuario.correo == correo).first() is not None