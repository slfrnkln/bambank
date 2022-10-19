from typing import List, Union
from pydantic import BaseModel

from .balance_schema import Balance

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    balance = Balance

    class Config:
        orm_mode = True
