import sqlite3
import json


# --------------------------------
# Student_Master Class
# --------------------------------
class Student_Master:
    def __init__(self, stu_id, stu_name, stu_major, stu_courses, stu_cgpa):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_major = stu_major
        self.stu_courses = stu_courses
        self.stu_cgpa = stu_cgpa


# --------------------------------
# Faculty_Master Class
# --------------------------------
class Faculty_Master:
    def __init__(self, fac_id, fac_name, fac_department, fac_teaches_courses):
        self.fac_id = fac_id
        self.fac_name = fac_name
        self.fac_department = fac_department
        self.fac_teaches_courses = fac_teaches_courses


# --------------------------------
# Database Connection
# --------------------------------
conn = sqlite3.connect("college.db")
cursor = conn.cursor()


# Create Student Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student_Master (
    stu_id INTEGER PRIMARY KEY,
    stu_name TEXT,
    stu_major TEXT,
    stu_courses TEXT,
    stu_cgpa REAL
)
""")


# Create Faculty Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Faculty_Master (
    fac_id INTEGER PRIMARY KEY,
    fac_name TEXT,
    fac_department TEXT,
    fac_teaches_courses TEXT
)
""")

conn.commit()


# --------------------------------
# Add a New Student
# --------------------------------
def add_student():
    print("\n========== ADD NEW STUDENT ==========")

    try:
        stu_id = int(input("Enter Student ID: "))
        stu_name = input("Enter Student Name: ")
        stu_major = input("Enter Student Major: ")

        courses = input("Enter Student Courses (separated by commas): ")
        stu_courses = [
            course.strip() for course in courses.split(",") if course.strip()
        ]

        stu_cgpa = float(input("Enter Student CGPA: "))

        if not stu_name.strip() or not stu_major.strip():
            print("\nName and major cannot be empty!")
            return

        if not stu_courses:
            print("\nAt least one course must be entered!")
            return

        if not 0.0 <= stu_cgpa <= 4.0:
            print("\nCGPA must be between 0.0 and 4.0!")
            return

        # Create Student Object
        student = Student_Master(
            stu_id, stu_name, stu_major, stu_courses, stu_cgpa
        )

        # Insert Student Object into Database
        cursor.execute("""
        INSERT INTO Student_Master
        VALUES (?, ?, ?, ?, ?)
        """, (
            student.stu_id,
            student.stu_name,
            student.stu_major,
            json.dumps(student.stu_courses),
            student.stu_cgpa
        ))

        conn.commit()
        print("\nStudent added successfully!")

    except ValueError:
        print("\nInvalid input! Please enter the correct data types.")

    except sqlite3.IntegrityError:
        print("\nError! A student with this ID already exists.")

    except sqlite3.Error as e:
        print("\nDatabase Error:", e)


# --------------------------------
# Add a New Faculty Member
# --------------------------------
def add_faculty():
    print("\n========== ADD NEW FACULTY ==========")

    try:
        fac_id = int(input("Enter Faculty ID: "))
        fac_name = input("Enter Faculty Name: ")
        fac_department = input("Enter Faculty Department: ")

        courses = input("Enter Courses Taught (separated by commas): ")
        fac_teaches_courses = [
            course.strip() for course in courses.split(",") if course.strip()
        ]

        if not fac_name.strip() or not fac_department.strip():
            print("\nName and department cannot be empty!")
            return

        if not fac_teaches_courses:
            print("\nAt least one course must be entered!")
            return

        # Create Faculty Object
        faculty_member = Faculty_Master(
            fac_id, fac_name, fac_department, fac_teaches_courses
        )

        # Insert Faculty Object into Database
        cursor.execute("""
        INSERT INTO Faculty_Master
        VALUES (?, ?, ?, ?)
        """, (
            faculty_member.fac_id,
            faculty_member.fac_name,
            faculty_member.fac_department,
            json.dumps(faculty_member.fac_teaches_courses)
        ))

        conn.commit()
        print("\nFaculty member added successfully!")

    except ValueError:
        print("\nInvalid input! Please enter the correct data types.")

    except sqlite3.IntegrityError:
        print("\nError! A faculty member with this ID already exists.")

    except sqlite3.Error as e:
        print("\nDatabase Error:", e)


# --------------------------------
# Display Student Records
# --------------------------------
def display_students():
    cursor.execute("SELECT * FROM Student_Master")
    records = cursor.fetchall()

    print("\n========== STUDENT DETAILS ==========")

    if not records:
        print("No student records found.")
        return

    for record in records:
        print("\nStudent ID:", record[0])
        print("Student Name:", record[1])
        print("Major:", record[2])
        print("Courses:", ", ".join(json.loads(record[3])))
        print("CGPA:", record[4])


# --------------------------------
# Display Faculty Records
# --------------------------------
def display_faculty():
    cursor.execute("SELECT * FROM Faculty_Master")
    records = cursor.fetchall()

    print("\n========== FACULTY DETAILS ==========")

    if not records:
        print("No faculty records found.")
        return

    for record in records:
        print("\nFaculty ID:", record[0])
        print("Faculty Name:", record[1])
        print("Department:", record[2])
        print("Courses Taught:", ", ".join(json.loads(record[3])))


# --------------------------------
# Menu-Driven Program
# --------------------------------
try:
    while True:

        print("\n================================")
        print("       COLLEGE DATABASE")
        print("================================")
        print("1. Add a Student")
        print("2. Add Faculty")
        print("3. Display Student Records")
        print("4. Display Faculty Records")
        print("5. Display All Records")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            add_faculty()

        elif choice == "3":
            display_students()

        elif choice == "4":
            display_faculty()

        elif choice == "5":
            display_students()
            display_faculty()

        elif choice == "6":
            print("\nExiting College Database...")
            break

        else:
            print("\nInvalid choice! Please try again.")

finally:
    # Close Database Connection
    conn.close()
    print("\nDatabase connection closed.")

