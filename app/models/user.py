from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_pword = Column(String)
    is_active = Column(Boolean, default = True)

    balance = relationship("Balance")
    transactions = relationship("Transaction", back_populates="owner")