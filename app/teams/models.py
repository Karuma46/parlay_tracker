from ..database import Base
from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship

class Sport(Base):
  __tablename__ = "sports"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  is_active = Column(Boolean, default=True)
  leagues = relationship("League", back_populates="sport")

class League(Base):
  __tablename__ = "leagues"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  sport_id = Column(Integer, ForeignKey("sports.id"))
  is_active = Column(Boolean, default=True)
  sport = relationship("Sport", back_populates="leagues")
  teams = relationship("Team", back_populates="league")


class Team(Base):
  __tablename__ = "teams"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  league_id = Column(Integer, ForeignKey("leagues.id"))
  is_active = Column(Boolean, default=True)
  league = relationship("League", back_populates="teams")



