class Student:
    def __init__(self, sid, name, dob):
        self.__id = sid
        self.__name = name
        self.__dob = dob
        self.__marks = {}

    def input_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def list_marks(self, course_id):
        return self.__marks.get(course_id, None)


class Course:
    def __init__(self, cid, name):
        self.__id = cid
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            sid = input("Student ID: ")
            name = input("Name: ")
            dob = input("DoB: ")
            self.students.append(Student(sid, name, dob))

    def input_courses(self):
        n = int(input("Number of courses: "))
        for _ in range(n):
            cid = input("Course ID: ")
            name = input("Course name: ")
            self.courses.append(Course(cid, name))

    def list_students(self):
        print("\nStudents:")
        for s in self.students:
            print(f"{s.get_id()} - {s.get_name()}")

    def list_courses(self):
        print("\nCourses:")
        for c in self.courses:
            print(f"{c.get_id()} - {c.get_name()}")

    def input_marks(self):
        self.list_courses()
        cid = input("Choose course ID: ")
        for s in self.students:
            m = float(input(f"Mark for {s.get_name()}: "))
            s.input_mark(cid, m)

    def show_marks(self):
        cid = input("Course ID to show marks: ")
        print(f"\nMarks for course {cid}:")
        for s in self.students:
            mk = s.list_marks(cid)
            if mk is not None:
                print(f"{s.get_name()}: {mk}")
            else:
                print(f"{s.get_name()}: No mark")


def main():
    sm = StudentMarkManagement()
    sm.input_students()
    sm.input_courses()

    while True:
        print("\n1. List students")
        print("2. List courses")
        print("3. Input marks")
        print("4. Show marks")
        print("0. Quit")

        ch = input("Choice: ")

        if ch == "1": sm.list_students()
        elif ch == "2": sm.list_courses()
        elif ch == "3": sm.input_marks()
        elif ch == "4": sm.show_marks()
        elif ch == "0": break

main()
