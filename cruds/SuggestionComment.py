from sqlalchemy.orm import Session

from models.SuggestionComment import SuggestionComment

# コメント登録
def createComment(db: Session, comment):
    newSuggestionComment = SuggestionComment(**comment)
    db.add(newSuggestionComment)
    db.commit()
    db.refresh(newSuggestionComment)