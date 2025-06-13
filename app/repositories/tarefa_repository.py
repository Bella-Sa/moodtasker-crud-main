from sqlalchemy.orm import Session
from app.entities.tarefa_entity import Tarefa
from typing import List, Optional

class TarefaRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Tarefa]:
        return self.db.query(Tarefa).all()

    def get_by_id(self, tarefa_id: int) -> Optional[Tarefa]:
        return self.db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

    def get_by_usuario(self, usuario_id: int) -> List[Tarefa]:
        return self.db.query(Tarefa).filter(Tarefa.usuario_id == usuario_id).all()

    def create(self, tarefa: Tarefa) -> Tarefa:
        self.db.add(tarefa)
        self.db.commit()
        self.db.refresh(tarefa)
        return tarefa

    def update(self, tarefa: Tarefa) -> Tarefa:
        self.db.commit()
        self.db.refresh(tarefa)
        return tarefa

    def delete(self, tarefa: Tarefa):
        self.db.delete(tarefa)
        self.db.commit()
