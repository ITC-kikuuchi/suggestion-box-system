from fastapi import APIRouter

router = APIRouter()


# ステータス一覧取得API
@router.get("/statuses")
async def getStatuses():
    pass
