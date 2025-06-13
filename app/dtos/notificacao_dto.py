from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class NotificacaoBase(BaseModel):
    mensagem: str = Field(..., min_length=5)
    data: Optional[datetime] = None
    usuario_id: int
    lido: Optional[bool] = False 


class NotificacaoCreate(NotificacaoBase):
    pass

class NotificacaoUpdate(BaseModel):
    mensagem: Optional[str] = None
    data: Optional[datetime] = None
    usuario_id: Optional[int] = None
    lido: Optional[bool] = False 


class NotificacaoRead(NotificacaoBase):
    id: int

    class Config:
        orm_mode = True
