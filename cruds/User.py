from sqlalchemy.orm import Session

import models.User as UserModel


# ログインユーザ取得
def getLoginUser(db: Session, mail: str, password: str):
    return (
        db.query(UserModel.User)
        .filter(
            UserModel.User.mail_address == mail,
            UserModel.User.password == password,
        )
        .first()
    )