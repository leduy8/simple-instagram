from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from src.database import get_db
from src.schemas.posts import PostRequest, PostResponse
from src.services import posts as posts_service

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=PostResponse)
def create_post(data: PostRequest, db: Session = Depends(get_db)):
    return posts_service.create_post(db, data)
