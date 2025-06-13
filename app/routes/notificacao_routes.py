from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import traceback

from app.database import get_db
from app.controllers.notificacao_controller import NotificacaoController
from app.dtos.notificacao_dto import NotificacaoCreate, NotificacaoUpdate, NotificacaoRead

router = APIRouter(tags=["Notificacoes"])

@router.get("/", response_model=List[NotificacaoRead])
def listar_notificacoes(db: Session = Depends(get_db)):
    return NotificacaoController(db).listar()

@router.get("/{notificacao_id}", response_model=NotificacaoRead)
def buscar_notificacao(notificacao_id: int, db: Session = Depends(get_db)):
    notificacao = NotificacaoController(db).buscar(notificacao_id)
    if not notificacao:
        raise HTTPException(status_code=404, detail="Notificação não encontrada")
    return notificacao

@router.post("/", response_model=NotificacaoRead, status_code=status.HTTP_201_CREATED)
def criar_notificacao(notificacao_create: NotificacaoCreate, db: Session = Depends(get_db)):
    return NotificacaoController(db).criar(notificacao_create)


@router.put("/{notificacao_id}", response_model=NotificacaoRead)
def atualizar_notificacao(notificacao_id: int, notificacao_update: NotificacaoUpdate, db: Session = Depends(get_db)):
    notificacao = NotificacaoController(db).atualizar(notificacao_id, notificacao_update)
    if not notificacao:
        raise HTTPException(status_code=404, detail="Notificação não encontrada")
    return notificacao

@router.delete("/{notificacao_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_notificacao(notificacao_id: int, db: Session = Depends(get_db)):
    sucesso = NotificacaoController(db).deletar(notificacao_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Notificação não encontrada")
