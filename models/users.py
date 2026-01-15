from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from config.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)