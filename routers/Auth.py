from fastapi import APIRouter

router = APIRouter()


# ログインAPI
@router.post("/login")
async def login():
    pass


# ログイン情報取得API
@router.get("/me")
async def me():
    pass


# ログアウトAPI
@router.post("/logout")
def logout():
    pass
