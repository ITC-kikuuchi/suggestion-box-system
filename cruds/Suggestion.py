from sqlalchemy.orm import Session, joinedload

from models.Suggestion import Suggestion
from models.SuggestionCategory import SuggestionCategory


# 意見一覧取得
def getSuggestions(db: Session):
    return (
        db.query(Suggestion)
        .options(
            joinedload(Suggestion.suggestionCategory).joinedload(
                SuggestionCategory.category
            )
        )
        .all()
    )
