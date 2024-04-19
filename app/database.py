from sqlmodel import SQLModel, create_engine, Session

# Replace with actual database if used in production
DATABASE_URL = "sqlite:///./data/api.db"

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
