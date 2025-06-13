from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class DiaInativoBase(BaseModel):
    data: date
    motivo: str = Field(..., min_length=5)

class DiaInativoCreate(DiaInativoBase):
    usuario_id: int

class DiaInativoUpdate(BaseModel):
    data: Optional[date] = None
    motivo: Optional[str] = None
    usuario_id: Optional[int] = None


class DiaInativoRead(DiaInativoBase):
    id: int

    class Config:
        orm_mode = True
