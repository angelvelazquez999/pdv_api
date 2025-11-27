from models.safe_delete_model import SafeDeleteModel
from sqlalchemy import Column, Integer, String


class MetodosPagoDB(SafeDeleteModel):
    __tablename__ = "metodos_de_pagos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

