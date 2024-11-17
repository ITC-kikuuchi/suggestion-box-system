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
async def createComment(
    item: SuggestionCommentSchema.CreateComment,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    response = []
    try:
        # 意見詳細取得
        suggestion = SuggestionCrud.getSuggestionDetail(db, item.suggestion_id)
        # データ存在チェック
        if not suggestion:
            # id に紐づくデータが存在しなかった場合
            raise NotFoundException

        comment = {
            "suggestion_id": item.suggestion_id,
            "comment": item.comment,
            "created_id": UNKNOWN_CREATED_ID,
        }
        # コメント登録
        SuggestionCommentCrud.createComment(db, comment)
    except Exception as e:
        return exception_handler(e)
    return response


# コメント更新API
@router.put("/comments/{comment_id}")
async def updateComment(
    comment_id: int,
    item: SuggestionCommentSchema.UpdateComment,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    response = []
    try:
        # コメント詳細取得
        comment = SuggestionCommentCrud.getCommentDetail(db, comment_id)
        if not comment:
            # id に紐づくデータが存在しなかった場合
            raise NotFoundException

        updateComment = {
            "comment": item.comment,
        }
        # コメント更新
        SuggestionCommentCrud.updateComment(db, updateComment, comment)
    except Exception as e:
        return exception_handler(e)
    return response


# コメント削除API
@router.delete("/comments/{comment_id}")
async def deleteComment():
    pass
