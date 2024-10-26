from sqlalchemy.orm import Session

from models.SuggestionCategory import SuggestionCategory


# 意見に関するカテゴリの登録
def createSuggestionCategory(db: Session, suggestionCategory):
    newSuggestionCategory = SuggestionCategory(**suggestionCategory)
    db.add(newSuggestionCategory)
    db.commit()
    db.refresh(newSuggestionCategory)
