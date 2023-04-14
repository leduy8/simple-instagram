from sqlalchemy import Column
from sqlalchemy.types import Boolean, String

from src.models import BaseModel


class Post(BaseModel):
    __tablename__ = "posts"

    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    published = Column(Boolean, nullable=False)

    def __str__(self) -> str:
        return f"<Post {self.id}>"
