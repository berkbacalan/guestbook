from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .entry_model import EntryModel
from ..base import Base
from datetime import datetime


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    created_date = Column(DateTime, default=datetime.now)


UserModel.entries = relationship("EntryModel", order_by=EntryModel.id, back_populates="user")
