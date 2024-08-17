from pydantic import BaseModel

class Option(BaseModel):
  name: str
  description: str
  option: int

  class Config:
    from_attributes = True

class Parlay(BaseModel):
  name: str
  description: str
  type: int

  class Config:
    from_attributes = True

class ParlayType(BaseModel):
  name: str
  outcome: int
  spread: int

  class Config:
    from_attributes = True

class ParlayTypeOption(BaseModel):
  name: str
  parlay_type_id: int

  class Config:
    from_attributes = True


class ParlayTeam(BaseModel):
  id: int
  parlay_id: int
  team_id: int

  class Config:
    from_attributes = True


class ParlayWeek(BaseModel):
  id: int
  parlay_id: int
  week: int

  class Config:
    from_attributes = True

class ParlayEvent(BaseModel):
  id: int
  parlay_team_id: int
  parlay_week_id: int
  date: str
  is_home_team: bool
  rival_team: str
  odds: int
  spread: int
  final_score: str
  outcome: int

  class Config:
    from_attributes = True