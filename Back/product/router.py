from typing import List
from fastapi import Depends, Query
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from database import  schemas
from product import manager
from database.database import get_db


router = APIRouter(
    prefix="/products",
    tags=["product"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=schemas.Product)
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    db_product = manager.get_product_by_name(db, name=product.name)
    if db_product:
        raise HTTPException(status_code=400, detail="Product already registered")
    return manager.create_product(db=db, product=product)

@router.get("/list", response_model=List[schemas.Product])
def read_users(db: Session = Depends(get_db)):
    users = manager.get_all(db)
    return users
