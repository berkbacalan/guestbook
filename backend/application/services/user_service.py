from typing import List
from domain.models.user import User
from domain.interfaces.user_repository import IUserRepository
from ..schemas.user_schema import UserCreateSchema, UserSchema

class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_data: UserCreateSchema) -> UserSchema:
        user = User(name=user_data.name)
        created_user = await self.user_repository.add(user)
        return UserSchema(id=created_user.id, name=created_user.name, createdate= created_user.created_date)

    def get_user_by_id(self, user_id: int) -> UserSchema:
        user = self.user_repository.find_by_id(user)
        return UserSchema.model_validate(user)

    def list_users(self) -> List[UserSchema]:
        users = self.user_repository.list_users()
        return [UserSchema.model_validate(user) for user in users]
