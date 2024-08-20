from sqlalchemy.orm import Session
from fastapi import Depends
from ..database import get_db, engine
from ..parlays.models import Parlay, ParlayTeam, ParlayType
from ..teams.models import Team
from ..tasks.odds import odds

def create_parlays_events():

def get_team_odds():
  with Session(engine) as db:
  # Get all parlays
    parlays = db.query(Parlay).all()
    for parlay in parlays:
      # Get all active parly teams
      parlay_type = db.query(ParlayType).filter(ParlayType.id == parlay.type).first()
      side = 'home_team' if parlay_type.outcome == 1 else 'away_team'
      parlay_teams = db.query(ParlayTeam).filter(ParlayTeam.parlay_id == parlay.id).all()

      for parlay_team in parlay_teams:
        team = db.query(Team).filter(Team.id == parlay_team.team_id).first()
        for odd in odds:
          if odd[side] == team.name and len(odd['bookmakers']) > 0:
            market = odd['bookmakers'][0]['markets'][0]
            if(parlay_type.spread <= market['outcomes'][0]['price'] - market['outcomes'][1]['price']):
              print(odd['home_team'], odd['away_team'], odd['bookmakers'][0]['markets'][0]['outcomes'][0]['price'])

get_team_odds()