from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import schemas
from app.database import SessionLocal, engine
from app.crud import get_tasks, get_task, get_user_tasks, create_user, create_task, update_task, delete_task, \
    get_tasks_by_category, get_user
from schemas import UserCreate, TaskCreate, User, Task
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.auth import auth  

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()

origins = [
    "http://localhost",
    # "https://your-netlify-app.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# login endpoint


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.username}
    )
    # Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}


# user create

@app.post("/users/", response_model=User)
def create_user_api(user: UserCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return create_user(db, user)


@app.get("/users/me", response_model=schemas.User)
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    return current_user


# GET endpoints

@app.get("/tasks/", response_model=list[Task])  # return all tasks
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return get_tasks(db, skip=skip, limit=limit)


@app.get("/tasks/{task_id}", response_model=Task)  # return specific task
def read_task(task_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    task = get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.get("/tasks/user/{user_id}", response_model=list[schemas.Task])  # return all tasks for specific user
def read_user_tasks(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db),
                    token: str = Depends(oauth2_scheme)):
    return get_user_tasks(db, user_id, skip=skip, limit=limit)


@app.get("/tasks/category/{category}", response_model=list[Task])
def read_tasks_by_category(category: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return get_tasks_by_category(db, category)


# POST endpoint


@app.post("/tasks/", response_model=Task)
def create_task_api(task: TaskCreate, user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return create_task(db, task, user_id)


# PUT endpoint


@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task_api(task_id: int, task: TaskCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return update_task(db, task_id, task)


# DELETE endpoint


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task_api(task_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    deleted_task = delete_task(db, task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task

