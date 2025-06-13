from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.controllers.historico_controller import HistoricoController
from app.dtos.historico_dto import HistoricoCreate, HistoricoUpdate, HistoricoRead

router = APIRouter(tags=["Historicos"])

@router.get("/", response_model=List[HistoricoRead])
def listar_historicos(db: Session = Depends(get_db)):
    return HistoricoController(db).listar()

@router.get("/{historico_id}", response_model=HistoricoRead)
def buscar_historico(historico_id: int, db: Session = Depends(get_db)):
    historico = HistoricoController(db).buscar(historico_id)
    if not historico:
        raise HTTPException(status_code=404, detail="Histórico não encontrado")
    return historico

@router.post("/", response_model=HistoricoRead, status_code=status.HTTP_201_CREATED)
def criar_historico(historico_create: HistoricoCreate, db: Session = Depends(get_db)):
    return HistoricoController(db).criar(historico_create)

@router.put("/{historico_id}", response_model=HistoricoRead)
def atualizar_historico(historico_id: int, historico_update: HistoricoUpdate, db: Session = Depends(get_db)):
    historico = HistoricoController(db).atualizar(historico_id, historico_update)
    if not historico:
        raise HTTPException(status_code=404, detail="Histórico não encontrado")
    return historico

@router.delete("/{historico_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_historico(historico_id: int, db: Session = Depends(get_db)):
    sucesso = HistoricoController(db).deletar(historico_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Histórico não encontrado")
