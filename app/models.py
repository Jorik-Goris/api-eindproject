# models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    hashed_password = Column(String)

    tasks = relationship("Task", back_populates="owner", lazy="dynamic")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    is_complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    due_date = Column(Date, nullable=True)
    category = Column(String, nullable=True)

    owner = relationship("User", back_populates="tasks")
