from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from sqlalchemy.orm.session import Session

from src.database import get_db
from src.schemas.users import UserRequest, UserResponse
from src.services import users as users_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
def create_user(db: Session = Depends(get_db), data: UserRequest = Body(...)):
    try:
        user = users_service.create_user(db, data)

        if not user:
            raise Exception("User creation failed")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return Response("User created")
