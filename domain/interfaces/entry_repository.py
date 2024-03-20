from abc import ABC, abstractmethod
from typing import List
from ..models.entry import Entry


class IEntryRepository(ABC):

    @abstractmethod
    def add(self, entry: Entry) -> Entry:
        pass

    @abstractmethod
    def find_by_id(self, entry_id: int) -> Entry:
        pass

    @abstractmethod
    def list_entries(self, limit: int = 10, offset: int = 0) -> List[Entry]:
        pass

    @abstractmethod
    def list_entries_by_user_id(self, user_id: int, limit: int = 10, offset: int = 0) -> List[Entry]:
        pass

    @abstractmethod
    def get_entry_count(self) -> int:
        pass
