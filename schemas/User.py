from pydantic import validator
from utils.CustomBaseModel import CustomBaseModel


class LoginData(CustomBaseModel):
    mail_address: str
    password: str

    @validator("mail_address", "password", pre=True, always=True)
    def check_required(cls, value, field):
        error_messages = {
            "mail_address": "メールアドレスを入力してください",
            "password": "パスワードを入力してください",
        }
        if not value:
            raise ValueError(error_messages[field.name])
        return value
