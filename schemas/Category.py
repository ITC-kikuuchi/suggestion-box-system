from typing import Optional, List
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    category: Optional[str]
    count: int


class CategoryList(BaseModel):
    category_list: List[Category]

    class Config:
        orm_mode = True
