from sqlalchemy.orm import Session
from typing import List, Optional
from app.services.dia_inativo_service import DiaInativoService
from app.dtos.dia_inativo_dto import DiaInativoCreate, DiaInativoUpdate
from app.entities.dia_inativo_entity import DiaInativo

class DiaInativoController:
    def __init__(self, db: Session):
        self.service = DiaInativoService(db)

    def listar(self) -> List[DiaInativo]:
        return self.service.get_all()

    def buscar(self, dia_inativo_id: int) -> Optional[DiaInativo]:
        return self.service.get_by_id(dia_inativo_id)

    def criar(self, dia_inativo_create: DiaInativoCreate) -> DiaInativo:
        return self.service.create(dia_inativo_create)

    def atualizar(self, dia_inativo_id: int, dia_inativo_update: DiaInativoUpdate) -> Optional[DiaInativo]:
        return self.service.update(dia_inativo_id, dia_inativo_update)

    def deletar(self, dia_inativo_id: int) -> bool:
        return self.service.delete(dia_inativo_id)
