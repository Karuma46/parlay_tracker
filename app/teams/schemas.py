from pydantic import BaseModel

class Sport(BaseModel):
  id: int
  name: str
  is_active: bool

  class Config:
    from_attributes = True

class SportCreate(BaseModel):
  name: str

class League(BaseModel):
  id: int
  name: str
  sport_id: int
  is_active: bool

  class Config:
    from_attributes = True

class LeagueCreate(BaseModel):
  name: str
  sport_id: int

class Team(BaseModel):
  id: int
  name: str
  is_active: bool
  league_id: int

  class Config:
    from_attributes = True

class TeamCreate(BaseModel):
  name: str
  league_id: int