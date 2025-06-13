from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.entities.tarefa_entity import TipoEsforcoEnum, StatusTarefaEnum, ClassificacaoPosTarefaEnum

class TarefaBase(BaseModel):
    titulo: str = Field(..., min_length=3)
    descricao: Optional[str] = None
    data_criacao: Optional[datetime] = None
    data_conclusao: Optional[datetime] = None
    usuario_id: int
    tipo_esforco: TipoEsforcoEnum
    status: Optional[StatusTarefaEnum] = StatusTarefaEnum.pendente
    classificacao_pos_tarefa: Optional[ClassificacaoPosTarefaEnum] = None
    prioridade: Optional[int] = None
    tempo_estimado: Optional[int] = None
    nivel_satisfacao_pos_tarefa: Optional[int] = None
    energia_pos_tarefa: Optional[int] = None

class TarefaCreate(TarefaBase):
    pass

class TarefaUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    data_criacao: Optional[datetime] = None
    data_conclusao: Optional[datetime] = None
    usuario_id: Optional[int] = None
    tipo_esforco: Optional[TipoEsforcoEnum] = None
    status: Optional[StatusTarefaEnum] = None
    classificacao_pos_tarefa: Optional[ClassificacaoPosTarefaEnum] = None
    prioridade: Optional[int] = None
    tempo_estimado: Optional[int] = None
    nivel_satisfacao_pos_tarefa: Optional[int] = None
    energia_pos_tarefa: Optional[int] = None

class TarefaRead(TarefaBase):
    id: int

    class Config:
        orm_mode = True
