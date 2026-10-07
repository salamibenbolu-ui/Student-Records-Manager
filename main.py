#This is my 34th project(Day 34/100 of learning python)
#laerning lists + dictionary together

students = []

while True:
    print("===== STUDENTS RECORD MANAGER =====")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Exit")
    choice = int(input("Enter your option: "))

    if choice == 1:
        stu_name = input("Enter your name: ").strip().title()
        stu_score = float(input("Enter your score: "))
        student = {"name": stu_name,
                   "score": stu_score}
        students.append(student)
        print("Student added successfully")

    elif choice == 2:
        if not students:
            print("No student found.")
        else:
            print("===== ALL STUDENTS =====")
            for student in students:
                print(f"Name: {student["name"]}")
                print(f"Score: {student["score"]}")

    elif choice == 3:
        stu_name = input("Enter your name: ").strip().title()
        found = False
        for student in students:
            if student["name"].lower() == stu_name.lower():
                print("===== STUDENT FOUND =====")
                print(f"Name: {student["name"]}")
                print(f"Score: {student["score"]}")
                found = True
                break
        if not found:
            print("Student not found")

    elif choice == 4:
        print("Thank you for using the Student Record Manager")
        break

    else:
        print("Invalid option")
