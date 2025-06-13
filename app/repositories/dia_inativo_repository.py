from sqlalchemy.orm import Session
from app.entities.dia_inativo_entity import DiaInativo
from typing import List, Optional

class DiaInativoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[DiaInativo]:
        return self.db.query(DiaInativo).all()

    def get_by_id(self, dia_inativo_id: int) -> Optional[DiaInativo]:
        return self.db.query(DiaInativo).filter(DiaInativo.id == dia_inativo_id).first()

    def get_by_usuario(self, usuario_id: int) -> List[DiaInativo]:
        return self.db.query(DiaInativo).filter(DiaInativo.usuario_id == usuario_id).all()

    def create(self, dia_inativo: DiaInativo) -> DiaInativo:
        self.db.add(dia_inativo)
        self.db.commit()
        self.db.refresh(dia_inativo)
        return dia_inativo

    def update(self, dia_inativo: DiaInativo) -> DiaInativo:
        self.db.commit()
        self.db.refresh(dia_inativo)
        return dia_inativo

    def delete(self, dia_inativo: DiaInativo):
        self.db.delete(dia_inativo)
        self.db.commit()
