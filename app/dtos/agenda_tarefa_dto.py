from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, time

class AgendaTarefaBase(BaseModel):
    tarefa_id: int
    data: date
    hora_inicio: time
    hora_fim: time

class AgendaTarefaCreate(AgendaTarefaBase):
    pass

class AgendaTarefaUpdate(BaseModel):
    tarefa_id: Optional[int] = None
    data: Optional[date] = None
    hora_inicio: Optional[time] = None
    hora_fim: Optional[time] = None

class AgendaTarefaRead(AgendaTarefaBase):
    id: int

    class Config:
        orm_mode = True
