from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv('.env')
DB_URL = os.environ.get("DATABASE_URL")
DB_NAME = os.environ.get("DATABASE_NAME")
DB_USER = os.environ.get("DATABASE_USER")
DB_PWORD = os.environ.get("DATABASE_PWORD")

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/bamboobank"
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PWORD}@{DB_URL}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 