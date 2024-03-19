from dataclasses import dataclass
from datetime import datetime
from .user import User


@dataclass
class Entry:
    def __init__(self, subject: str, message: str, user: User, id: int = None):
        self.id = id
        self.subject = subject
        self.message = message
        self.user = user

    id: int
    subject: str
    message: str
    user: User
    created_date: datetime = datetime.now()
