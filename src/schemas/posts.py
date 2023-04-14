from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from src.schemas import Pagination


class PostBase(BaseModel):
    title: str
    content: Optional[str] = None
    published: bool


class PostRequest(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PostManyResponse(Pagination):
    items: List[PostResponse]
    total: int
