from typing import List, Optional
from sqlalchemy.orm import Session
from app.entities.notificacao_entity import Notificacao
from app.dtos.notificacao_dto import NotificacaoCreate, NotificacaoUpdate
from datetime import datetime

class NotificacaoService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Notificacao]:
        return self.db.query(Notificacao).all()

    def get_by_id(self, notificacao_id: int) -> Optional[Notificacao]:
        return self.db.query(Notificacao).filter(Notificacao.id == notificacao_id).first()

    def create(self, notificacao_create: NotificacaoCreate) -> Notificacao:
        dados = notificacao_create.dict(exclude_none=True)  # remove campos None, incluindo 'data' se for None
        if 'data' not in dados:
            dados['data'] = datetime.utcnow()
        notificacao = Notificacao(**dados)
        self.db.add(notificacao)
        self.db.commit()
        self.db.refresh(notificacao)
        return notificacao

    def update(self, notificacao_id: int, notificacao_update: NotificacaoUpdate) -> Optional[Notificacao]:
        notificacao = self.get_by_id(notificacao_id)
        if not notificacao:
            return None
        update_data = notificacao_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(notificacao, key, value)
        self.db.commit()
        self.db.refresh(notificacao)
        return notificacao

    def delete(self, notificacao_id: int) -> bool:
        notificacao = self.get_by_id(notificacao_id)
        if not notificacao:
            return False
        self.db.delete(notificacao)  # exclusão física
        self.db.commit()
        return True
