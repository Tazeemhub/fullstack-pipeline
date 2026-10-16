import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declaration_base

load_dotenv()

DATABASE_URL= os.getenv("DATABASE_URL","postgresql://postgres:postgres@localhost:5432/fspipelinedb")

connect_args={"check_same_thread":False} if DATABASE_URL.startswith("postgresql") else {}

engine= create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit+False, autoflush=False, bing=engine)
Base = declarative_base()

def get_db():
    """Dependency generator yielding a safe DB session per HTTP request. """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    