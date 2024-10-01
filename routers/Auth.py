from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime, timedelta
from jose import jwt, JWTError

from Exceptions.UnauthorizedException import UnauthorizedException
from utils.ExceptionHandler import exception_handler

import os
import hashlib
import cruds.User as UserCrud
import schemas.User as UserSchema

router = APIRouter()


# トークン生成処理
def createTokens(user):
    # ペイロード生成
    accessPayload = {
        "token_type": "access_token",
        "exp": datetime.utcnow() + timedelta(minutes=60),
        "user_id": user.id,
    }
    # アクセストークンの生成
    accessToken = jwt.encode(accessPayload, os.environ["SECRET_KEY"], algorithm="HS256")
    # アクセストークンの返却
    return {
        "id": user.id,
        "unknown": user.unknown,
        "access_token": accessToken,
    }


# リクエストヘッダーからトークンを取得
def getBearerToken(authorization: str = Header(None)):
    if not authorization:
        raise UnauthorizedException
    if not authorization.startswith("Bearer "):
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


# ログインAPI
@router.post("/login")
async def login(formData: UserSchema.LoginData, db: Session = Depends(get_db)):
    try:
        # 入力された情報に紐づくユーザデータの取得
        user = UserCrud.getLoginUser(
            db,
            mail_address=formData.mail_address,
            password=hashlib.sha256(formData.password.encode("utf-8")).hexdigest(),
        )
        if not user:
            # ユーザデータが存在しない場合
            raise UnauthorizedException
    except Exception as e:
        return exception_handler(e)
    # トークン生成し返却
    return createTokens(user)


# ログインユーザ情報取得API
@router.get("/me", response_model=UserSchema.LoginUser)
async def me(loginUser: UserSchema.LoginUser = Depends(getCurrentUser)):
    return loginUser


# ログアウトAPI
@router.post("/logout")
def logout():
    pass
