from typing import List
from domain.models.user import User
from domain.interfaces.user_repository import IUserRepository
from domain.interfaces.entry_repository import IEntryRepository
from ..schemas.user_schema import UserCreateSchema, UserSchema, UserDataSchema


class UserService:
    def __init__(self, user_repository: IUserRepository, entry_repository: IEntryRepository):
        self.user_repository = user_repository
        self.entry_repository = entry_repository

    async def create_user(self, user_data: UserCreateSchema) -> UserSchema:
        user = User(name=user_data.name)
        created_user = self.user_repository.add(user)
        return UserSchema(id=created_user.id, name=created_user.name, createdate=created_user.created_date)

    def get_user_by_id(self, user_id: int) -> UserSchema:
        user = self.user_repository.find_by_id(user_id)
        return UserSchema.model_validate(user)

    def list_users(self) -> List[UserSchema]:
        users = self.user_repository.list_users()
        return [UserSchema(id=user.id, name=user.name, createdate=user.created_date) for user in users]

    def get_user_data(self) -> List[UserDataSchema]:
        users =self.user_repository.list_users()
        user_data_list = []
        for user in users:
            user_last_entry = None
            user_last_entry_list = self.entry_repository.list_entries_by_user_id(user_id=user.id, limit=1, offset=1)
            if len(user_last_entry_list) > 0:
                user_last_entry = user_last_entry_list[0]
                last_entry = f"{user_last_entry.subject} | {user_last_entry.message}"
            else:
                last_entry = ""
            user_data_list.append(UserDataSchema(username=user.name, last_entry=last_entry))
        return user_data_list
