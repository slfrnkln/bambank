from typing import List, Union
from pydantic import BaseModel

class TransactionBase(BaseModel):
    amount: int

class TransactionCreate(TransactionBase):
    account_id: int

class Transaction(TransactionBase):
    id: int
    account_id: int
    owner_id = int

    class Config:
        orm_mode = True
