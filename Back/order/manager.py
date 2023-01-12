from sqlalchemy.orm import Session
import uuid
from database import model, schemas

def get_orders_by_product(db: Session, product_id: str):
    return db.query(model.Order).filter(model.Order.product_id == product_id).all()

def get_all (db: Session):
    return db.query(model.Order).all()

def avaiable_product(db: Session, product_id: str, amount: int):

    avaiable_product = db.query(model.Product).filter(model.Product.id == product_id).first()

    if avaiable_product.amount >= amount:
        return avaiable_product

    elif avaiable_product.amount < amount:
        return None

def create_order(db: Session, order: schemas.Order):

    find_order = db.query(model.Order).filter(model.Order.account_id == order.account_id).first()

    user = db.query(model.Account).filter(model.Account.id == order.account_id).first()

    product = db.query(model.Product).filter(model.Product.id == order.product_id).first()

    if product:
        product.amount -= order.amount
    
    if not find_order:
        user.first_date_order = order.order_date
        user.last_date_order = order.order_date
        user.amount_order += order.amount
        user.amount_register_order += 1

    if user and find_order:
        user.last_date_order = order.order_date
        user.amount_order += order.amount
        user.amount_register_order += 1
   
    db_order = model.Order(
        id = uuid.uuid4().hex,
        amount = order.amount,
        value = order.value,
        order_date = order.order_date,
        product_id = order.product_id,
        account_id = order.account_id
        )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order
