from sqlalchemy.orm import Session

from models.SuggestionComment import SuggestionComment

# コメント登録
def createComment(db: Session, comment):
    newSuggestionComment = SuggestionComment(**comment)
    db.add(newSuggestionComment)
    db.commit()
    db.refresh(newSuggestionComment)

# コメント詳細取得
def getCommentDetail(db: Session, comment_id):
    return (
        db.query(SuggestionComment)
        .filter(SuggestionComment.id == comment_id)
        .first()
    )

# コメント更新
def updateComment(db: Session, comment, original: SuggestionComment):
    for field, value in comment.items():
        setattr(original, field, value)
    db.commit()
    db.refresh(original)