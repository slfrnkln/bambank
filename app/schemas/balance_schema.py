from typing import List, Union
from pydantic import BaseModel

class BalanceBase(BaseModel):
    balance: int

class BalanceCreate(BalanceBase):
    pass

class Balance(BalanceBase):
    id: int
    owner_id = int

    class Config:
        orm_mode = True
