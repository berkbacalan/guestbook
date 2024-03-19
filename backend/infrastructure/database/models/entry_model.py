from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base
from datetime import datetime

class EntryModel(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, index=True)
    message = Column(String, index=True)
    created_date = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("UserModel", back_populates="entries")
