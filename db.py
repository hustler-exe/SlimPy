# db.py
import sqlite3

def initialize_database():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bmi_data (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            height REAL NOT NULL,
            weight REAL NOT NULL,
            bmi REAL NOT NULL,
            category TEXT NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(name, height, weight, bmi, category):
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO bmi_data (name, height, weight, bmi, category)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, height, weight, bmi, category))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM bmi_data')
    rows = c.fetchall()
    conn.close()
    return rows
