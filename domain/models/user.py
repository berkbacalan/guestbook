from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    def __init__(self, name: str, created_date: datetime = None, user_id: int = None):
        self.id = user_id
        self.name = name
        if created_date is not None:
            self.created_date = created_date

    id: int
    name: str
    created_date: datetime = datetime.now()
