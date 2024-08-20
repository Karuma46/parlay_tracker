from sqlalchemy.orm import Session
from . import models, schemas

def create_parlay(db: Session, parlay: schemas.Parlay):
  db_parlay = models.Parlay(**parlay.model_dump())
  db.add(db_parlay)
  db.commit()
  db.refresh(db_parlay)
  return db_parlay

def get_parlays(db: Session):
  return db.query(models.Parlay).all()

def get_parlay_by_id(db: Session, parlay_id: int):
  return db.query(models.Parlay).filter(models.Parlay.id == parlay_id).first()


def create_parlay_team(db: Session, parlay_team: schemas.ParlayTeam):
  db_parlay_team = models.ParlayTeam(**parlay_team.model_dump())
  db.add(db_parlay_team)
  db.commit()
  db.refresh(db_parlay_team)
  return db_parlay_team

def get_parlay_teams(db: Session):
  return db.query(models.ParlayTeam).all()

def get_parlay_team_by_id(db: Session, parlay_team_id: int):
  return db.query(models.ParlayTeam).filter(models.ParlayTeam.id == parlay_team_id).first()


def create_parlay_week(db: Session, parlay_week: schemas.ParlayWeek):
  db_parlay_week = models.ParlayWeek(**parlay_week.model_dump())
  db.add(db_parlay_week)
  db.commit()
  db.refresh(db_parlay_week)
  return db_parlay_week

def get_parlay_weeks(db: Session):
  return db.query(models.ParlayWeek).all()

def get_parlay_week_by_id(db: Session, parlay_week_id: int):
  return db.query(models.ParlayWeek).filter(models.ParlayWeek.id == parlay_week_id).first()


def create_parlay_event(db: Session, parlay_event: schemas.ParlayEvent):
  db_parlay_event = models.ParlayEvent(**parlay_event.model_dump())
  db.add(db_parlay_event)
  db.commit()
  db.refresh(db_parlay_event)
  return db_parlay_event

def get_parlay_events(db: Session):
  return db.query(models.ParlayEvent).all()

def get_parlay_event_by_id(db: Session, parlay_event_id: int):
  return db.query(models.ParlayEvent).filter(models.ParlayEvent.id == parlay_event_id).first()