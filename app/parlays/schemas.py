from pydantic import BaseModel

class Parlay(BaseModel):
  name: str
  description: str
  outcome: int
  spread: int

  class Config:
    from_attributes = True


class ParlayTeam(BaseModel):
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