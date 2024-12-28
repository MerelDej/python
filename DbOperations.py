import sqlite3
import os
from settings.config import DB_PATH

def connect_db():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Database not found at path: {DB_PATH}")
    return sqlite3.connect(DB_PATH)

def fetch_all_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_all_orders():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_user(name, email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def add_order(user_id, item, price):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (user_id, item, price) VALUES (?, ?, ?)", (user_id, item, price))
    conn.commit()
    conn.close()

def update_user(user_id, new_name=None, new_email=None):
    conn = connect_db()
    cursor = conn.cursor()
    if new_name:
        cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, user_id))
    if new_email:
        cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    conn.commit()
    conn.close()

def update_order(order_id, new_item=None, new_price=None):
    conn = connect_db()
    cursor = conn.cursor()
    if new_item:
        cursor.execute("UPDATE orders SET item = ? WHERE id = ?", (new_item, order_id))
    if new_price is not None:
        cursor.execute("UPDATE orders SET price = ? WHERE id = ?", (new_price, order_id))
    conn.commit()
    conn.close()