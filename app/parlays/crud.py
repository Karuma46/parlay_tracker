from sqlalchemy.orm import Session
from . import models, schemas

def create_option(db: Session, option: schemas.Option):
  db_option = models.Option(**option.model_dump())
  db.add(db_option)
  db.commit()
  db.refresh(db_option)
  return db_option

def get_options(db: Session):
  return db.query(models.Option).all()

def get_option_by_id(db: Session, option_id: int):
  return db.query(models.Option).filter(models.Option.id == option_id).first()


def create_parlay_type(db: Session, parlay_type: schemas.ParlayType):
  db_parlay_type = models.ParlayType(**parlay_type.model_dump())
  db.add(db_parlay_type)
  db.commit()
  db.refresh(db_parlay_type)
  return db_parlay_type

def update_parlay_type(db: Session, parlay_type_id: int, parlay_type: schemas.ParlayType):
  db_parlay_type = db.query(models.ParlayType).filter(models.ParlayType.id == parlay_type_id).first()
  db_parlay_type.name = parlay_type.name
  db_parlay_type.outcome = parlay_type.outcome
  db.commit()
  db.refresh(db_parlay_type)
  return db_parlay_type

def get_parlay_types(db: Session):
  return db.query(models.ParlayType).all()

def get_parlay_types_by_id(db: Session, parlay_type_id: int):
  return db.query(models.ParlayType).filter(models.ParlayType.id == parlay_type_id).first()


def create_parlay_type_option(db: Session, parlay_type_option: schemas.ParlayTypeOption):
  db_parlay_type_option = models.ParlayTypeOption(**parlay_type_option.model_dump())
  db.add(db_parlay_type_option)
  db.commit()
  db.refresh(db_parlay_type_option)
  return db_parlay_type_option

def get_parlay_type_options(db: Session):
  return db.query(models.ParlayTypeOption).all()

def get_parlay_type_options_by_id(db: Session, parlay_type_option_id: int):
  return db.query(models.ParlayTypeOption).filter(models.ParlayTypeOption.id == parlay_type_option_id).first()


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