from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from Exceptions.NotFoundException import NotFoundException


from utils.ExceptionHandler import exception_handler
from utils.CheckToken import getCurrentUser

from constants import UNKNOWN, DATE_FORMAT_YMD, STATUS_UNRESOLVED, UNKNOWN_CREATED_ID


import schemas.Suggestion as SuggestionSchema
import cruds.Suggestion as SuggestionCrud
import cruds.SuggestionCategory as SuggestionCategory

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
async def createSuggestion(
    item: SuggestionSchema.createSuggestion,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    response = []
    try:
        suggestion = {
            "title": item.title,
            "contents": item.contents,
            "status_id": STATUS_UNRESOLVED,
            "created_id": UNKNOWN_CREATED_ID,
        }
        suggestionId = SuggestionCrud.createSuggestion(db, suggestion)

        for categoryId in item.category_list:
            suggestionCategory = {
                "suggestion_id": suggestionId,
                "category_id": categoryId,
            }
            SuggestionCategory.createSuggestionCategory(db, suggestionCategory)

    except Exception as e:
        return exception_handler(e)
    return response


# 意見詳細取得API
@router.get(
    "/suggestions/{suggestion_id}", response_model=SuggestionSchema.SuggestionDetail
)
async def getSuggestionDetail(
    suggestion_id: int,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    try:
        # 意見詳細取得
        suggestion = SuggestionCrud.getSuggestionDetail(db, suggestion_id)
        # カテゴリ一覧の作成
        categoryList = []
        for category in suggestion.suggestionCategory:
            categoryList.append(
                {
                    "category_id": category.category.id,
                    "category": category.category.category,
                }
            )
        # コメント一覧の作成
        commentList = []
        for comment in suggestion.suggestionComment:
            commentList.append(
                {
                    "comment_id": comment.id,
                    "comment": comment.comment,
                    "created_id": comment.created_id,
                }
            )
        # レスポンスの作成
        response = SuggestionSchema.SuggestionDetail(
            id=suggestion.id,
            unknown=UNKNOWN,
            title=suggestion.title,
            created_at=suggestion.created_at.strftime(DATE_FORMAT_YMD),
            status_id=suggestion.status_id,
            category_list=categoryList,
            comment_list=commentList,
        )
    except Exception as e:
        return exception_handler(e)
    return response


# 意見削除API
@router.delete("/suggestions/{suggestion_id}")
async def deleteSuggestion(
    suggestion_id: int,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    try:
        # ID に紐づく意見の取得
        suggestion = SuggestionCrud.getSuggestionDetail(db, suggestion_id)
        # データ存在チェック
        if not suggestion:
            # id に紐づくデータが存在しなかった場合
            raise NotFoundException
        # id に紐づくデータの削除
        SuggestionCrud.deleteSuggestion(db, suggestion_id)
    except Exception as e:
        return exception_handler(e)


# 意見解決API
@router.put("/suggestions/resolved/{suggestion_id}")
async def resolveSuggestion():
    pass
