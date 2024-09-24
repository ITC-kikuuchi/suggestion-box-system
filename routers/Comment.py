from fastapi import APIRouter

router = APIRouter()


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
