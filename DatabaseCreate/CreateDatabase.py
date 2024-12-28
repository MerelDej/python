import sqlite3

def create_database():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        item TEXT NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (1, 'Merel', 'merel@gmail.com')")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (2, 'Arjan', 'arjan@gmail.com')")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (3, 'Zoë', 'zoe@gmail.com')")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (4, 'Ruben', 'ruben@gmail.com')")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (5, 'Catalina', 'catalina@gmail.com')")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (6, 'Quinten', 'quinten@gmail.com')")

    cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, item, price) VALUES (1, 5, 'Laptop', 1999.50)")
    cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, item, price) VALUES (2, 3, 'Headphones', 150.75)")
    cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, item, price) VALUES (3, 2, 'USB cable', 4.99)")
    cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, item, price) VALUES (4, 6, 'USB-c cable', 5.50)")
    cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, item, price) VALUES (5, 4, 'HDMI cable', 10.35)")
    cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, item, price) VALUES (6, 6, 'Phone', 199.99)")
    cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, item, price) VALUES (7, 1, 'Tablet', 299.99)")

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_database()