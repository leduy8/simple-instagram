from sqlalchemy.orm.session import Session

from src.models.users import User
from src.schemas.users import UserRequest
from src.services.images import create_image
from src.utils.password import (check_password_hash, gen_salt,
                                generate_password_hash)


def create_user(db: Session, data: UserRequest):
    salt = gen_salt()

    user = User(
        email=data.email,
        password_salt=salt,
        password_hash=generate_password_hash(password=data.password, salt=salt),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def upload_user_avatar(db: Session, data):
    pass
