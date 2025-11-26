from sqlalchemy.orm import Session
from dao.usuario_dao import UsuarioCRUD
from schemas.usuario import UsuarioCreate, UsuarioUpdate
from utils.security import get_password_hash
from services.main import AppService
from utils.service_result import ServiceResult, handle_result
from utils.app_exceptions import AppException


class UsuarioService(AppService):

    def get_all_usuarios(self, skip: int = 0, limit: int = 100) -> ServiceResult:
        usuarios = UsuarioCRUD(self.db).get_all_usuarios(skip, limit)
        return ServiceResult(usuarios)

    def get_usuario_by_id(self, usuario_id: int) -> ServiceResult:
        usuario = UsuarioCRUD(self.db).get_usuario_by_id_for_router(usuario_id)
        if not usuario:
            return ServiceResult(AppException.GetPanaSeccion({"Message": f"No se ha encontrado un usuario con el id: {usuario_id}"}))
        return ServiceResult(usuario)

    def get_usuario_by_correo(self, correo: str) -> ServiceResult:
        usuario = UsuarioCRUD(self.db).get_usuario_by_correo(correo)
        if not usuario:
            return ServiceResult(AppException.GetPanaSeccion({"Message": f"No se ha encontrado un usuario con el correo: {correo}"}))
        return ServiceResult(usuario)

    def create_usuario(self, item: UsuarioCreate) -> ServiceResult:
        if UsuarioCRUD(self.db).exists_correo(item.correo):
            return ServiceResult(AppException.CreateUsuario({"Message": f"El correo {item.correo} ya está registrado"}))
        
        password_hash = get_password_hash(item.password)
        
        post = UsuarioCRUD(self.db).create_usuario(item, password_hash)
        
        result = handle_result(self.get_usuario_by_id(post.id))
        
        return ServiceResult((result, post.id))

    def update_usuario(self, usuario_id: int, item: UsuarioUpdate) -> ServiceResult:
        old_usuario = UsuarioCRUD(self.db).get_usuario_by_id(usuario_id)
        if not old_usuario:
            return ServiceResult(AppException.GetPanaSeccion({"Message": f"No se ha encontrado un usuario con el id: {usuario_id}"}))
        
        password_hash = None
        if item.password:
            password_hash = get_password_hash(item.password)
        
        UsuarioCRUD(self.db).update_usuario(item, old_usuario, password_hash)
        
        result = handle_result(self.get_usuario_by_id(usuario_id))
        
        return ServiceResult(result)

    def delete_usuario(self, usuario_id: int) -> ServiceResult:
        usuario = UsuarioCRUD(self.db).get_usuario_by_id(usuario_id)
        if not usuario:
            return ServiceResult(AppException.GetPanaSeccion({"Message": f"No se ha encontrado un usuario con el id: {usuario_id}"}))
        
        UsuarioCRUD(self.db).delete_usuario(usuario)
        
        return ServiceResult({"Message": f"El usuario {usuario.nombre} {usuario.apellidos} fue eliminado exitosamente"})
