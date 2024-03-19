from pydantic import BaseModel
from datetime import datetime

class UserCreateSchema(BaseModel):
    name: str

class UserSchema(BaseModel):
    id: int
    name: str
    createdate: datetime
    
    class Config:
        orm_mode = True
