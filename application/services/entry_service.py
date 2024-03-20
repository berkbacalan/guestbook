from typing import List
import math
from domain.models.user import User
from domain.models.entry import Entry
from domain.interfaces.entry_repository import IEntryRepository
from domain.interfaces.user_repository import IUserRepository
from ..schemas.entry_schema import EntryCreateSchema, EntrySchema, EntryListPagination


class EntryService:
    def __init__(self, entry_repository: IEntryRepository, user_repository: IUserRepository):
        self.entry_repository = entry_repository
        self.user_repository = user_repository

    async def create_entry(self, entry_data: EntryCreateSchema) -> EntrySchema:
        user = self.user_repository.find_by_name(entry_data.username)
        if user is None:
            user = self.user_repository.add(User(name=entry_data.username))

        entry = Entry(subject=entry_data.subject, message=entry_data.message, created_date=None, user=user)
        created_entry = self.entry_repository.add(entry)
        return EntrySchema(id=created_entry.id, subject=created_entry.subject, message=created_entry.message,
                           created_date=created_entry.created_date, user_id=created_entry.user.id,
                           username=created_entry.user.name)

    def list_entries(self, limit: int = 10, offset: int = 0) -> List[EntrySchema]:
        entries = self.entry_repository.list_entries(limit, offset)
        entry_count = self.entry_repository.get_entry_count()
        entry_list = [EntrySchema(id=entry.id, subject=entry.subject, message=entry.message, created_date=entry.created_date, user_id=entry.user.id, username=entry.user.name) for entry in entries]
        entry_list_response = EntryListPagination(count=entry_count, page_size=limit, total_pages=math.ceil(entry_count/limit), current_page_number=offset, entries=entry_list)
        return entry_list_response
