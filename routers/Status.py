from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db


from utils.ExceptionHandler import exception_handler
from utils.CheckToken import getCurrentUser


import schemas.Status as StatusSchema
import cruds.Status as StatusCrud

router = APIRouter()


# ステータス一覧取得API
@router.get("/statuses", response_model=StatusSchema.StatusList)
async def getStatuses(
    loginUser: dict = Depends(getCurrentUser), db: Session = Depends(get_db)
):
    formattedStatuses = []
    try:
        # ステータス一覧取得
        statuses = StatusCrud.getStatuses(db)
        for status in statuses:
            formattedStatus = StatusSchema.Status(
                id=status.id,
                status=status.status,
                count=len(status.suggestion),
            )
            formattedStatuses.append(formattedStatus)

        # レスポンス作成
        response = StatusSchema.StatusList(status_list=formattedStatuses)
    except Exception as e:
        return exception_handler(e)
    return response
