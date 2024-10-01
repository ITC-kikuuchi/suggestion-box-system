from fastapi import Depends, Header
from sqlalchemy.orm import Session
from database import get_db
from jose import jwt, JWTError

from Exceptions.UnauthorizedException import UnauthorizedException
from utils.ExceptionHandler import exception_handler

import os
import cruds.User as UserCrud


# リクエストヘッダーからトークンを取得
def getBearerToken(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise UnauthorizedException
    return authorization.split(" ")[1]


# トークンを検証してユーザーを取得
def getCurrentUser(token: str = Depends(getBearerToken), db: Session = Depends(get_db)):
    try:
        # トークンをデコードしてペイロードを取得
        payload = jwt.decode(token, os.environ["SECRET_KEY"], algorithms=["HS256"])
        # ID に紐づくユーザ情報の取得
        user = UserCrud.getUserById(db, payload["user_id"])
        if not user:
            # ID に紐づくユーザ情報が存在しない場合
            raise UnauthorizedException
        return user
    except JWTError:
        raise UnauthorizedException
    except Exception as e:
        return exception_handler(e)
