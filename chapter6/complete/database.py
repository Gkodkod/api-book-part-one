"""Database configuration"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

import os
# SQLALCHEMY_DATABASE_URL = "sqlite:///./fantasy_data.db"
SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL", "postgresql://postgres:postgres@localhost:5432/fantasy_data")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()