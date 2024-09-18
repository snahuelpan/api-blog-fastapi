from sqlalchemy.orm import Session
from app.models.article import Article
from app.schemas.article import ArticleCreate

def get_article(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()

def get_article_by_name(db: Session, name: str):
    return db.query(Article).filter(Article.name == name).first()

def create_article(db: Session, article: ArticleCreate):
    url_post_create = f"/artucle/{article.name}"
    url_image_create = f"/images/{article.name}.png"
    db_article = Article(name=article.name, url_post=url_post_create ,description=article.description,tags=article.tags, url_image=url_image_create)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article