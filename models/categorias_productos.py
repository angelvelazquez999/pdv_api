from models.safe_delete_model import SafeDeleteModel
from sqlalchemy import Column, Integer, String


class CategoriasProductos(SafeDeleteModel):
    __tablename__ = "categorias_productos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

