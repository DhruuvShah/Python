import sqlite3

connect = sqlite3.connect("university.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student(
    StudentID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Class TEXT NOT NULL,
    Marks REAL
)""")
connect.commit()

def insert_student():
    sid = int(input("Student ID: "))
    name = input("Name: ")
    student_class = input("Class: ")
    marks = float(input("Marks: "))
    cursor.execute(
        "INSERT INTO Student (StudentID, Name, Class, Marks) VALUES (?, ?, ?, ?)",
        (sid, name, student_class, marks)
    )
    connect.commit()
    print("Student inserted.")

def read_student():
    cursor.execute("SELECT StudentID, Name, Class, Marks FROM Student")
    rows = cursor.fetchall()
    if not rows:
        print("No student record found.")
    for row in rows:
        print(row)

def update_student():
    sid = int(input("Student ID to update: "))
    marks = float(input("New marks: "))
    cursor.execute("UPDATE Student SET Marks = ? WHERE StudentID = ?", (marks, sid))
    connect.commit()
    print("Rows updated:", cursor.rowcount)

def delete_student():
    sid = int(input("Student ID to delete: "))
    cursor.execute("DELETE FROM Student WHERE StudentID = ?", (sid,))
    connect.commit()
    print("Rows deleted:", cursor.rowcount)

while True:
    print("\n1. Insert 2. Read 3. Update 4. Delete 5. Exit")
    choice = input("Choose an option: ")
    try:
        if choice == "1":
            insert_student()
        elif choice == "2":
            read_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    except sqlite3.IntegrityError as error:
        print("Database integrity error:", error)
    except ValueError:
        print("Please enter valid numeric values.")
    except sqlite3.Error as error:
        print("Database error:", error)

connect.close()
