from typing import List, Union

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from endpoints import balance_endpoints, transaction_endpoints, user_endpoints
from models import balance, transaction, user
from schemas import balance_schema, transaction_schema, user_schema

from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
#     "http://localhost:8000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Initialise DB middleware
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal Server Error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

def get_db(request: Request):
    return request.state.db


# Debug
@app.get("/")
def read_root():
    return {"Hello": "World"}

# User
@app.post("/users/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db:Session = Depends(get_db)):
    db_user = user_endpoints.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Already Registered!")
    return user_endpoints.create_user(db=db, user=user)

@app.get("/users/", response_model=user_schema.User)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_user = user_endpoints.get_users(db, skip, limit)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/{user_id}", response_model=user_schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_endpoints.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/search", response_model=user_schema.User)
def search_user(user_email: user_schema.UserBase, db: Session = Depends(get_db)):
    db_user = user_endpoints.get_user_by_email(db, email=user_email.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/login", response_model=user_schema.User)
def login(login: user_schema.UserLogin, db: Session = Depends(get_db)):
    db_user = user_endpoints.login(db, login=login)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Balance
@app.post("/users/{user_id}/balance/", response_model=balance_schema.Balance)
def read_balance(
    user_id: int, db: Session = Depends(get_db)
):
    return balance_endpoints.get_balance(db=db, user_id=user_id)

# Transactions
@app.post("/users/{user_id}/transactions/new", response_model=transaction_schema.Transaction)
def make_transaction(
    user_id: int, account_id: int, amount: int, db: Session = Depends(get_db)
):
    return transaction_endpoints.make_transaction(db=db, user_id=user_id, account_id=account_id, amount=amount)

@app.post("/users/{user_id}/transactions/record", response_model=transaction_schema.Transaction)
def record_transaction(
    user_id: int, transaction: transaction_schema.TransactionCreate, db: Session = Depends(get_db)
):
    return transaction_endpoints.record_transaction(db=db, transaction=transaction, user_id=user_id)

@app.post("/users/{user_id}/transactions/", response_model=List[transaction_schema.Transaction])
def read_transactions(
    user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return transaction_endpoints.get_transactions(db=db, user_id=user_id)