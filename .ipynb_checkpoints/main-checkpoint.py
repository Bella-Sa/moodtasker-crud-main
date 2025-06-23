from fastapi import FastAPI
from app.database import Base, engine
from app.routes import (
    usuario_routes,
    tarefa_routes,
    historico_routes,
    notificacao_routes,
    dia_inativo_routes,
    agenda_tarefa_routes
)

app = FastAPI(title="MoodTasker API")

Base.metadata.create_all(bind=engine)

# Registrar as rotas (prefixos e tags já definidos nos routers)
app.include_router(usuario_routes.router)
app.include_router(tarefa_routes.router)
app.include_router(historico_routes.router)
app.include_router(notificacao_routes.router)
app.include_router(dia_inativo_routes.router)
app.include_router(agenda_tarefa_routes.router)

@app.get("/")
def root():
    return {"message": "API MoodTasker está rodando!"}
