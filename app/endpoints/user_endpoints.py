from sqlalchemy.orm import Session

from models.user import User
from schemas.user_schema import UserCreate, UserLogin

import models.balance as balance

def get_user(db:Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db:Session, email:str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notactuallyhashed"
    db_user = User(email=user.email, hashed_pword=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db_balance = balance.Balance(balance=100, owner_id=db_user.id)
    db.add(db_balance)
    db.commit()
    db.refresh(db_balance)

    return db_user

def login(db: Session, login: UserLogin):
    fake_hashed_password = login.password + "notactuallyhashed"
    return db.query(User).filter(User.email == login.email, User.hashed_pword == fake_hashed_password).first()