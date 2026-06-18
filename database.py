import sqlite3

def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        course TEXT NOT NULL,
        mobile TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_student(name, course, mobile, email):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, course, mobile, email) VALUES (?, ?, ?, ?)",
        (name, course, mobile, email)
    )

    conn.commit()
    conn.close()


def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students
def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()


def search_student(name):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    results = cursor.fetchall()

    conn.close()

    return results
def update_student(student_id, name, course, mobile, email):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET name=?, course=?, mobile=?, email=?
    WHERE id=?
    """, (name, course, mobile, email, student_id))

    conn.commit()
    conn.close()