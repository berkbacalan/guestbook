from dataclasses import dataclass
from datetime import datetime
from .user import User


@dataclass
class Entry:
    id: int = None
    subject: str
    message: str
    created_date: datetime = datetime.now()
    user: User
