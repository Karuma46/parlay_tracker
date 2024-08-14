from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

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

  def __repr__(self):
    return f"<User {self.username}>"

  def __str__(self):
    return self.username