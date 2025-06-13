from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date
from app.entities.usuario_entity import HumorEnum

class UsuarioBase(BaseModel):
    nome: str = Field(..., min_length=3)
    email: EmailStr
    humor: Optional[HumorEnum] = None
    energia: Optional[int] = None
    ativo: Optional[bool] = True
    data_checkin: Optional[date] = None

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    humor: Optional[HumorEnum] = None
    energia: Optional[int] = None
    ativo: Optional[bool] = None
    data_checkin: Optional[date] = None

class UsuarioRead(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
