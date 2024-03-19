from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    def __init__(self, name: str, id: int = None):
        self.id = id
        self.name = name

    id: int
    name: str
    created_date: datetime = datetime.now()
