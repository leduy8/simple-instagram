from fastapi import APIRouter, Body, Depends, Path
from sqlalchemy.orm.session import Session

from src.database import get_db
from src.schemas import Pagination
from src.schemas.posts import PostManyResponse, PostRequest, PostResponse
from src.services import posts as posts_service

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=PostResponse)
def create_post(data: PostRequest, db: Session = Depends(get_db)):
    return posts_service.create_post(db, data)


@router.get("/", response_model=PostManyResponse)
def get_posts(data: Pagination = Depends(Pagination), db: Session = Depends(get_db)):
    return posts_service.get_posts(db, data)


@router.get("/{id}", response_model=PostResponse)
def get_post_by_id(id: int = Path(...), db: Session = Depends(get_db)):
    return posts_service.get_post_by_id(db, id)


@router.put("/{id}", response_model=PostResponse)
def update_post(
    id: int = Path(...), data: PostRequest = Body(...), db: Session = Depends(get_db)
):
    return posts_service.update_post(db, id, data)


@router.delete("/{id}")
def delete_post(id: int = Path(...), db: Session = Depends(get_db)):
    return posts_service.delete_post(db, id)
