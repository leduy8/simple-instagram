from sqlalchemy.orm.session import Session

from src.models.images import Avatar
from src.schemas.images import AvatarRequest


def create_image(db: Session, data: AvatarRequest, user_id: int):
    avatar = Avatar(url=data.url, user_id=user_id)

    db.add(avatar)
    db.commit()
    db.refresh(avatar)

    return avatar
