from sqlalchemy.orm import Session
from typing import List, Optional
from app.services.tarefa_service import TarefaService
from app.dtos.tarefa_dto import TarefaCreate, TarefaUpdate
from app.entities.tarefa_entity import Tarefa

class TarefaController:
    def __init__(self, db: Session):
        self.service = TarefaService(db)

    def listar(self) -> List[Tarefa]:
        return self.service.get_all()

    def buscar(self, tarefa_id: int) -> Optional[Tarefa]:
        return self.service.get_by_id(tarefa_id)

    def criar(self, tarefa_create: TarefaCreate) -> Tarefa:
        return self.service.create(tarefa_create)

    def atualizar(self, tarefa_id: int, tarefa_update: TarefaUpdate) -> Optional[Tarefa]:
        return self.service.update(tarefa_id, tarefa_update)

    def deletar(self, tarefa_id: int) -> bool:
        return self.service.delete(tarefa_id)
