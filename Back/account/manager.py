from sqlalchemy.orm import Session
import uuid
from database import model, schemas
from auth import manager as get

def get_account_by_email(db: Session, email: str):
    return db.query(model.Account).filter(model.Account.email == email).first()

def get_all (db: Session):
    return db.query(model.Account).all()

def create_account(db: Session, account: schemas.Account):
    db_account = model.Account(
        id = uuid.uuid4().hex,
        email=account.email, 
        hashed_password=get.get_password_hash(account.hashed_password),
        first_name= account.first_name,
        last_name = account.last_name,
        first_date_product_register = account.first_date_product_register,
        last_date_product_register = account.last_date_product_register,
        amount_product= account.amount_product,
        first_date_order = account.first_date_order,
        last_date_order = account.last_date_order,
        amount_order=  account.amount_order)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account