from models.safe_delete_model import SafeDeleteModel
from models.categorias_productos import CategoriasProductosDB
from models.unidades_medida import UnidadesMedidaDB
from sqlalchemy import Column, Integer, String, Numeric, BigInteger, ForeignKey


class ProductosDB(SafeDeleteModel):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sku = Column(String(50), unique=True, nullable=False, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(500), nullable=True)
    categoria_id = Column(BigInteger, ForeignKey(f"{CategoriasProductosDB.__tablename__}.id"))
    unidad_medida_id = Column(BigInteger, ForeignKey(f"{UnidadesMedidaDB.__tablename__}.id"))
    precio_venta = Column(Numeric(10,2), nullable=False)
    precio_compra = Column(Numeric(10,2), nullable=False)
    codigo_barras = Column(String(100), unique=True, nullable=True)
    
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)




    