from sqlalchemy.orm import Session, joinedload

from models.Status import Status

# ステータス一覧取得
def getStatuses(db: Session):
    return db.query(Status).options(joinedload(Status.suggestion)).all()
