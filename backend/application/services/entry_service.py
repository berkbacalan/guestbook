from typing import List
from backend.domain.models.user import User
from domain.models.entry import Entry
from domain.interfaces.entry_repository import IEntryRepository
from domain.interfaces.user_repository import IUserRepository
from ..schemas.entry_schema import EntryCreateSchema, EntrySchema

class EntryService:
    def __init__(self, entry_repository: IEntryRepository, user_repository: IUserRepository):
        self.entry_repository = entry_repository
        self.user_repository = user_repository

    def create_entry(self, entry_data: EntryCreateSchema) -> EntrySchema:
        user = self.user_repository.find_by_name(entry_data.username)
        if not user:
            user = self.user_repository.add(User(name=entry_data.username))
        entry = Entry(subject=entry_data.subject, message=entry_data.message, user=user)
        created_entry = self.entry_repository.add(entry)
        return EntrySchema.model_validate(created_entry)

    def list_entries(self, limit: int = 10, offset: int = 0) -> List[EntrySchema]:
        entries = self.entry_repository.list_entries(limit, offset)
        return [EntrySchema.model_validate(entry) for entry in entries]