from fastapi import FastAPI
from app.api.routes import user

app = FastAPI(
    tittle = "Creacion de Usuarios",
    description = "Registrar Usuarios por API RESTful"
)
app.include_router(user.router, prefix="/api")