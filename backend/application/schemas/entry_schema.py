from pydantic import BaseModel
from datetime import datetime

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
