from pydantic import BaseModel
import datetime



class ProductBase(BaseModel):
    name: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id : str 
    amount: int
    value: int
    register_date : datetime.datetime
    account_id: str

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    amount: int
    value: int
    order_date : datetime.datetime

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: str
    product_id: str
    account_id: str

    class Config:
        orm_mode = True


class AccountBase(BaseModel):
    id: str
    email: str

class AccountCreate(AccountBase):
    password: str

class Account(AccountBase):
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    first_date_product_register : datetime.datetime | None = None
    last_date_product_register : datetime.datetime | None = None
    amount_product : int | None = None
    first_date_order : datetime.datetime | None = None
    last_date_order : datetime.datetime | None = None
    amount_order : int | None = None
    amount_register_product : int | None = None
    amount_register_order : int | None = None

    products = list[Product]
    orders = list[Order]
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user: object


class TokenData(BaseModel):
    email: str | None = None


class AccountInDB(Account):
    hashed_password: str
