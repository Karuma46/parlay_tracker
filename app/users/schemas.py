from pydantic import BaseModel

class UserBase(BaseModel):
  username: str
  email: str
  firstname: str
  lastname: str

class UserCreate(UserBase):
  pass

class User(UserBase):
  id: int
  is_active: bool

  class Config:
    orm_mode = True

class UserUpdatePassword(BaseModel):
  password: str

class UserLogin(BaseModel):
  username: str
  password: str