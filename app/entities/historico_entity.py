from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Historico(Base):
    __tablename__ = "historico"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    data = Column(Date, nullable=False)
    humor = Column(String(50))
    energia = Column(Integer)
    tempo_total_tarefas = Column(Integer)

    usuario = relationship("Usuario", back_populates="historico")
