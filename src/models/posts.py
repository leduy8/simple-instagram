from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Boolean, Integer, String

from src.models.base import BaseModel


class Post(BaseModel):
    __tablename__ = "posts"

    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    published = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")
    images = relationship("PostImage", back_populates="post")

    def __str__(self) -> str:
        return f"<Post {self.id}>"
