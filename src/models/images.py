from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Text

from src.models.base import SimpleBaseModel


class ImageBase(SimpleBaseModel):
    __abstract__ = True

    url = Column(Text)


class Avatar(ImageBase):
    __tablename__ = "avatars"

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="avatar")

    def __str__(self) -> str:
        return f"<Avatar {self.id}>"


class PostImage(ImageBase):
    __tablename__ = "postimages"

    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="images")

    def __str__(self) -> str:
        return f"<PostImage {self.id}>"
