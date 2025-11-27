from models.safe_delete_model import SafeDeleteModel
from models.productos import ProductosDB
from sqlalchemy import Column, Integer, BigInteger, ForeignKey


class InventarioDB(SafeDeleteModel):
    __tablename__ = "inventario"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    producto_id = Column(BigInteger, ForeignKey(f"{ProductosDB.__tablename__}.id"))
    stock_actual = Column(Integer, nullable=False, server_default="0")
    stock_minimo = Column(Integer, nullable=False, server_default="0")
    
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)




    