from requests import session
from sqlalchemy.orm import Session

from models.balance import Balance

def get_balance(db:Session, user_id: int):
    return db.query(Balance).filter(Balance.owner_id == user_id).first()

def update_balance(db:Session, user_id: int, new_balance: int):
    balance = db.query(Balance).filter(Balance.owner_id == user_id).first()
    balance.balance = new_balance
    db.add(balance)
    db.commit()
    db.refresh(balance)
    return balance

def withdraw(db:Session, user_id: int, amount: int):
    balance = db.query(Balance).filter(Balance.owner_id == user_id).first()
    balance.balance -= amount
    db.add(balance)
    db.commit()
    db.refresh(balance)
    return balance

def deposit(db:Session, user_id: int, amount: int):
    balance = db.query(Balance).filter(Balance.owner_id == user_id).first()
    balance.balance += amount
    db.add(balance)
    db.commit()
    db.refresh(balance)
    return balance
    