from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import model, schema, crud 
from .database import SessionLocal, engine 

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/create/", response_model=schema.UserCreate)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email=user.email)
    if db_user:
        return HTTPException(status_code=400, detail="This email has a;ready been registered")
    else:
        return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schema.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users 

@app.get("/users/{user_id}", response_model=schema.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        return HTTPException(status_code=400, detail="User not found")
    else:
        return db_user 

@app.post("/blog/create/{user_id}/", response_model=schema.Blog)
def create_blog(user_id: int, blog: schema.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(user_id=user_id, blog=blog, db=db)

@app.get("/blogs/", response_model=List[schema.Blog])
def get_blogs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db=db, skip=skip, limit=limit)
    return blogs 

    



