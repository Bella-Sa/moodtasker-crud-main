from typing import List, Optional
from sqlalchemy.orm import Session
from app.entities.agenda_tarefa_entity import AgendaTarefa
from app.dtos.agenda_tarefa_dto import AgendaTarefaCreate, AgendaTarefaUpdate

class AgendaTarefaService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[AgendaTarefa]:
        #return self.db.query(AgendaTarefa).all()
        return self.db.query(AgendaTarefa).filter(AgendaTarefa.tarefa_id.isnot(None)).all()

    def get_by_id(self, agenda_id: int) -> Optional[AgendaTarefa]:
        return self.db.query(AgendaTarefa).filter(AgendaTarefa.id == agenda_id).first()

    def create(self, agenda_create: AgendaTarefaCreate) -> AgendaTarefa:
        agenda = AgendaTarefa(**agenda_create.dict())
        self.db.add(agenda)
        self.db.commit()
        self.db.refresh(agenda)
        return agenda

    def update(self, agenda_id: int, agenda_update: AgendaTarefaUpdate) -> Optional[AgendaTarefa]:
        agenda = self.get_by_id(agenda_id)
        if not agenda:
            return None
        update_data = agenda_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(agenda, key, value)
        self.db.commit()
        self.db.refresh(agenda)
        return agenda

    def delete(self, agenda_id: int) -> bool:
        agenda = self.get_by_id(agenda_id)
        if not agenda:
            return False
        self.db.delete(agenda) #exclusão fisica real
        self.db.commit()
        return True
