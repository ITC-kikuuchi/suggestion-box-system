from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import logging
import os

from utils.ExceptionHandler import exception_handler

app = FastAPI()

# ロギングの設定
logging.basicConfig(
    filename="app.log", level=logging.DEBUG, format="%(asctime)s %(message)s"
)


# グローバル例外ハンドラー
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return exception_handler(exc)


from routers import Auth, Suggestion, Category, Status, Comment

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ["FRONTEND_URL"]],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Auth.router)
app.include_router(Suggestion.router)
app.include_router(Category.router)
app.include_router(Status.router)
app.include_router(Comment.router)
