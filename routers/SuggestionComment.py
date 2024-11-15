from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from Exceptions.NotFoundException import NotFoundException
from utils.ExceptionHandler import exception_handler
from utils.CheckToken import getCurrentUser

from constants import UNKNOWN_CREATED_ID

router = APIRouter()

import schemas.SuggestionComment as SuggestionCommentSchema
import cruds.Suggestion as SuggestionCrud
import cruds.SuggestionComment as SuggestionCommentCrud

# コメント登録API
@router.post("/comments")
async def createComment():
    pass


# コメント更新API
@router.put("/comments/{comment_id}")
async def updateComment():
    pass


# コメント削除API
@router.delete("/comments/{comment_id}")
async def deleteComment():
    pass
