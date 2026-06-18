from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# ADD STUDENT
# ==========================

@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"]
        course = request.form["course"]
        mobile = request.form["mobile"]
        email = request.form["email"]

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students (name, course, mobile, email)
        VALUES (?, ?, ?, ?)
        """, (name, course, mobile, email))

        conn.commit()
        conn.close()

        return redirect("/students")

    return render_template("add_student.html")


# ==========================
# VIEW & SEARCH STUDENTS
# ==========================

@app.route("/students")
def view_students():

    search = request.args.get("search")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    if search:

        cursor.execute(
            "SELECT * FROM students WHERE name LIKE ?",
            ('%' + search + '%',)
        )

    else:

        cursor.execute(
            "SELECT * FROM students"
        )

    students = cursor.fetchall()

    conn.close()

    return render_template(
        "view_students.html",
        students=students
    )


# ==========================
# DELETE STUDENT
# ==========================

@app.route("/delete/<int:id>")
def delete_student(id):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/students")


# ==========================
# UPDATE STUDENT
# ==========================

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_student(id):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        course = request.form["course"]
        mobile = request.form["mobile"]
        email = request.form["email"]

        cursor.execute("""
        UPDATE students
        SET name=?, course=?, mobile=?, email=?
        WHERE id=?
        """, (
            name,
            course,
            mobile,
            email,
            id
        ))

        conn.commit()
        conn.close()

        return redirect("/students")

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    )

    student = cursor.fetchone()

    conn.close()

    return render_template(
        "update_student.html",
        student=student
    )


if __name__ == "__main__":
    app.run(debug=True)