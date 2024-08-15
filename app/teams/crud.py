from sqlalchemy.orm import Session
from . import models, schemas

def create_sport(db: Session, sport: schemas.SportCreate):
  db_sport = models.Sport(**sport.model_dump())
  db.add(db_sport)
  db.commit()
  db.refresh(db_sport)
  return db_sport

def get_sport_by_id(db: Session, sport_id: int):
  return db.query(models.Sport).filter(models.Sport.id == sport_id).first()

def get_sports(db: Session):
  return db.query(models.Sport).all()

def create_league(db: Session, league: schemas.LeagueCreate):
  db_league = models.League(**league.model_dump())
  db.add(db_league)
  db.commit()
  db.refresh(db_league)
  return db_league

def get_leagues(db: Session):
  return db.query(models.League).all()

def get_league_by_id(db: Session, league_id: int):
  return db.query(models.League).filter(models.League.id == league_id).first()

def create_team(db: Session, team: schemas.TeamCreate):
  db_team = models.Team(**team.model_dump())
  db.add(db_team)
  db.commit()
  db.refresh(db_team)
  return db_team

def get_teams(db: Session):
  return db.query(models.Team).all()

def get_team_by_id(db: Session, team_id: int):
  return db.query(models.Team).filter(models.Team.id == team_id).first()