from abc import ABC, abstractmethod
from typing import List
from ..models.user import User

class IUserRepository(ABC):
    
    @abstractmethod
    def add(self, user: User) -> User:
        pass
    
    @abstractmethod
    def find_by_id(self, user_id: int) -> User:
        pass
    
    @abstractmethod
    def find_by_name(self, name: str) -> User:
        pass
    
    @abstractmethod
    def list_users(self) -> List[User]:
        pass
