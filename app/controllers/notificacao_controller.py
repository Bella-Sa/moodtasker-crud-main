from sqlalchemy.orm import Session
from typing import List, Optional
from app.services.notificacao_service import NotificacaoService
from app.dtos.notificacao_dto import NotificacaoCreate, NotificacaoUpdate
from app.entities.notificacao_entity import Notificacao

class NotificacaoController:
    def __init__(self, db: Session):
        self.service = NotificacaoService(db)

    def listar(self) -> List[Notificacao]:
        return self.service.get_all()

    def buscar(self, notificacao_id: int) -> Optional[Notificacao]:
        return self.service.get_by_id(notificacao_id)

    def criar(self, notificacao_create: NotificacaoCreate) -> Notificacao:
        return self.service.create(notificacao_create)

    def atualizar(self, notificacao_id: int, notificacao_update: NotificacaoUpdate) -> Optional[Notificacao]:
        return self.service.update(notificacao_id, notificacao_update)

    def deletar(self, notificacao_id: int) -> bool:
        return self.service.delete(notificacao_id)
