from pydantic import BaseModel
from datetime import datetime

from typing import List


class EntryCreateSchema(BaseModel):
    username: str
    subject: str
    message: str


class EntrySchema(BaseModel):
    id: int
    subject: str
    message: str
    created_date: datetime
    user_id: int
    username: str

    class Config:
        orm_mode = True


class EntryListPagination(BaseModel):
    count: int
    page_size: int
    total_pages: int
    current_page_number: int
    entries: List[EntrySchema]

    class Config:
        orm_mode = True
