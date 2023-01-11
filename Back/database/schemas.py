from pydantic import BaseModel
import datetime



class ProductBase(BaseModel):
    amount: int
    value: int
    register_date : datetime.datetime

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: str
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
    email: str

class AccountCreate(AccountBase):
    password: str

class Account(AccountBase):
    id = str
    first_name: str
    last_name: str
    email : str
    hashed_password : str
    first_date_product_register : datetime.datetime 
    last_date_product_register : datetime.datetime
    amount_product : int
    first_date_order : datetime.datetime
    last_date_order : datetime.datetime
    amount_order : int

    products = list[Product]
    orders = list[Order]
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class AccountInDB(Account):
    hashed_password: str