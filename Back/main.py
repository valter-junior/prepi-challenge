from fastapi import FastAPI

from database import model
from database.database import engine

from account import router as account
from auth import router as auth
from product import router as product
from order import router as order

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(account.router)
app.include_router(product.router)
app.include_router(order.router)
    