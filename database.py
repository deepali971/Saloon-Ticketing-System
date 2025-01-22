# database.py
import sqlite3

def create_connection():
    conn = sqlite3.connect('saloon.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            ticket_id TEXT NOT NULL,
            services TEXT NOT NULL,
            total_amount REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()