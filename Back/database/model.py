from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(UUID, primary_key=True, index=True)
    frist_name = Column(String, unique=False, index=False)
    last_name = Column(String, unique=False, index=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    first_date_product_register = Column(DateTime)
    last_date_product_register = Column(DateTime)
    amount_product = Column(Integer)
    first_date_order = Column(DateTime)
    last_date_order = Column(DateTime)
    amount_order = Column(Integer)

    products = relationship("Product", back_populates="account")
    orders = relationship("Order", back_populates="account")


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID, unique=True, index=True)
    amount = Column(Integer)
    value = Column(Integer)
    register_date = Column(DateTime)
    account_id = Column(UUID, ForeignKey("accounts.id"))

    account = relationship("Account", back_populate="products")
    order = relationship("Order", back_populates="products")

class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID, unique=True, index=True)
    amount = Column(Integer)
    value = Column(Integer)
    order_date = Column(DateTime)
    product_id = Column(UUID, ForeignKey("products.id"))
    account_id = Column(UUID, ForeignKey("accounts.id"))

    account = relationship("Account", back_populate="orders")
    products = relationship("Product", back_populates="order")
