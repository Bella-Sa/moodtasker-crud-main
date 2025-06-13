from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.controllers.dia_inativo_controller import DiaInativoController
from app.dtos.dia_inativo_dto import DiaInativoCreate, DiaInativoUpdate, DiaInativoRead

router = APIRouter(tags=["Dias Inativos"])

@router.get("/", response_model=List[DiaInativoRead])
def listar_dias_inativos(db: Session = Depends(get_db)):
    return DiaInativoController(db).listar()

@router.get("/{dia_inativo_id}", response_model=DiaInativoRead)
def buscar_dia_inativo(dia_inativo_id: int, db: Session = Depends(get_db)):
    dia_inativo = DiaInativoController(db).buscar(dia_inativo_id)
    if not dia_inativo:
        raise HTTPException(status_code=404, detail="Dia Inativo não encontrado")
    return dia_inativo

@router.post("/", response_model=DiaInativoRead, status_code=status.HTTP_201_CREATED)
def criar_dia_inativo(dia_inativo_create: DiaInativoCreate, db: Session = Depends(get_db)):
    return DiaInativoController(db).criar(dia_inativo_create)

@router.put("/{dia_inativo_id}", response_model=DiaInativoRead)
def atualizar_dia_inativo(dia_inativo_id: int, dia_inativo_update: DiaInativoUpdate, db: Session = Depends(get_db)):
    dia_inativo = DiaInativoController(db).atualizar(dia_inativo_id, dia_inativo_update)
    if not dia_inativo:
        raise HTTPException(status_code=404, detail="Dia Inativo não encontrado")
    return dia_inativo

@router.delete("/{dia_inativo_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_dia_inativo(dia_inativo_id: int, db: Session = Depends(get_db)):
    sucesso = DiaInativoController(db).deletar(dia_inativo_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Dia Inativo não encontrado")
