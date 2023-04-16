from pydantic import BaseModel, Field


class ImageBase(BaseModel):
    url: str


class AvatarBase(ImageBase):
    pass


class AvatarRequest(AvatarBase):
    pass


class AvatarResponse(AvatarBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
