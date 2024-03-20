import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from application.services.entry_service import EntryService
from domain.interfaces.entry_repository import IEntryRepository
from domain.interfaces.user_repository import IUserRepository
from domain.models.entry import Entry
from domain.models.user import User
from application.schemas.entry_schema import EntryCreateSchema

from typing import List

class MockEntryRepository(IEntryRepository):
    def __init__(self):
        self.entries = []
        self.next_id = 1

    async def add(self, entry: Entry) -> Entry:
        entry.id = self.next_id
        self.next_id += 1
        self.entries.append(entry)
        return entry

    async def find_by_id(self, entry_id: int) -> Entry:
        for entry in self.entries:
            if entry.id == entry_id:
                return entry
        return None

    async def list_entries(self, limit: int = 10, offset: int = 0) -> List[Entry]:
        return self.entries[offset: offset + limit]

    async def list_entries_by_user_id(self, user_id: int, limit: int = 10, offset: int = 0) -> List[Entry]:
        filtered_entries = [entry for entry in self.entries if entry.user.id == user_id]
        return filtered_entries[offset: offset + limit]

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
    entry_repository = MockEntryRepository()
    
    entry_service = EntryService(entry_repository=entry_repository, user_repository=user_repository)
    
    entry_data = EntryCreateSchema(username="Test User", subject="Test Subject", message="Test Message")
    
    entry = await entry_service.create_entry(entry_data=entry_data)
    
    assert entry.subject == "Test Subject"
    assert entry.message == "Test Message"
    assert entry.username == "Test User"
