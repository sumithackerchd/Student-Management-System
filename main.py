from database import (
    create_database,
    add_student,
    view_students,
    update_student,
    delete_student,
    search_student
)

create_database()

while True:

    print("\n===== Student Management System =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        course = input("Enter Course: ")
        mobile = input("Enter Mobile: ")
        email = input("Enter Email: ")

        add_student(name, course, mobile, email)

        print("Student Added Successfully!")

    elif choice == "2":

        students = view_students()

        print("\n===== Student Records =====")

        for student in students:
            print(student)

    elif choice == "3":

        student_id = input("Enter Student ID: ")

        name = input("Enter New Name: ")
        course = input("Enter New Course: ")
        mobile = input("Enter New Mobile: ")
        email = input("Enter New Email: ")

        update_student(
            student_id,
            name,
            course,
            mobile,
            email
        )

        print("Student Updated Successfully!")

    elif choice == "4":

        student_id = input("Enter Student ID: ")

        delete_student(student_id)

        print("Student Deleted Successfully!")

    elif choice == "5":

        name = input("Enter Student Name: ")

        results = search_student(name)

        print("\n===== Search Results =====")

        for student in results:
            print(student)

    elif choice == "6":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")