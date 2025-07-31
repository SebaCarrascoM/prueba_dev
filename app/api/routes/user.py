from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserResponse, UserDB
from app.models.user import build_user_dict
from app.db.user_repo import find_user_by_email, save_user, get_all_users
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserResponse, summary="Registrar un nuevo usuario")
async def register_user(user: UserCreate):
    """
    Registra un nuevo usuario si el correo no ha sido utilizado previamente.
    """
    # Verificar si ya existe un usuario con el mismo correo
    existing_user = await find_user_by_email(user.email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail={"mensaje": "Este correo ya ha sido registrado anteriormente."}
        )

    # Preparar y guardar la información del nuevo usuario
    user_data = build_user_dict(user.dict())
    await save_user(user_data)
    
    return user_data

@router.get("/", response_model=List[UserDB], summary="Listar todos los usuarios")
async def list_users():
    """
    Retorna todos los usuarios registrados.
    """
    users = await get_all_users()
    return users
