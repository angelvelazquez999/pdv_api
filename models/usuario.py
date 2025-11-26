from models.safe_delete_model import SafeDeleteModel
from sqlalchemy import Column, Integer, String


class Usuario(SafeDeleteModel):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
