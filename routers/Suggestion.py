from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db


from utils.ExceptionHandler import exception_handler
from utils.CheckToken import getCurrentUser

from constants import UNKNOWN, DATE_FORMAT_YMD


import schemas.Suggestion as SuggestionSchema
import cruds.Suggestion as SuggestionCrud

router = APIRouter()


# 意見一覧取得API
@router.get("/suggestions", response_model=SuggestionSchema.SuggestionList)
async def getSuggestions(
    loginUser: dict = Depends(getCurrentUser), db: Session = Depends(get_db)
):
    formattedSuggestions = []
    try:
        # 意見一覧取得
        suggestions = SuggestionCrud.getSuggestions(db)
        for suggestion in suggestions:
            categoryList = []
            for category in suggestion.suggestionCategory:
                categoryList.append(
                    {
                        "category_id": category.category.id,
                        "category": category.category.category,
                    }
                )

            formattedSuggestion = SuggestionSchema.Suggestion(
                id=suggestion.id,
                unknown=UNKNOWN,
                title=suggestion.title,
                created_at=suggestion.created_at.strftime(DATE_FORMAT_YMD),
                status_id=suggestion.status_id,
                category_list=categoryList,
            )
            formattedSuggestions.append(formattedSuggestion)

        # レスポンス作成
        response = SuggestionSchema.SuggestionList(suggestion_list=formattedSuggestions)
    except Exception as e:
        return exception_handler(e)
    return response


# 意見登録API
@router.post("/suggestions")
async def createSuggestion():
    pass


# 意見詳細取得API
@router.get("/suggestions/{suggestion_id}")
async def getSuggestionDetail():
    pass


# 意見削除API
@router.delete("/suggestions/{suggestion_id}")
async def deleteSuggestion():
    pass


# 意見解決API
@router.put("/suggestions/resolved/{suggestion_id}")
async def resolveSuggestion():
    pass
