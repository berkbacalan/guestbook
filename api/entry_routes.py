from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from infrastructure.database.base import SessionLocal
from application.services.entry_service import EntryService
from application.schemas.entry_schema import EntryCreateSchema, EntrySchema, EntryListPagination
from infrastructure.repositories.user_repository_impl import UserRepository
from infrastructure.repositories.entry_repository_impl import EntryRepository

entry_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@entry_router.post("/", response_model=EntrySchema)
async def create_entry(entry: EntryCreateSchema, db: Session = Depends(get_db)):
    entry_service = EntryService(EntryRepository(db), UserRepository(db))
    return await entry_service.create_entry(entry)


@entry_router.get("/", response_model=EntryListPagination)
def list_entries(page: int = 1, page_size: int = 3, db: Session = Depends(get_db)):
    entry_service = EntryService(EntryRepository(db), UserRepository(db))
    return entry_service.list_entries(page_size, page)
