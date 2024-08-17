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

@router.post("/options/add")
async def create_option(option: schemas.Option, db: Session = Depends(get_db)):
  return crud.create_option(db, option)

@router.get("/options/list")
async def get_options(db: Session = Depends(get_db)):
  return crud.get_options(db)

@router.get("/options/{option_id}")
async def get_option_by_id(option_id: int, db: Session = Depends(get_db)):
  return crud.get_option_by_id(db, option_id)

# crud routes for parlaytype
@router.post("/parlay_type/add")
async def create_parlay_type(parlay_type: schemas.ParlayType, db: Session = Depends(get_db)):
  return crud.create_parlay_type(db, parlay_type)

@router.get("/parlay_type/list")
async def get_parlay_types(db: Session = Depends(get_db)):
  return crud.get_parlay_types(db)

@router.get("/parlay_type/{parlaytype_id}")
async def get_parlay_type_by_id(parlaytype_id: int, db: Session = Depends(get_db)):
  return crud.get_parlay_types_by_id(db, parlaytype_id)

@router.put("/parlay_type/{parlay_type_id}")
async def update_parlay_type(parlay_type_id: int, parlay_type: schemas.ParlayType, db: Session = Depends(get_db)):
  return crud.update_parlay_type(db, parlay_type_id, parlay_type)

@router.get("/parlay_type_options/list")
async def get_parlay_type_options(db: Session = Depends(get_db)):
  return crud.get_parlay_type_options(db)

@router.get("/parlay_type_options/{parlay_type_option_id}")
async def get_parlay_type_option_by_id(parlay_type_option_id: int, db: Session = Depends(get_db)):
  return crud.get_parlay_type_option_by_id(db, parlay_type_option_id)

@router.post("/parlay_type_options/add")
async def create_parlay_type_option(parlay_type_option: schemas.ParlayTypeOption, db: Session = Depends(get_db)):
  return crud.create_parlay_type_option(db, parlay_type_option)

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

