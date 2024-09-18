from sqlalchemy import Column, Integer, String, DateTime
from app.db.session import Base
from sqlalchemy.sql import func

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    url_post = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
    tags = Column(String, index=True)
    url_image = Column(String, index=True)
    # Campos de timestamp
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Valor por defecto al crear
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())  # Se actualiza en cada modificación