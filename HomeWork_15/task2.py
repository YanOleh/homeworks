class Dog:
    age_factor = 7
    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * self.age_factor

dog1 = Dog(5)
print(f"The dog's age in human equivalent is {dog1.human_age()} years.")