from pydantic import BaseModel, ValidationError
from fastapi import HTTPException


class CustomBaseModel(BaseModel):
    @classmethod
    def validate(cls, values):
        try:
            return super().validate(values)
        except ValidationError as e:
            # エラーメッセージのカスタマイズ
            detail = {}
            for error in e.errors():
                field_name = error["loc"][0]  # フィールド名
                message = error["msg"]  # メッセージ
                detail.setdefault(field_name, []).append(message)
            raise HTTPException(status_code=422, detail=detail)
