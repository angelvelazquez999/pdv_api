from fastapi import Request
from starlette.responses import JSONResponse


class AppExceptionCase(Exception):
    def __init__(self, status_code: int, context: dict):
        self.exception_case = self.__class__.__name__
        self.status_code = status_code
        self.context = context

    def __str__(self):
        return (
            f"<AppException {self.exception_case} - "
            + f"status_code={self.status_code} - context={self.context}>"
        )


async def app_exception_handler(request: Request, exc: AppExceptionCase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "app_exception": exc.exception_case,
            "context": exc.context,
        },
    )


class AppException(object):

    class InternalError(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Internal server error
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)
    
    class ItemNotFound(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Item not found
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)
    
    class UpdateProveedor(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Proveedor no encontrado
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)
    
    class GetUsuario(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Usuario no encontrado
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)
    
    class CreateUsuario(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Error al crear usuario
            """
            status_code = 400
            AppExceptionCase.__init__(self, status_code, context)
    
    class UpdateUsuario(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Error al actualizar usuario
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)
    
    class DeleteUsuario(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Error al eliminar usuario
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)

    class TokenInvalidCredentials(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Credenciales inválidas
            """
            status_code = 401
            AppExceptionCase.__init__(self, status_code, context)
    
    class CreateToken(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Error al crear token
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)
    
    class GetToken(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Token no encontrado
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)

    class ValidarPermiso(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Permiso denegado
            """
            status_code = 401
            AppExceptionCase.__init__(self, status_code, context)
            
    class DeleteProveedor(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Error al eliminar proveedor
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)
            
    class CreateProveedor(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Error al crear proveedor
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)
            
    class GetProveedor(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Proveedor no encontrado
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)
