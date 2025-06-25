from typing import List, Optional
from sqlalchemy.orm import Session
from app.entities.usuario_entity import Usuario
from app.dtos.usuario_dto import UsuarioCreate, UsuarioUpdate

class UsuarioService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Usuario]:
        return self.db.query(Usuario).filter(Usuario.ativo == True).order_by(Usuario.id).all()

    def get_by_id(self, usuario_id: int) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.id == usuario_id, Usuario.ativo == True).first()
    
    def get_by_email(self, email: str) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.email == email, Usuario.ativo == True).first()

    def create(self, usuario_create: UsuarioCreate) -> Usuario:
        usuario = Usuario(**usuario_create.dict())
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario


        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario


    def update(self, usuario_id: int, usuario_update: UsuarioUpdate) -> Optional[Usuario]:
        usuario = self.get_by_id(usuario_id)
        if not usuario:
            return None
        update_data = usuario_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(usuario, key, value)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def delete(self, usuario_id: int) -> bool:
        usuario = self.get_by_id(usuario_id)
        if not usuario:
            return False
        # usuario.ativo = False  # exclusão lógica soft delete
        # Se quiser realmente deletar, use:
        self.db.delete(usuario) #exclusão fisica real
        self.db.commit()
        return True
