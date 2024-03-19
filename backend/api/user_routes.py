from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from infrastructure.database.base import SessionLocal
from application.services.user_service import UserService
from application.schemas.user_schema import UserSchema
from infrastructure.repositories.user_repository_impl import UserRepository

user_router = APIRouter()

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

@user_router.get("/", response_model=List[UserSchema])
def list_users(db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return user_service.list_users
