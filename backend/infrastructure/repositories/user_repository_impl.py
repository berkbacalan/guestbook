from sqlalchemy.orm import Session
from typing import List
from domain.models.user import User
from domain.interfaces.user_repository import IUserRepository
from ..database.models.user_model import UserModel

class UserRepository(IUserRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add(self, user: User) -> User:
        db_user = UserModel(name=user.name)
        self.db_session.add(db_user)
        self.db_session.commit()
        self.db_session.refresh(db_user)
        user.id = db_user.id
        return user

    def find_by_id(self, user_id: int) -> User:
        db_user = self.db_session.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            return User(id=db_user.id, name=db_user.name, created_date=db_user.created_date)
        return None

    def find_by_name(self, name: str) -> User:
        db_user = self.db_session.query(UserModel).filter(UserModel.name == name).first()
        if db_user:
            return User(id=db_user.id, name=db_user.name, created_date=db_user.created_date)
        return None

    def list_users(self) -> List[User]:
        db_users = self.db_session.query(UserModel).all()
        return [User(id=user.id, name=user.name, created_date=user.created_date) for user in db_users]