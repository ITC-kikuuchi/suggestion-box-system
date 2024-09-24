from fastapi import APIRouter

router = APIRouter()


# 意見一覧取得API
@router.get("/suggestions")
async def getSuggestions():
    pass


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
