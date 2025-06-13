from sqlalchemy.orm import Session
from app.entities.usuario_entity import Usuario
from typing import List, Optional

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Usuario]:
        return self.db.query(Usuario).all()

    def get_by_id(self, usuario_id: int) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.id == usuario_id).first()

    def get_by_email(self, email: str) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.email == email).first()

    def create(self, usuario: Usuario) -> Usuario:
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def update(self, usuario: Usuario) -> Usuario:
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def delete(self, usuario: Usuario):
        self.db.delete(usuario)
        self.db.commit()
