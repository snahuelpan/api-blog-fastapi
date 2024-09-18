from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ArticleBase(BaseModel):
    name: str
    description: str

class ArticleCreate(ArticleBase):
    tags: str


class ArticleOut(ArticleBase):
    id: int
    created_at: Optional[datetime]  # Permitir que sea None si es necesario
    updated_at: Optional[datetime]  # Permitir que sea None si es necesario


    class Config:
        from_attributes = True  # Cambiado de orm_mode a from_attributes