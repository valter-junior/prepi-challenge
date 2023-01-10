from pydantic import BaseModel
import uuid, datetime



class ProductBase(BaseModel):
    amount: int
    value: int
    register_date : datetime

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: uuid
    account_id: uuid

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    amount: int
    value: int
    order_date : datetime

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: uuid
    product_id: uuid
    account_id: uuid

    class Config:
        orm_mode = True


class AccountBase(BaseModel):
    email: str

class AccountCreate(AccountBase):
    password: str

class Account(AccountBase):
    id = uuid
    firt_name: str
    last_name: str
    email : str
    hashed_password : str
    first_date_product_register : datetime 
    last_date_product_register : datetime
    amount_product : int
    first_date_order : datetime
    last_date_order : datetime
    amount_order : int

    products = list[Product]
    orders = list[Order]
    
    class Config:
        orm_mode = True
