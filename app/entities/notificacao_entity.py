from sqlalchemy import Column, Integer, Text, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Notificacao(Base):
    __tablename__ = "notificacao"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    data = Column(TIMESTAMP)
    mensagem = Column(Text, nullable=False)
    lido = Column(Boolean, default=False)

    usuario = relationship("Usuario", back_populates="notificacoes")
