from sqlalchemy.orm.session import Session

from src.models.posts import Post
from src.schemas.posts import PostRequest


def create_post(db: Session, data: PostRequest):
    post = Post(title=data.title, published=data.published)

    if "content" in data:
        post.content = data.content

    db.add(post)
    db.commit()
    db.refresh(post)

    return post
