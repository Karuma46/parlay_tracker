from sqlalchemy.orm import Session
from . import models, schemas
import hashlib
from typing import Union

def get_user(db:Session, userId: int):
  return db.query(models.User).filter(models.User.id == userId).first()

def get_users(db: Session,):
  return db.query(models.User).all()

def get_user_by_id(db: Session, user_id: Union[str, int]):
  return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
  db_user = models.User(**user.model_dump())
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

def update_password(db: Session, userId: int, password: schemas.UserUpdatePassword):
  db_user = db.query(models.User).filter(models.User.id == userId).first()
  db_user.password = hashlib.sha256(password.password.encode('utf-8')).hexdigest()
  db.commit()
  db.refresh(db_user)
  return db_user

def user_login(db: Session, user: schemas.UserLogin):
  db_user = db.query(models.User).filter(models.User.username == user.username).first()
  if not db_user:
    return 'User not found'
  else:
    if db_user.password == hashlib.sha256(user.password.encode('utf-8')).hexdigest():
      db_user_token = models.UserToken(user_id=db_user.id)
      db.add(db_user_token)
      db.commit()
      db.refresh(db_user_token)
      return db_user_token
    return 'Wrong Password'

def user_logout(db: Session, token: str):
  db_user_token = db.query(models.UserToken).filter(models.UserToken.token == token).first()
  db.delete(db_user_token)
  db.commit()
  return True