from typing import List, Optional

from sqlalchemy.orm import Session

from domain.interfaces.entry_repository import IEntryRepository
from domain.models.entry import Entry
from domain.models.user import User
from infrastructure.database.models.entry_model import EntryModel


class EntryRepository(IEntryRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add(self, entry: Entry) -> Entry:
        db_entry = EntryModel(subject=entry.subject, message=entry.message, created_date=entry.created_date,
                              user_id=entry.user.id)
        self.db_session.add(db_entry)
        self.db_session.commit()
        self.db_session.refresh(db_entry)
        return Entry(id=db_entry.id, subject=db_entry.subject, message=db_entry.message,
                     created_date=db_entry.created_date, user=db_entry.user)

    def find_by_id(self, entry_id: int) -> Optional[Entry]:
        db_entry = self.db_session.query(EntryModel).filter(EntryModel.id == entry_id).first()
        if db_entry is not None:
            return Entry(id=db_entry.id, subject=db_entry.subject, message=db_entry.message,
                         created_date=db_entry.created_date, user=User(user_id=db_entry.user.id, name=db_entry.user.name,
                                                                       created_date=db_entry.user.created_date))
        return None

    def list_entries(self, limit: int = 10, offset: int = 0) -> List[Entry]:
        db_entries = self.db_session.query(EntryModel).order_by(EntryModel.created_date.desc()).offset(offset).limit(
            limit).all()
        return [Entry(id=e.id, subject=e.subject, message=e.message, created_date=e.created_date,
                      user=User(user_id=e.user.id, name=e.user.name, created_date=e.user.created_date)) for e in db_entries]

    def list_entries_by_user_id(self, user_id: int, limit: int = 10, offset: int = 0) -> List[Entry]:
        db_entries = self.db_session.query(EntryModel).filter(EntryModel.user_id == user_id).order_by(
            EntryModel.created_date.desc()).offset(offset).limit(limit).all()
        return [Entry(id=e.id, subject=e.subject, message=e.message, created_date=e.created_date,
                      user=User(user_id=e.user.id, name=e.user.name, created_date=e.user.created_date)) for e in db_entries]

    def get_entry_count(self) -> int:
        return self.db_session.query(EntryModel).count()