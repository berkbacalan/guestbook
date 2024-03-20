from dataclasses import dataclass
from datetime import datetime
from .user import User


@dataclass
class Entry:
    def __init__(self, subject: str, message: str, user: User, created_date: datetime, id: int = None):
        self.id = id
        self.subject = subject
        self.message = message
        self.user = user
        if created_date is not None:
            self.created_date = created_date

    id: int
    subject: str
    message: str
    user: User
    created_date: datetime = datetime.now()
