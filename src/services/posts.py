from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from src.models.posts import Post
from src.schemas import Pagination
from src.schemas.posts import PostRequest


def create_post(db: Session, data: PostRequest):
    post = Post(title=data.title, published=data.published)

    if "content" in data:
        post.content = data.content

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


def get_posts(db: Session, data: Pagination):
    query = db.query(Post).offset(data.page).limit(data.page_size)

    return {"items": query.all(), "total": query.count()}


def get_post_by_id(db: Session, id: int):
    post = db.query(Post).filter_by(id=id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found"
        )

    return post


def update_post(db: Session, id: int, data: PostRequest):
    post = db.query(Post).filter_by(id=id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found"
        )

    post.title = data.title
    post.published = data.published

    if data.content:
        post.content = data.content

    db.commit()

    return post


def delete_post(db: Session, id: int):
    post = db.query(Post).filter_by(id=id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found"
        )

    db.delete(post)
    db.commit()

    return {"message": f"Post with id {id} has been deleted"}
