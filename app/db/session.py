from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
# URL de la base de datos, con variables de entorno
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', "postgresql://user:password@localhost/dbname")

# Crear el motor de base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()
