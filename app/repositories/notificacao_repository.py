from sqlalchemy.orm import Session
from app.entities.notificacao_entity import Notificacao
from typing import List, Optional

class NotificacaoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Notificacao]:
        return self.db.query(Notificacao).all()

    def get_by_id(self, notificacao_id: int) -> Optional[Notificacao]:
        return self.db.query(Notificacao).filter(Notificacao.id == notificacao_id).first()

    def get_by_usuario(self, usuario_id: int) -> List[Notificacao]:
        return self.db.query(Notificacao).filter(Notificacao.usuario_id == usuario_id).all()

    def create(self, notificacao: Notificacao) -> Notificacao:
        self.db.add(notificacao)
        self.db.commit()
        self.db.refresh(notificacao)
        return notificacao

    def update(self, notificacao: Notificacao) -> Notificacao:
        self.db.commit()
        self.db.refresh(notificacao)
        return notificacao

    def delete(self, notificacao: Notificacao):
        self.db.delete(notificacao)
        self.db.commit()
