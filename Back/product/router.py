from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from database import  schemas
from product import manager
from database.database import get_db
from auth.manager import get_current_user

router = APIRouter(
    prefix="/products",
    tags=["product"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=schemas.Product)
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    db_product = manager.get_product_by_name(db, name=product.name)
    if db_product:
        raise HTTPException(status_code=400, detail="Email already registered")
    return manager.create_product(db=db, product=product)

@router.get("/list", response_model=List[schemas.Product])
def read_users(db: Session = Depends(get_db)):
    users = manager.get_all(db)
    return users
