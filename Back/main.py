from typing import List
import os

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import model, schemas
from account import manager
from database.database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/account/", response_model=schemas.Account)
def create_account(account: schemas.Account, db: Session = Depends(get_db)):
    db_account = manager.get_account_by_email(db, email=account.email)
    if db_account:
        raise HTTPException(status_code=400, detail="Email already registered")
    return manager.create_account(db=db, account=account)
