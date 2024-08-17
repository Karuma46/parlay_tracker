from fastapi import APIRouter, Depends, Response, Request
from ..database import SessionLocal
# from ..dependencies import get_token_header
from ..users import crud, schemas
from typing import Union
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/list")
async def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@router.post("/add")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user

@router.post("/login")
async def user_login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return crud.user_login(db, user)

@router.post("/logout")
async def user_logout(request: Request, db: Session = Depends(get_db)):
    return crud.user_logout(db, request.headers.get('Authorization'))

@router.get("/{user_id}")
async def get_user(user_id: Union[str, int], db: Session = Depends(get_db)):
    return crud.get_user_by_id(db, user_id)

@router.post("/update_password")
async def update_password(user: schemas.UserUpdatePassword, db: Session = Depends(get_db)):
    return crud.update_password(db, user)