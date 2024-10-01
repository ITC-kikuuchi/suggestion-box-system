from sqlalchemy.orm import Session

import models.User as UserModel


# ログインユーザ取得
def getLoginUser(db: Session, mail_address: str, password: str):
    return (
        db.query(UserModel.User)
        .filter(
            UserModel.User.mail_address == mail_address,
            UserModel.User.password == password,
        )
        .first()
    )


# ID に紐づくユーザ取得
def getUserById(db: Session, id: int):
    return db.query(UserModel.User).filter(UserModel.User.id == id).first()
