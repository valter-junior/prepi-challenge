from fastapi import FastAPI

from decouple import config
import psycopg2
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe

from database import model
from database.database import engine

from account import router as account
from auth import router as auth
from product import router as product
from order import router as order
from fastapi.middleware.cors import CORSMiddleware

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(account.router)
app.include_router(product.router)
app.include_router(order.router)
