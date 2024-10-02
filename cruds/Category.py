from sqlalchemy.orm import Session, joinedload

from models.Category import Category


# カテゴリー一覧取得
def getCategories(db: Session):
    return db.query(Category).options(joinedload(Category.suggestionCategory)).all()
