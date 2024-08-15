from fastapi import APIRouter, Depends, Request
from ..database import SessionLocal, get_db
from . import crud, schemas
from typing import Union
from sqlalchemy.orm import Session

router = APIRouter(
  prefix="/teams",
  tags=["teams"],
)

@router.get("/{team_id}")
async def get_team_by_id(team_id: int, db: Session = Depends(get_db)):
  return crud.get_team_by_id(db, team_id)

@router.get("/list")
async def get_teams(db: Session = Depends(get_db)):
  teams = crud.get_teams(db)
  return teams

@router.post("/add")
async def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
  return crud.create_team(db, team)

@router.post("/sports/add")
async def create_sport(sport: schemas.SportCreate, db: Session = Depends(get_db)):
  return crud.create_sport(db, sport)

@router.get("/sports/list")
async def get_sports(db: Session = Depends(get_db)):
  return crud.get_sports(db)

@router.get("/sports/{sport_id}")
async def get_sport_by_id(sport_id: int, db: Session = Depends(get_db)):
  return crud.get_sport_by_id(db, sport_id)

@router.post("/leagues/add")
async def create_league(league: schemas.LeagueCreate, db: Session = Depends(get_db)):
  return crud.create_league(db, league)

@router.get("/leagues/list")
async def get_leagues(db: Session = Depends(get_db)):
  return crud.get_leagues(db)

@router.get("/leagues/{league_id}")
async def get_league_by_id(league_id: int, db: Session = Depends(get_db)):
  return crud.get_league_by_id(db, league_id)