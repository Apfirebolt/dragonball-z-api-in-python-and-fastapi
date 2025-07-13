from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv
load_dotenv()

# DATABASE_USERNAME = os.getenv("DATABASE_USER")
# DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
# DATABASE_HOST = os.getenv("DATABASE_HOST")
# DATABASE_NAME = os.getenv("DATABASE_NAME")

DATABASE_USER='postgres'
DATABASE_PASSWORD='pass123'
DATABASE_HOST='localhost'
# DATABASE_HOST='db'
DATABASE_NAME='dbz-api'

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
