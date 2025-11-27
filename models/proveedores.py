from models.safe_delete_model import SafeDeleteModel
from sqlalchemy import Column, Integer, String


class ProveedoresDB(SafeDeleteModel):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(Integer, nullable=True)
    correo = Column(String(100), nullable=True)
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

