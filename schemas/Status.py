from typing import Optional, List
from pydantic import BaseModel


class Status(BaseModel):
    id: int
    status: Optional[str]
    count: int


class StatusList(BaseModel):
    status_list: List[Status]

    class Config:
        orm_mode = True
