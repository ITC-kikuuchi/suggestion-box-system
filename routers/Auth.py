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
