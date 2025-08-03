#main
import sqlite3

def create_connection():
    return sqlite3.connect('student_fee.db')

def initialize_db():
    conn = create_connection()
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, class TEXT, roll_number TEXT, email TEXT, phone TEXT,
            username TEXT UNIQUE, password TEXT
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT,
            status TEXT,
            FOREIGN KEY (student_id) REFERENCES students (id)
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS fees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            amount REAL,
            date TEXT,
            balance REAL,
            FOREIGN KEY (student_id) REFERENCES students (id)
        )
    ''')

    conn.commit()
    conn.close()