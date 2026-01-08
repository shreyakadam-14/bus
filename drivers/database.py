import sqlite3

DB_NAME = "drivers.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drivers (
            driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            dob TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def get_next_driver_id():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(driver_id) FROM drivers")
    row = cursor.fetchone()

    next_id = 1 if row[0] is None else row[0] + 1

    conn.close()
    return next_id


def insert_driver(name, dob, age, gender, phone, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO drivers (name, dob, age, gender, phone, email)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, dob, age, gender, phone, email))

    conn.commit()
    conn.close()
