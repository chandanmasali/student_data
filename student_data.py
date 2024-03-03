class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.courses = {}

    def enroll(self, course):
        self.courses[course.course_code] = course

    def display_courses(self):
        print(f"Courses enrolled by {self.name}:")
        for course_code, course in self.courses.items():
            print(f"{course_code}: {course.name}")

class Teacher(Person):
    def __init__(self, teacher_id, name):
        super().__init__(teacher_id, name)
        self.courses_taught = []

    def teach(self, course):
        self.courses_taught.append(course)

    def display_courses_taught(self):
        print(f"Courses taught by {self.name}:")
        for course in self.courses_taught:
            print(course.name)

class Course:
    def __init__(self, course_code, name):
        self.course_code = course_code
        self.name = name
        self.students = []
        self.teacher = None

    def enroll_student(self, student):
        self.students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def display_students(self):
        print(f"Students enrolled in {self.name}:")
        for student in self.students:
            print(f"{student.person_id}: {student.name}")

class StudentManagementSystem:
    def __init__(self):
        self.people = {}
        self.courses = {}

    def add_person(self, person_id, name, role):
        if role == "student":
            person = Student(person_id, name)
        elif role == "teacher":
            person = Teacher(person_id, name)
        else:
            raise ValueError("Invalid role. Use 'student' or 'teacher'.")
        
        self.people[person_id] = person
        return person

    def add_course(self, course_code, name):
        course = Course(course_code, name)
        self.courses[course_code] = course
        return course

    def enroll_student_in_course(self, student, course):
        student.enroll(course)
        course.enroll_student(student)

# Example Usage:
sms = StudentManagementSystem()

# Adding students and teachers
student1 = sms.add_person(1, "Student1", "student")
student2 = sms.add_person(2, "Student2", "student")
teacher1 = sms.add_person(101, "Teacher1", "teacher")

# Adding courses
print( sms.add_course("MATH101", "Mathematics 101"))
physics_course = sms.add_course("PHY201", "Physics 201")

# Enrolling students in courses
sms.enroll_student_in_course(student1, math_course)
sms.enroll_student_in_course(student2, physics_course)

# Assigning a teacher to a course
math_course.assign_teacher(teacher1)

# Displaying information
student1.display_courses()
teacher1.display_courses_taught()
math_course.display_students()
