from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from ..database import Base
from datetime import datetime
from sqlalchemy.orm import relationship
from ..teams.models import Team

class Parlay(Base):
  __tablename__ = "parlays"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  description = Column(String)
  outcome = Column(Integer)
  spread = Column(Integer)

class ParlayTeam(Base):
  __tablename__ = "parlay_teams"

  id = Column(Integer, primary_key=True, index=True)
  parlay_id = Column(Integer, ForeignKey("parlays.id"))
  team_id = Column(Integer, ForeignKey("teams.id"))

  events = relationship("ParlayEvent", back_populates="parlay_team")


class ParlayWeek(Base):
  __tablename__ = "parlay_weeks"

  id = Column(Integer, primary_key=True, index=True)
  parlay_id = Column(Integer, ForeignKey("parlays.id"))
  week = Column(Integer)

class ParlayEvent(Base):
  __tablename__ = "parlay_events"

  id = Column(Integer, primary_key=True, index=True)
  parlay_team_id = Column(Integer, ForeignKey("parlay_teams.id"))
  parlay_week_id = Column(Integer, ForeignKey("parlay_weeks.id"))
  date = Column(DateTime, default=datetime.now())
  is_home_team = Column(Boolean, nullable=False)
  rival_team = Column(String, nullable=False)
  odds = Column(Integer, nullable=False)
  spread = Column(Integer, nullable=False)
  final_score = Column(String, nullable=True)
  outcome = Column(Integer, nullable=True)
  parlay_team = relationship("ParlayTeam", back_populates="events")