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
# Create 5 Student Objects
# --------------------------------
students = [
    Student_Master(1, "John Smith", "Computer Science",
                   ["Python", "Database", "Networking"], 3.8),

    Student_Master(2, "Emily Johnson", "Mathematics",
                   ["Calculus", "Statistics", "Algebra"], 3.6),

    Student_Master(3, "Michael Brown", "Engineering",
                   ["Physics", "Robotics", "Electronics"], 3.9),

    Student_Master(4, "Sarah Davis", "Biology",
                   ["Chemistry", "Genetics", "Ecology"], 3.7),

    Student_Master(5, "David Wilson", "Information Technology",
                   ["Cybersecurity", "Programming", "Web Design"], 3.5)
]


# --------------------------------
# Create 5 Faculty Objects
# --------------------------------
faculty = [
    Faculty_Master(101, "Dr. James", "Computer Science",
                   ["Python", "Database"]),

    Faculty_Master(102, "Prof. Williams", "Mathematics",
                   ["Calculus", "Statistics"]),

    Faculty_Master(103, "Dr. Anderson", "Engineering",
                   ["Physics", "Robotics"]),

    Faculty_Master(104, "Prof. Taylor", "Biology",
                   ["Chemistry", "Genetics"]),

    Faculty_Master(105, "Dr. Thomas", "Information Technology",
                   ["Cybersecurity", "Networking"])
]


# --------------------------------
# Insert Student Records
# --------------------------------
def insert_students():
    for student in students:
        cursor.execute("""
        INSERT OR IGNORE INTO Student_Master
        VALUES (?, ?, ?, ?, ?)
        """, (
            student.stu_id,
            student.stu_name,
            student.stu_major,
            json.dumps(student.stu_courses),
            student.stu_cgpa
        ))

    conn.commit()
    print("\nStudent records inserted successfully!")


# --------------------------------
# Insert Faculty Records
# --------------------------------
def insert_faculty():
    for member in faculty:
        cursor.execute("""
        INSERT OR IGNORE INTO Faculty_Master
        VALUES (?, ?, ?, ?)
        """, (
            member.fac_id,
            member.fac_name,
            member.fac_department,
            json.dumps(member.fac_teaches_courses)
        ))

    conn.commit()
    print("\nFaculty records inserted successfully!")


# --------------------------------
# Display Student Records
# --------------------------------
def display_students():
    cursor.execute("SELECT * FROM Student_Master")
    records = cursor.fetchall()

    print("\n========== STUDENT DETAILS ==========")

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

    for record in records:
        print("\nFaculty ID:", record[0])
        print("Faculty Name:", record[1])
        print("Department:", record[2])
        print("Courses Taught:", ", ".join(json.loads(record[3])))


# --------------------------------
# Menu-Driven Program
# --------------------------------
while True:

    print("\n================================")
    print("       COLLEGE DATABASE")
    print("================================")
    print("1. Insert Student Records")
    print("2. Insert Faculty Records")
    print("3. Display Student Records")
    print("4. Display Faculty Records")
    print("5. Display All Records")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        insert_students()

    elif choice == "2":
        insert_faculty()

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


# Close Database Connection
conn.close()