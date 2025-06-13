from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import traceback

from app.database import get_db
from app.controllers.usuario_controller import UsuarioController
from app.dtos.usuario_dto import UsuarioCreate, UsuarioUpdate, UsuarioRead

router = APIRouter(tags=["Usuarios"])

@router.get("/", response_model=List[UsuarioRead])
def listar_usuarios(db: Session = Depends(get_db)):
    return UsuarioController(db).listar()


@router.get("/{usuario_id}", response_model=UsuarioRead)
def buscar_usuario(usuario_id: int, db: Session = Depends(get_db)):
        usuario = UsuarioController(db).buscar(usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return usuario

    
@router.post("/", response_model=UsuarioRead, status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario_create: UsuarioCreate, db: Session = Depends(get_db)):
    return UsuarioController(db).criar(usuario_create)

@router.put("/{usuario_id}", response_model=UsuarioRead)
def atualizar_usuario(usuario_id: int, usuario_update: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = UsuarioController(db).atualizar(usuario_id, usuario_update)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        sucesso = UsuarioController(db).deletar(usuario_id)
        if not sucesso:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
    except Exception as e:
        traceback.print_exc()  # imprime o erro completo no console
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
