from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base

# Each class = one table in the database
class User(Base):
    __tablename__ = "users"   # actual table name in PostgreSQL

    # primary_key=True makes this the unique row identifier; index speeds up lookups
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
