from models.safe_delete_model import SafeDeleteModel
from sqlalchemy import Column, Integer, String


class UnidadMedida(SafeDeleteModel):
    __tablename__ = "unidades_medida"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    abreviacion = Column(String(100), nullable=False)

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
