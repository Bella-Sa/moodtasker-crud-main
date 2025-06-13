from sqlalchemy.orm import Session
from typing import List, Optional
from app.services.agenda_tarefa_service import AgendaTarefaService
from app.dtos.agenda_tarefa_dto import AgendaTarefaCreate, AgendaTarefaUpdate
from app.entities.agenda_tarefa_entity import AgendaTarefa

class AgendaTarefaController:
    def __init__(self, db: Session):
        self.service = AgendaTarefaService(db)

    def listar(self) -> List[AgendaTarefa]:
        return self.service.get_all()

    def buscar(self, agenda_id: int) -> Optional[AgendaTarefa]:
        return self.service.get_by_id(agenda_id)

    def criar(self, agenda_create: AgendaTarefaCreate) -> AgendaTarefa:
        return self.service.create(agenda_create)

    def atualizar(self, agenda_id: int, agenda_update: AgendaTarefaUpdate) -> Optional[AgendaTarefa]:
        return self.service.update(agenda_id, agenda_update)

    def deletar(self, agenda_id: int) -> bool:
        return self.service.delete(agenda_id)
