from sqlalchemy.orm import Session
from app.entities.agenda_tarefa_entity import AgendaTarefa
from typing import List, Optional

class AgendaTarefaRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[AgendaTarefa]:
        return self.db.query(AgendaTarefa).all()

    def get_by_id(self, agenda_id: int) -> Optional[AgendaTarefa]:
        return self.db.query(AgendaTarefa).filter(AgendaTarefa.id == agenda_id).first()

    def get_by_tarefa(self, tarefa_id: int) -> List[AgendaTarefa]:
        return self.db.query(AgendaTarefa).filter(AgendaTarefa.tarefa_id == tarefa_id).all()

    def create(self, agenda: AgendaTarefa) -> AgendaTarefa:
        self.db.add(agenda)
        self.db.commit()
        self.db.refresh(agenda)
        return agenda

    def update(self, agenda: AgendaTarefa) -> AgendaTarefa:
        self.db.commit()
        self.db.refresh(agenda)
        return agenda

    def delete(self, agenda: AgendaTarefa):
        self.db.delete(agenda)
        self.db.commit()
