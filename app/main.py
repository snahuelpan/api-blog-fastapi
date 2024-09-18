from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models
from app.db.session import SessionLocal, engine
from app.schemas.user import UserOut, UserCreate
from app.schemas.article import ArticleOut, ArticleCreate
from app.crud import user as crud_user
from app.crud import article as crud_article

# Crear las tablas de la base de datos si no existen
models.Base.metadata.create_all(bind=engine)

# Crear la instancia de FastAPI
app = FastAPI()

# Dependencia para obtener una sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta de ejemplo para crear un usuario
@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db=db, user=user)

# Ruta de ejemplo para obtener usuarios
@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/articles/", response_model=ArticleOut)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    db_article = crud_article.get_article_by_name(db, name=article.name)
    if db_article:
        raise HTTPException(status_code=400, detail="Article already registered")
    return crud_article.create_article(db=db, article=article)

@app.get("/articles/{article_id}", response_model=ArticleOut)
def get_user(article_id: int, db: Session = Depends(get_db)):
    db_article = crud_article.get_article(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article