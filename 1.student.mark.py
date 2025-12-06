students = []
courses = []
marks = {} 

# -------- Input Functions --------

def input_number_of_students():
    n = int(input("Number of students: "))
    for i in range(n):
        print(f"---- Student {i+1} ----")
        sid = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Date of birth: ")
        students.append({
            "id": sid,
            "name": name,
            "dob": dob
        })


def input_number_of_courses():
    n = int(input("Number of courses: "))
    for i in range(n):
        print(f"---- Course {i+1} ----")
        cid = input("Course ID: ")
        name = input("Course name: ")
        courses.append({
            "id": cid,
            "name": name
        })


def input_marks_for_course():
    cid = input("Enter course ID to input marks: ")

    # check if course exists
    found = False
    for c in courses:
        if c["id"] == cid:
            found = True

    if not found:
        print("Course not found.")
        return

    print(f"Input marks for course {cid}")

    course_marks = []
    for s in students:
        m = float(input(f"Mark for {s['name']} ({s['id']}): "))
        course_marks.append((s["id"], m))

    marks[cid] = course_marks


# -------- Listing Functions --------

def list_students():
    print("==== STUDENTS ====")
    for s in students:
        print(f"{s['id']} - {s['name']}, DoB: {s['dob']}")


def list_courses():
    print("==== COURSES ====")
    for c in courses:
        print(f"{c['id']} - {c['name']}")


def show_student_marks():
    cid = input("Course ID to show marks: ")

    if cid not in marks:
        print("No marks found for this course.")
        return

    print(f"==== Marks for course {cid} ====")
    for (sid, mark) in marks[cid]:
        # find student name
        for s in students:
            if s["id"] == sid:
                print(f"{s['name']} ({sid}): {mark}")


# -------- Main Program --------

def main():
    print("=== Student Mark Management ===")

    input_number_of_students()
    input_number_of_courses()

    while True:
        print("\nMenu:")
        print("1. List students")
        print("2. List courses")
        print("3. Input marks for a course")
        print("4. Show marks for a course")
        print("5. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            list_students()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            show_student_marks()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

main()
