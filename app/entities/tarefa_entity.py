from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class TipoEsforcoEnum(str, enum.Enum):
    leve = "leve"
    moderado = "moderado"
    intenso = "intenso"

class StatusTarefaEnum(str, enum.Enum):
    pendente = "pendente"
    completo = "completo"

class ClassificacaoPosTarefaEnum(str, enum.Enum):
    motivadora = "motivadora"
    neutra = "neutra"
    desgastante = "desgastante"

class Tarefa(Base):
    __tablename__ = "tarefa"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(Text)
    tipo_esforco = Column(Enum(TipoEsforcoEnum))
    prioridade = Column(Integer)
    tempo_estimado = Column(Integer)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    data_criacao = Column(TIMESTAMP)
    status = Column(Enum(StatusTarefaEnum), default=StatusTarefaEnum.pendente)
    data_conclusao = Column(TIMESTAMP)
    classificacao_pos_tarefa = Column(Enum(ClassificacaoPosTarefaEnum))
    nivel_satisfacao_pos_tarefa = Column(Integer)
    energia_pos_tarefa = Column(Integer)

    usuario = relationship("Usuario", back_populates="tarefas")
    agenda = relationship("AgendaTarefa", back_populates="tarefa")
