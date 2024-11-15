from pydantic import BaseModel

class CreateComment(BaseModel):
    suggestion_id: int
    comment: str