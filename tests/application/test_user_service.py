import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from application.services.user_service import UserService
from application.schemas.user_schema import UserCreateSchema
from domain.interfaces.entry_repository import IEntryRepository
from domain.interfaces.user_repository import IUserRepository
from domain.models.entry import Entry
from domain.models.user import User

from typing import List

class MockEntryRepository(IEntryRepository):
    async def add(self, entry: Entry) -> Entry:
        return Entry(id=1, subject=entry.subject, message=entry.message, user=entry.user)

class MockUserRepository(IUserRepository):
    def __init__(self):
        self.users = []
        self.next_id = 1

    async def add(self, user: User) -> User:
        user.id = self.next_id
        self.next_id += 1
        self.users.append(user)
        return user
    
    async def find_by_id(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    async def find_by_name(self, name: str) -> User:
        for user in self.users:
            if user.name == name:
                return user
        return None
    
    async def list_users(self) -> List[User]:
        return self.users

@pytest.mark.asyncio
async def test_create_entry():
    user_repository = MockUserRepository()
    
    user_service = UserService(user_repository)
    
    user_data = UserCreateSchema(name="Test User")
    
    user = await user_service.create_user(user_data)
    
    assert user.id is not None
    assert user.name == "Test User"
