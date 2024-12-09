from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc

from models.Suggestion import Suggestion
from models.SuggestionCategory import SuggestionCategory
from models.SuggestionComment import SuggestionComment


# 意見一覧取得
def getSuggestions(db: Session):
    return (
        db.query(Suggestion)
        .options(
            joinedload(Suggestion.suggestionCategory).joinedload(
                SuggestionCategory.category
            )
        )
        .order_by(desc(Suggestion.created_at))
        .all()
    )


# 意見登録
def createSuggestion(db: Session, suggestion):
    newSuggestion = Suggestion(**suggestion)
    db.add(newSuggestion)
    db.commit()
    db.refresh(newSuggestion)
    return newSuggestion.id


# 意見詳細取得
def getSuggestionDetail(db: Session, suggestionId):
    return (
        db.query(Suggestion)
        .filter(Suggestion.id == suggestionId)
        .options(
            joinedload(Suggestion.suggestionCategory).joinedload(
                SuggestionCategory.category
            ),
            joinedload(Suggestion.suggestionComment),
        )
        .first()
    )


# 意見削除
def deleteSuggestion(db: Session, suggestionId):
    db.query(SuggestionComment).filter(
        SuggestionComment.suggestion_id == suggestionId
    ).delete(synchronize_session=False)
    db.query(SuggestionCategory).filter(
        SuggestionCategory.suggestion_id == suggestionId
    ).delete(synchronize_session=False)
    db.query(Suggestion).filter(Suggestion.id == suggestionId).delete(
        synchronize_session=False
    )
    db.commit()


# 意見解決
def resolvedSuggestion(db: Session, suggestionId, statusId):
    suggestion = db.query(Suggestion).filter(Suggestion.id == suggestionId).first()
    suggestion.status_id = statusId
    db.commit()
