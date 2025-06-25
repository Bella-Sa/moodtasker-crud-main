from typing import List, Optional
from sqlalchemy.orm import Session
from app.entities.tarefa_entity import Tarefa
from app.dtos.tarefa_dto import TarefaCreate, TarefaUpdate

class TarefaService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Tarefa]:
        self.db.expire_all()
        return self.db.query(Tarefa).order_by(Tarefa.id).all()

    def get_by_id(self, tarefa_id: int) -> Optional[Tarefa]:
        self.db.expire_all()
        return self.db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

    def create(self, tarefa_create: TarefaCreate) -> Tarefa:
        tarefa = Tarefa(**tarefa_create.dict())
        self.db.add(tarefa)
        self.db.commit()
        self.db.refresh(tarefa)
        return tarefa

    def update(self, tarefa_id: int, tarefa_update: TarefaUpdate) -> Optional[Tarefa]:
        tarefa = self.get_by_id(tarefa_id)
        if not tarefa:
            return None
        update_data = tarefa_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(tarefa, key, value)
        self.db.commit()
        self.db.refresh(tarefa)
        return tarefa

    def delete(self, tarefa_id: int) -> bool:
        tarefa = self.get_by_id(tarefa_id)
        if not tarefa:
            return False
        self.db.delete(tarefa)  # exclusão física
        self.db.commit()
        return True
