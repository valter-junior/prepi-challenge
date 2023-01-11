from fastapi import FastAPI

from account import router as account
from auth import router as auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(account.router)
    