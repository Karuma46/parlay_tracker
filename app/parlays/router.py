from fastapi import APIRouter, Depends
from ..database import SessionLocal, get_db
from ..parlays import crud, schemas
from typing import Union
from sqlalchemy.orm import Session

router = APIRouter(
  prefix="/parlays",
  tags=["parlays"],
)

@router.get("/list")
async def get_parlays(db: Session = Depends(get_db)):
  parlays = crud.get_parlays(db)
  return parlays

@router.post("/add")
async def create_parlay(parlay: schemas.Parlay, db: Session = Depends(get_db)):
  return crud.create_parlay(db, parlay)

@router.get("/{parlay_id}")
async def get_parlay_by_id(parlay_id: int, db: Session = Depends(get_db)):
  return crud.get_parlay_by_id(db, parlay_id)

@router.post("/parlay_week/add")
async def create_parlay_week(parlay_week: schemas.ParlayWeek, db: Session = Depends(get_db)):
  return crud.create_parlay_week(db, parlay_week)

@router.get("/parlay_week/list")
async def get_parlay_weeks(db: Session = Depends(get_db)):
  return crud.get_parlay_weeks(db)

@router.get("/parlay_week/{parlay_week_id}")
async def get_parlay_week_by_id(parlay_week_id: int, db: Session = Depends(get_db)):
  return crud.get_parlay_week_by_id(db, parlay_week_id)

@router.get("/parlay_teams/list")
async def get_parlay_team(db: Session = Depends(get_db)):
  return crud.get_parlay_teams(db)

@router.get("/parlay_teams/{parlay_team_id}")
async def get_parlay_team_by_id(parlay_team_id: int, db: Session = Depends(get_db)):
  return crud.get_parlay_team_by_id(db, parlay_team_id)

@router.post("/parlay_teams/add")
async def create_parlay_team(parlay_team: schemas.ParlayTeam, db: Session = Depends(get_db)):
  return crud.create_parlay_team(db, parlay_team)

@router.get("/parlay_events/list")
async def get_parlay_events(db: Session = Depends(get_db)):
  return crud.get_parlay_events(db)

@router.get("/parlay_events/{parlay_event_id}")
async def get_parlay_event_by_id(parlay_event_id: int, db: Session = Depends(get_db)):
  return crud.get_parlay_event_by_id(db, parlay_event_id)

