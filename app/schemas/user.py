from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: str
    full_name: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: Optional[datetime]  # Permitir que sea None si es necesario
    updated_at: Optional[datetime]  # Permitir que sea None si es necesario

    class Config:
        from_attributes = True  # Cambiado de orm_mode a from_attributes
