from decouple import config
import psycopg2
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe


def execute():

    API_BASE = config('BASE_URL')
    SHEET_BASE = config('SHEET_SECRET')
    conn = psycopg2.connect(API_BASE)
        
    sql = "SELECT * FROM accounts ORDER BY id ASC"

    df = pd.read_sql(sql, conn)

    gc = gspread.service_account(filename="evident-trees-374600-55495dcb0a4e.json")
    sh = gc.open_by_key(SHEET_BASE)
    worksheet = sh.get_worksheet(0)

    set_with_dataframe(worksheet, df)
