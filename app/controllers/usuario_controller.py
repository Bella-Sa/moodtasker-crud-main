from sqlalchemy.orm import Session
from typing import List, Optional
from app.services.usuario_service import UsuarioService
from app.dtos.usuario_dto import UsuarioCreate, UsuarioUpdate
from app.entities.usuario_entity import Usuario
from fastapi import HTTPException

class UsuarioController:
    def __init__(self, db: Session):
        self.service = UsuarioService(db)

    def listar(self) -> List[Usuario]:
        return self.service.get_all()

    def buscar(self, usuario_id: int) -> Optional[Usuario]:
        return self.service.get_by_id(usuario_id)

    def criar(self, usuario_create: UsuarioCreate) -> Usuario:
        return self.service.create(usuario_create)

    def atualizar(self, usuario_id: int, usuario_update: UsuarioUpdate) -> Optional[Usuario]:
        return self.service.update(usuario_id, usuario_update)

    def deletar(self, usuario_id: int) -> bool:
        return self.service.delete(usuario_id)
    
    def get_by_email(self, email: str):
        user = self.service.get_by_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return user