from sqlalchemy import Column, Integer, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class DiaInativo(Base):
    __tablename__ = "dia_inativo"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    data = Column(Date, nullable=False)
    motivo = Column(Text)

    usuario = relationship("Usuario", back_populates="dias_inativos")
