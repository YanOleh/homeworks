class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        message =f'Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old'
        print(message)

person1 = Person('Carl', 'Johnson', '26')
person2 = Person('Tolik', 'Petrov', '30')

person1.talk()
person2.talk()