import re
from typing import List, Optional

from pydantic import BaseModel, Field, validator

from src.schemas.images import AvatarResponse
from src.schemas.posts import PostSimpleResponse


class UserBase(BaseModel):
    email: str = Field(default="abc@mail.com")


class UserRequest(UserBase):
    password: str

    @validator("email")
    def valid_email(cls, v):
        pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if not re.match(pattern, v):
            raise ValueError("Invalid email")
        return v


class UserResponse(UserBase):
    name: Optional[str] = None
    posts: List[PostSimpleResponse] = []
    avatar: Optional[AvatarResponse] = None

    class Config:
        orm_mode = True
