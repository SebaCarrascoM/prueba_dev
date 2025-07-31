from pydantic import BaseModel, EmailStr, Field, validator
from typing import List
from datetime import datetime
import re

class Phone(BaseModel):
    number: str
    citycode: str
    contrycode: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phones: List[Phone]

    @validator('password')
    def validate_password(cls, v):
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=(?:.*\d){2})[A-Za-z\d]{6,}$', v):
            raise ValueError("La contraseña no cumple con el formato requerido")
        return v

class UserResponse(UserCreate):
    id: str
    created: str
    modified: str
    last_login: str
    token: str
    isactive: bool

class UserDB(BaseModel):
    id: str
    name: str
    email: EmailStr
    phones: List[Phone]
    created: datetime
    modified: datetime
    last_login: datetime
    token: str
    isactive: bool