from fastapi import APIRouter

router = APIRouter()


# カテゴリ一覧取得API
@router.get("/categories")
async def getCategories():
    pass
