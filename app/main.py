from fastapi import FastAPI
from app.database import Base, engine
from app.routes import usuario_routes, tarefa_routes, historico_routes, notificacao_routes, dia_inativo_routes, agenda_tarefa_routes
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True, debug=True)

app = FastAPI(title="MoodTasker API")

# Criação das tabelas
Base.metadata.create_all(bind=engine)

# Registro de rotas
app.include_router(usuario_routes.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(tarefa_routes.router, prefix="/tarefas", tags=["Tarefas"])
app.include_router(historico_routes.router, prefix="/historicos", tags=["Históricos"])
app.include_router(notificacao_routes.router, prefix="/notificacoes", tags=["Notificações"])
app.include_router(dia_inativo_routes.router, prefix="/dias-inativos", tags=["Dias Inativos"])
app.include_router(agenda_tarefa_routes.router, prefix="/agendas", tags=["Agendas de Tarefa"])
