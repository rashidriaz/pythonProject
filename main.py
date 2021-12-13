import Student as St
import GetCourse as Gtcrs

name = str(input("Enter your name:"))
age = int(input("Enter your age: "))
registration_number = str(input("Enter your registration number:"))
my_student = St.Student(name, age, registration_number)
print(my_student.give_introduction())

print("\nEnroll your courses: \n")
print("type end to exit")
course = Gtcrs.get_course_input()

while 'exit' not in course:
    my_student.enroll_course(course)

    course = Gtcrs.get_course_input()

my_student.print_courses()