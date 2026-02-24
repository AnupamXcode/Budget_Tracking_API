from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///./budget_tracking.db'  # Change this to your database URL

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Declarative base
Base = declarative_base()

# SessionLocal class for session management
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()