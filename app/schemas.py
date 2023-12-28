from datetime import date
from typing import List, Optional
from pydantic import BaseModel

# USER schemas

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# TASK schemas

class TaskBase(BaseModel):
    title: str
    description: str
    due_date: Optional[date] = None
    category: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    owner: Optional[UserBase]
    is_complete: bool

    class Config:
        orm_mode = True
