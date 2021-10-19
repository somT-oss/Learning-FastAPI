import hashlib
from sqlalchemy.ext import declarative
from sqlalchemy.orm import Session
from . import model, schema


# Gets the user from the database with the users unique id passed as a parameter
def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()

# Gets the user from the database with the users unique email passed as a parameter
def get_user_by_email(db: Session, user_email: str):
    return db.query(model.User).filter(model.User.email == user_email).first()

# Returns all the users in the db with a limit to only 100 users without skipping any user
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()


# Creates a user by passing in the user email and hashed password to the user model attributes 
def create_user(db: Session, user: schema.UserCreate):
    user_password = user.password
    encoded_password = hashlib.md5(user_password.encode())
    hashed_password = encoded_password.hexdigest()

    db_user = model.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user