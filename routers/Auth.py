from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime, timedelta
from jose import jwt

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


# ログインAPI
@router.post("/login")
async def login(formData: UserSchema.LoginData, db: Session = Depends(get_db)):
    try:
        # 入力された情報に紐づくユーザデータの取得
        user = UserCrud.getLoginUser(
            db,
            mail=formData.username,
            password=hashlib.sha256(formData.password.encode("utf-8")).hexdigest(),
        )
        if not user:
            # ユーザデータが存在しない場合
            raise UnauthorizedException
    except Exception as e:
        return exception_handler(e)
    # トークン生成し返却
    return createTokens(user)


# ログイン情報取得API
@router.get("/me")
async def me():
    pass


# ログアウトAPI
@router.post("/logout")
def logout():
    pass
