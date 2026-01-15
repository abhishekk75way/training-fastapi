from sqlalchemy import Column, Integer, String, Boolean
from config.db import Base


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    completed = Column(Boolean, nullable=False)