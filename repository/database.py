from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# file with database configuration
DATABASE_URL= "sqlite:///./chinook.db"

engine = create_engine(DATABASE_URL)
# bind base model with engine 
Base = declarative_base(engine)

metadata = Base.metadata

LocalSession = sessionmaker(bind=engine)

# return database session and close it after use 
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()