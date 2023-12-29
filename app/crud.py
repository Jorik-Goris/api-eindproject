from sqlalchemy.orm import Session

import auth
from models import User, Task
from schemas import UserCreate, TaskCreate


# CREATE user
def create_user(db: Session, user: UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# CREATE task


def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# UPDATE task


def update_task(db: Session, task_id: int, task_data: TaskCreate):
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if db_task:
        for key, value in task_data.dict().items():
            setattr(db_task, key, value)

        db.commit()
        db.refresh(db_task)
        return db_task
    else:
        return None

# DELETE task


def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if db_task:
        db.delete(db_task)
        db.commit()
        return db_task
    else:
        return None


# READ
def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()


def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def get_user_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Task).filter(Task.owner_id == user_id).offset(skip).limit(limit).all()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_tasks_by_category(db: Session, category: str, skip: int = 0, limit: int = 10):
    return db.query(Task).filter(Task.category == category).offset(skip).limit(limit).all()
