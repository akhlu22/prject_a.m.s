#contains
from database import create_connection
from datetime import datetime

def register_student(name, student_class, roll, email, phone, username, password):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO students (name, class, roll_number, email, phone, username, password)
        VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (name, student_class, roll, email, phone, username, password))
    conn.commit()
    conn.close()

def mark_attendance(student_id, date, status):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO attendance (student_id, date, status)
        VALUES (?, ?, ?)''', (student_id, date, status))
    conn.commit()
    conn.close()

def pay_fee(student_id, amount, balance):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO fees (student_id, amount, date, balance)
        VALUES (?, ?, ?, ?)''', (student_id, amount, datetime.now().strftime('%Y-%m-%d'), balance))
    conn.commit()
    conn.close()

def login(username, password):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM students WHERE username=? AND password=?', (username, password))
    return cur.fetchone()