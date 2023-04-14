from fastapi import Query
from pydantic import BaseModel

from src.config import config


class Pagination(BaseModel):
    page: int = Query(1, ge=1)
    page_size: int = Query(config.POSTS_PER_PAGE, ge=1)
