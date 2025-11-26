from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

from database import Base

class SafeDeleteModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)


class SoftDeleteNoUpdate(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=func.now())
    deleted_at = Column(DateTime, nullable=True)
