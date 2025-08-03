#utility
from database import create_connection

def attendance_report(student_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT date, status FROM attendance WHERE student_id=?', (student_id,))
    rows = cur.fetchall()
    conn.close()
    return rows

def fee_status_report(student_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT amount, date, balance FROM fees WHERE student_id=?', (student_id,))
    rows = cur.fetchall()
    conn.close()
    return rows