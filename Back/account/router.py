from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from database import model, schemas
from account import manager
from database.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=schemas.Account)
def create_account(account: schemas.Account, db: Session = Depends(get_db)):
    db_account = manager.get_account_by_email(db, email=account.email)
    if db_account:
        raise HTTPException(status_code=400, detail="Email already registered")
    return manager.create_account(db=db, account=account)

@router.get("/list", response_model=List[schemas.Account])
def read_users(db: Session = Depends(get_db)):
    users = manager.get_all(db)
    return users
