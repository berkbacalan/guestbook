from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int = None
    name: str
    created_date: datetime = datetime.now()
