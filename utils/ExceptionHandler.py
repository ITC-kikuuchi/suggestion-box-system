from fastapi.responses import JSONResponse
import logging

from Exceptions.UnauthorizedException import UnauthorizedException
from Exceptions.ForbiddenException import ForbiddenException
from Exceptions.NotFoundException import NotFoundException


# 共通例外ハンドラー
def exception_handler(e: Exception) -> JSONResponse:
    logging.error(e)
    if isinstance(e, UnauthorizedException):
        return JSONResponse(status_code=401, content={"error": "Unauthorized"})
    elif isinstance(e, ForbiddenException):
        return JSONResponse(status_code=403, content={"error": "Forbidden"})
    elif isinstance(e, NotFoundException):
        return JSONResponse(status_code=404, content={"error": "Not Found"})
    else:
        return JSONResponse(
            status_code=500,
            content={"error": "Internal Server Error", "details": str(e)},
        )
