from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from database import  schemas
from order import manager
from database.database import get_db
from auth.manager import get_current_user

router = APIRouter(
    prefix="/orders",
    tags=["order"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=schemas.Order)
def create_Order(order: schemas.Order, db: Session = Depends(get_db)):
    db_order = manager.avaiable_product(db, product_id=order.product_id, amount=order.amount)
    if db_order is None:
        raise HTTPException(status_code=400, detail="Product amount is not avaiable try again.")
    return manager.create_order(db=db, order=order)

@router.get("/list", response_model=List[schemas.Order])
def read_users(db: Session = Depends(get_db)):
    orders = manager.get_all(db)
    return orders