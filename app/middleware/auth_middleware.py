from fastapi import Depends
from ..users.models import User, UserToken
from datetime import datetime
from sqlalchemy.orm import Session
from ..database import SessionLocal


async def authorize(headers: list, db:Session = SessionLocal()):
  if headers.get('Authorization'):
    token = headers['Authorization']
    db_user_token = db.query(UserToken).filter(UserToken.token == token).first()
    print(db_user_token)
    if db_user_token:
      return db_user_token.expiration > datetime.now()
    return False
  return False