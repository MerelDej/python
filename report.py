import pandas as pd
import sqlite3
import os
from settings.config import DB_PATH

def generate_report(file_type):
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT users.name AS User, orders.item AS Item, orders.price AS Price
    FROM users
    JOIN orders ON users.id = orders.user_id
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    try:
        os.mkdir("reports")
        print("Directory 'reports' created successfully.")
    except FileExistsError:
        print("Directory 'reports' already exsists.")

    if file_type == "csv":
        df.to_csv("reports/report.csv", index=False)
        print("Report generated: reports/report.csv")
    elif file_type == "excel":
        df.to_excel("reports/report.xlsx", index=False)
        print("Report generated: reports/report.xlsx")