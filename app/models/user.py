from sqlalchemy import Column, Integer, String, DateTime
from app.db.session import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, index=True)
    # Campos de timestamp
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Generado al crear
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())  # Actualizado en cada modificación
