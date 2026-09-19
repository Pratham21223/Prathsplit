from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.user import UserCreate
from database import get_db
import services.user as user_service

# APIRouter groups related endpoints; prefix applies to all routes below
router = APIRouter(prefix="/users", tags=["Users"])


# Depends(get_db) automatically injects an open DB session into every route
@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


# {user_id} is a path parameter — FastAPI extracts it from the URL automatically
@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user(db, user_id)


@router.put("/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, user)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.delete_user(db, user_id)
