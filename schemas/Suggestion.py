from typing import Optional, List
from pydantic import BaseModel


class Category(BaseModel):
    category_id: int
    category: str


class Suggestion(BaseModel):
    id: int
    unknown: Optional[str]
    title: Optional[str]
    created_at: Optional[str]
    status_id: int
    category_list: List[Category]


class SuggestionList(BaseModel):
    suggestion_list: List[Suggestion]

    class Config:
        orm_mode = True
