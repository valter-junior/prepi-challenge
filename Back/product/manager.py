from sqlalchemy.orm import Session
import uuid
from database import model, schemas

def get_product_by_name(db: Session, name: str):
    return db.query(model.Product).filter(model.Product.name == name).first()

def get_all (db: Session):
    return db.query(model.Product).all()

def create_product(db: Session, product: schemas.Product):

    list_product = db.query(model.Product).filter(model.Product.account_id == product.account_id).first()    
    user = db.query(model.Account).filter(model.Account.id == product.account_id).first()
    
    if not list_product:
        user.first_date_product_register = product.register_date
        user.last_date_product_register = product.register_date
        user.amount_product += product.amount

    if user and list_product:
        user.last_date_product_register = product.register_date
        user.amount_product += product.amount
    
    db_product = model.Product(
        id = uuid.uuid4().hex,
        name = product.name,
        amount = product.amount,
        value = product.value,
        register_date = product.register_date,
        account_id = product.account_id
        )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product