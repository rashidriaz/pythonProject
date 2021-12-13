class Student:
    def __init__(self, name, age, registration_number):
        self.courses = set({})
        self.name = name
        self.age = age
        self.registration_number = registration_number

    def give_introduction(self):
        return "Hi! my name is " + self.name + ", I am " + str(
            self.age) + " years of age and y registration number is: " + self.registration_number

    def enroll_courses(self, courses):
        self.courses.union(courses)

    def enroll_course(self, course):
        self.courses.add(course)

    def print_courses(self):
        print("\n")
        for course in self.courses:
            print(course + "\t")
        print("\n")
