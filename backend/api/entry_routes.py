from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from infrastructure.database.base import SessionLocal
from application.services.entry_service import EntryService
from application.schemas.entry_schema import EntryCreateSchema, EntrySchema
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
def create_entry(entry: EntryCreateSchema, db: Session = Depends(get_db)):
    entry_service = EntryService(EntryRepository(db), UserRepository(db))
    return entry_service.create_entry(entry)

@entry_router.get("/", response_model=List[EntrySchema])
def list_entries(db: Session = Depends(get_db)):
    entry_service = EntryService(EntryRepository(db), UserRepository(db))
    return entry_service.list_entries()
