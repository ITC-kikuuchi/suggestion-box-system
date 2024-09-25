from fastapi import FastAPI, Request

import logging

from utils.ExceptionHandler import exception_handler

# ロギングの設定
logging.basicConfig(
    filename="app.log", level=logging.DEBUG, format="%(asctime)s %(message)s"
)


# グローバル例外ハンドラー
async def global_exception_handler(request: Request, exc: Exception):
    return exception_handler(exc)


from routers import Auth, Suggestion, Category, Status, Comment

app = FastAPI()
app.include_router(Auth.router)
app.include_router(Suggestion.router)
app.include_router(Category.router)
app.include_router(Status.router)
app.include_router(Comment.router)
