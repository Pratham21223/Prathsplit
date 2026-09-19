# SQLAlchemy is the ORM (Object Relational Mapper) we use to interact with the database.
# Instead of writing raw SQL, we write Python classes and SQLAlchemy translates them to SQL.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# declarative_base() gives us a base class that all our models (tables) will inherit from.
# SQLAlchemy uses it to track which classes represent database tables.
from sqlalchemy.orm import declarative_base

# The DATABASE_URL tells SQLAlchemy HOW and WHERE to connect to the database.
# Format: "dialect+driver://username:password@host:port/database_name"
DATABASE_URL = "postgresql://postgres:30042007@localhost:5433/prathsplit"

# The engine is the core connection to the database.
# Think of it as the "phone line" between your Python app and PostgreSQL.
engine = create_engine(DATABASE_URL)

# SessionLocal is a factory that creates database sessions.
# A session is like a "conversation" with the database — you open it, do work, then close it.
# autocommit=False  → changes are NOT saved automatically; you must call db.commit()
# autoflush=False   → SQLAlchemy won't auto-sync changes to the DB before every query
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base is the parent class for all our SQLAlchemy models (User, Expense, etc.)
# When a class inherits from Base, SQLAlchemy registers it as a database table.
Base = declarative_base()


# get_db is a FastAPI "dependency" — a function that runs before your route handler
# and provides it with something (in this case, a database session).
#
# The `yield` keyword makes this a generator:
#   1. Code BEFORE yield runs first → opens the DB session
#   2. The session is injected into your route via `Depends(get_db)`
#   3. Code AFTER yield (the finally block) runs after your route finishes → closes the session
#
# This guarantees the session is ALWAYS closed, even if an error occurs.
def get_db():
    db = SessionLocal()
    try:
        yield db        # <-- hands the session to the route handler
    finally:
        db.close()      # <-- always runs, ensures no connection leak