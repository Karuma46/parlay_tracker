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
    from_attributes = True

class UserUpdatePassword(BaseModel):
  id: int
  password: str

class UserLogin(BaseModel):
  username: str
  password: str

class UserToken(BaseModel):
  user_id: int
  token: str