from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class HistoricoBase(BaseModel):
    data: Optional[date] = None
    usuario_id: int
    energia: Optional[int] = None
    humor: Optional[str] = None
    tempo_total_tarefas: Optional[int] = None

class HistoricoCreate(HistoricoBase):
    pass

class HistoricoUpdate(BaseModel):
    data: Optional[date] = None
    usuario_id: Optional[int] = None
    energia: Optional[int] = None
    humor: Optional[str] = None
    tempo_total_tarefas: Optional[int] = None

class HistoricoRead(HistoricoBase):
    id: int

    class Config:
        orm_mode = True
