from fastapi import Depends, Request, Response
from ..users.models import User, UserToken
from datetime import datetime
from sqlalchemy.orm import Session
from ..database import SessionLocal
from starlette.middleware.base import BaseHTTPMiddleware

excluded_urls = [
  '/users/login/',
  '/users/add',
  '/users/update_password'
]

class AuthMiddleware(BaseHTTPMiddleware):
  async def authorize(self, headers: list, db:Session = SessionLocal()):
    if headers.get('Authorization'):
      token = headers['Authorization']
      db_user_token = db.query(UserToken).filter(UserToken.token == token).first()
      print(db_user_token)
      if db_user_token:
        return db_user_token.expiration > datetime.now()
      return False
    return False

  async def dispatch(self, request: Request, call_next):
    if request.url.path in excluded_urls:
        return await call_next(request)
    else:
      if await self.authorize(request.headers):
          response = await call_next(request)
          return response
      else:
          return Response("Unauthorized", status_code=401)
