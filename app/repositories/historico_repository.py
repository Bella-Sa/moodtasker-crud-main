from sqlalchemy.orm import Session
from app.entities.historico_entity import Historico
from typing import List, Optional

class HistoricoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Historico]:
        return self.db.query(Historico).all()

    def get_by_id(self, historico_id: int) -> Optional[Historico]:
        return self.db.query(Historico).filter(Historico.id == historico_id).first()

    def get_by_usuario(self, usuario_id: int) -> List[Historico]:
        return self.db.query(Historico).filter(Historico.usuario_id == usuario_id).all()

    def create(self, historico: Historico) -> Historico:
        self.db.add(historico)
        self.db.commit()
        self.db.refresh(historico)
        return historico

    def update(self, historico: Historico) -> Historico:
        self.db.commit()
        self.db.refresh(historico)
        return historico

    def delete(self, historico: Historico):
        self.db.delete(historico)
        self.db.commit()
