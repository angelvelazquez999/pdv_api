from sqlalchemy.orm import Session


class AppCRUD:
    
    def __init__(self, db: Session):
        self.db = db


class AppService:
    """Clase base para servicios"""
    
    def __init__(self, db: Session):
        self.db = db
