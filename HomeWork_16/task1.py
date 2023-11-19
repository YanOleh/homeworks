class Person:
    def __init__(self, full_name):
        self.full_name = full_name


class Student(Person):
    def __init__(self, full_name, grant, course):
        super().__init__(full_name)
        self.grant = grant
        self.course = course

class Teacher(Person):
    def __init__(self,full_name, salary, subject):
        super().__init__(full_name)
        self.salary = salary
        self.salary = salary
        self.subject = subject



student1 = Student('Oleh Yankula', 1500, 3)
teacher1 = Teacher('Tamara Tamara', 2000, 'math')

print(student1.full_name)
print(student1.grant)
print(student1.course)
print(teacher1.full_name)
print(teacher1.salary)
print(teacher1.subject)