from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
import secrets

from ..database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True)
  email = Column(String, unique=True, index=True)
  firstname = Column(String, index=True)
  lastname = Column(String, index=True)
  password = Column(String, nullable=True)
  is_active = Column(Boolean, default=True)
  tokens = relationship("UserToken", back_populates="user")

  def __repr__(self):
    return f"<User {self.username}>"

  def __str__(self):
    return self.username

class UserToken(Base):
  __tablename__ = "user_tokens"

  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"))
  token = Column(String, default=secrets.token_hex(32))
  created_at = Column(DateTime, default=datetime.now())
  expiration = Column(DateTime, default=datetime.now() + timedelta(days=30))
  user = relationship("User", back_populates="tokens")