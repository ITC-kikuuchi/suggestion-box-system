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

router = APIRouter()

# OAuth2PasswordBearerを使用してトークン取得用エンドポイントを設定
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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
async def login():
    pass


# ログイン情報取得API
@router.get("/me")
async def me():
    pass


# ログアウトAPI
@router.post("/logout")
def logout():
    pass
