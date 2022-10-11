from sqlalchemy.orm import Session

from models.transaction import Transaction
from schemas.transaction_schema import TransactionCreate

from . import balance_endpoints as Balance

def get_transactions(db:Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Transaction).filter(Transaction.owner_id == user_id).offset(skip).limit(limit).all()

def record_transaction(db:Session, transaction: TransactionCreate, user_id: int):
    db_transaction = Transaction(**transaction.dict(), owner_id=user_id)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def make_transaction(db:Session, user_id: int, account_id: int, amount: int):
    Balance.withdraw(db, user_id, amount)
    Balance.deposit(db, account_id, amount)
    db_transaction = Transaction(amount=(-amount), account_id=account_id, owner_id=user_id)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    db_transaction_reflect = Transaction(amount=amount, account_id=user_id, owner_id=account_id)
    db.add(db_transaction_reflect)
    db.commit()
    db.refresh(db_transaction_reflect)
    return db_transaction