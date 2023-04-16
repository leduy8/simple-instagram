from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import String

from src.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    email = Column(String(254), index=True, unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    password_salt = Column(String(12), nullable=False)
    name = Column(String(50), nullable=True)
    posts = relationship("Post", back_populates="user")
    avatar = relationship("Avatar", back_populates="user", uselist=False)

    def __str__(self) -> str:
        return f"<User {self.id}>"
