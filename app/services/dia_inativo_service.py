from typing import List, Optional
from sqlalchemy.orm import Session
from app.entities.dia_inativo_entity import DiaInativo
from app.dtos.dia_inativo_dto import DiaInativoCreate, DiaInativoUpdate

class DiaInativoService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[DiaInativo]:
        return self.db.query(DiaInativo).all()

    def get_by_id(self, dia_inativo_id: int) -> Optional[DiaInativo]:
        return self.db.query(DiaInativo).filter(DiaInativo.id == dia_inativo_id).first()

    def create(self, dia_inativo_create: DiaInativoCreate) -> DiaInativo:
        dia_inativo = DiaInativo(**dia_inativo_create.dict())
        self.db.add(dia_inativo)
        self.db.commit()
        self.db.refresh(dia_inativo)
        return dia_inativo

    def update(self, dia_inativo_id: int, dia_inativo_update: DiaInativoUpdate) -> Optional[DiaInativo]:
        dia_inativo = self.get_by_id(dia_inativo_id)
        if not dia_inativo:
            return None
        update_data = dia_inativo_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(dia_inativo, key, value)
        self.db.commit()
        self.db.refresh(dia_inativo)
        return dia_inativo

    def delete(self, dia_inativo_id: int) -> bool:
        dia_inativo = self.get_by_id(dia_inativo_id)
        if not dia_inativo:
            return False
        self.db.delete(dia_inativo)  # exclusão física
        self.db.commit()
        return True
