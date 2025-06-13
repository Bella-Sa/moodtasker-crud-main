from sqlalchemy import Column, Integer, String, Date, Boolean, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM


class HumorEnum(str, enum.Enum):
    terrivel = "Terrível"
    ruim = "Ruim"
    neutro = "Neutro(a)"
    bom = "Bom/Boa"
    otimo = "Ótimo(a)"

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    humor = Column(PG_ENUM(HumorEnum, name="humor_enum", create_type=False, values_callable=lambda obj: [e.value for e in obj]), nullable=True)
    energia = Column(Integer)
    data_checkin = Column(Date)
    ativo = Column(Boolean, default=True)

    tarefas = relationship("Tarefa", back_populates="usuario")
    historico = relationship("Historico", back_populates="usuario")
    notificacoes = relationship("Notificacao", back_populates="usuario")
    dias_inativos = relationship("DiaInativo", back_populates="usuario")

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', email='{self.email}')>"