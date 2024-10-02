from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db


from utils.ExceptionHandler import exception_handler
from utils.CheckToken import getCurrentUser


import schemas.Category as CategorySchema
import cruds.Category as CategoryCrud

router = APIRouter()


# カテゴリ一覧取得API
@router.get("/categories")
async def getCategories(
    loginUser: dict = Depends(getCurrentUser), db: Session = Depends(get_db)
):
    formattedCategories = []
    try:
        # カテゴリー一覧取得
        categories = CategoryCrud.getCategories(db)
        for category in categories:
            formattedCategory = CategorySchema.Category(
                id=category.id,
                category=category.category,
                count=len(category.suggestionCategory),
            )
            formattedCategories.append(formattedCategory)

        # レスポンス作成
        response = CategorySchema.CategoryList(category_list=formattedCategories)
    except Exception as e:
        return exception_handler(e)
    return response
