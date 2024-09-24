from fastapi import FastAPI

import logging

# ロギングの設定
logging.basicConfig(
    filename="app.log", level=logging.DEBUG, format="%(asctime)s %(message)s"
)

from routers import Auth, Suggestion, Category, Status, Comment

app = FastAPI()
app.include_router(Auth.router)
app.include_router(Suggestion.router)
app.include_router(Category.router)
app.include_router(Status.router)
app.include_router(Comment.router)
