#main
from database import initialize_db
from models import register_student, mark_attendance, pay_fee, login
from utils import attendance_report, fee_status_report

initialize_db()

print("Welcome to Student Fee & Attendance System")

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        clas = input("Class: ")
        roll = input("Roll Number: ")
        email = input("Email: ")
        phone = input("Phone: ")
        username = input("Username: ")
        password = input("Password: ")
        register_student(name, clas, roll, email, phone, username, password)
        print("Registered successfully.")

    elif choice == "2":
        user = login(input("Username: "), input("Password: "))
        if user:
            student_id = user[0]
            print(f"Welcome, {user[1]}")
            while True:
                print("\n1. Mark Attendance\n2. Pay Fee\n3. View Attendance\n4. View Fee Report\n5. Logout")
                opt = input("Option: ")

                if opt == "1":
                    date = input("Enter date (YYYY-MM-DD): ")
                    status = input("Status (Present/Absent): ")
                    mark_attendance(student_id, date, status)
                    print("Attendance marked.")

                elif opt == "2":
                    amount = float(input("Enter amount paid: "))
                    balance = float(input("Enter remaining balance: "))
                    pay_fee(student_id, amount, balance)
                    print("Fee payment recorded.")

                elif opt == "3":
                    for date, status in attendance_report(student_id):
                        print(f"{date}: {status}")

                elif opt == "4":
                    for amt, dt, bal in fee_status_report(student_id):
                        print(f"{dt}: Paid ₹{amt}, Balance ₹{bal}")

                elif opt == "5":
                    break
        else:
            print("Invalid login.")
    
from models import register_student, mark_attendance, pay_fee, login
from utils import attendance_report, fee_status_report

initialize_db()

print("Welcome to Student Fee & Attendance System")

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        clas = input("Class: ")
        roll = input("Roll Number: ")
        email = input("Email: ")
        phone = input("Phone: ")
        username = input("Username: ")
        password = input("Password: ")
        register_student(name, clas, roll, email, phone, username, password)
        print("Registered successfully.")

    elif choice == "2":
        user = login(input("Username: "), input("Password: "))
        if user:
            student_id = user[0]
            print(f"Welcome, {user[1]}")
            while True:
                print("\n1. Mark Attendance\n2. Pay Fee\n3. View Attendance\n4. View Fee Report\n5. Logout")
                opt = input("Option: ")

                if opt == "1":
                    date = input("Enter date (YYYY-MM-DD): ")
                    status = input("Status (Present/Absent): ")
                    mark_attendance(student_id, date, status)
                    print("Attendance marked.")

                elif opt == "2":
                    amount = float(input("Enter amount paid: "))
                    balance = float(input("Enter remaining balance: "))
                    pay_fee(student_id, amount, balance)
                    print("Fee payment recorded.")

                elif opt == "3":
                    for date, status in attendance_report(student_id):
                        print(f"{date}: {status}")

                elif opt == "4":
                    for amt, dt, bal in fee_status_report(student_id):
                        print(f"{dt}: Paid ₹{amt}, Balance ₹{bal}")

                elif opt == "5":
                    break
        else:
            print("Invalid login.")
    else:
        break