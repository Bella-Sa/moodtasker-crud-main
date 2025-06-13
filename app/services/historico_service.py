from typing import List, Optional
from sqlalchemy.orm import Session
from app.entities.historico_entity import Historico
from app.dtos.historico_dto import HistoricoCreate, HistoricoUpdate

class HistoricoService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Historico]:
        return self.db.query(Historico).all()

    def get_by_id(self, historico_id: int) -> Optional[Historico]:
        return self.db.query(Historico).filter(Historico.id == historico_id).first()

    def create(self, historico_create: HistoricoCreate) -> Historico:
        historico = Historico(**historico_create.dict())
        self.db.add(historico)
        self.db.commit()
        self.db.refresh(historico)
        return historico

    def update(self, historico_id: int, historico_update: HistoricoUpdate) -> Optional[Historico]:
        historico = self.get_by_id(historico_id)
        if not historico:
            return None
        update_data = historico_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(historico, key, value)
        self.db.commit()
        self.db.refresh(historico)
        return historico

    def delete(self, historico_id: int) -> bool:
        historico = self.get_by_id(historico_id)
        if not historico:
            return False
        self.db.delete(historico)  # exclusão física
        self.db.commit()
        return True
