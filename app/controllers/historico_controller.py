from sqlalchemy.orm import Session
from typing import List, Optional
from app.services.historico_service import HistoricoService
from app.dtos.historico_dto import HistoricoCreate, HistoricoUpdate
from app.entities.historico_entity import Historico

class HistoricoController:
    def __init__(self, db: Session):
        self.service = HistoricoService(db)

    def listar(self) -> List[Historico]:
        return self.service.get_all()

    def buscar(self, historico_id: int) -> Optional[Historico]:
        return self.service.get_by_id(historico_id)

    def criar(self, historico_create: HistoricoCreate) -> Historico:
        return self.service.create(historico_create)

    def atualizar(self, historico_id: int, historico_update: HistoricoUpdate) -> Optional[Historico]:
        return self.service.update(historico_id, historico_update)

    def deletar(self, historico_id: int) -> bool:
        return self.service.delete(historico_id)
