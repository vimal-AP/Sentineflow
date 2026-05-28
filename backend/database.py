from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connects Python directly to our running Docker Postgres Container
DATABASE_URL = "postgresql://sentinel_user:sentinel_password@127.0.0.1:5433/sentinel_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# CRUCIAL: Make sure Base is capitalized exactly like this
Base = declarative_base()

# Dependency to get database sessions safely
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()