from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import traceback

from app.database import get_db
from app.controllers.tarefa_controller import TarefaController
from app.dtos.tarefa_dto import TarefaCreate, TarefaUpdate, TarefaRead

router = APIRouter(tags=["Tarefas"])

@router.get("/", response_model=List[TarefaRead])
def listar_tarefas(db: Session = Depends(get_db)):
    return TarefaController(db).listar()

@router.get("/{tarefa_id}", response_model=TarefaRead)
def buscar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = TarefaController(db).buscar(tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

    
@router.post("/", response_model=TarefaRead, status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa_create: TarefaCreate, db: Session = Depends(get_db)):
    try:
        return TarefaController(db).criar(tarefa_create)
    except Exception as e:
        # Log completo do erro
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@router.put("/{tarefa_id}", response_model=TarefaRead)
def atualizar_tarefa(tarefa_id: int, tarefa_update: TarefaUpdate, db: Session = Depends(get_db)):
    tarefa = TarefaController(db).atualizar(tarefa_id, tarefa_update)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

@router.delete("/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    sucesso = TarefaController(db).deletar(tarefa_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
