class Animal:
    def talk(self):
        print("Animal voice")

class Dog(Animal):
    def talk(self):
        return "WOOF!"

class Cat(Animal):
    def talk(self):
        return "MEOW!"

def generic(obj):
    if isinstance(obj, Animal):
        print(obj.talk())

dog = Dog()
cat = Cat()
print(dog.talk())
print(cat.talk())

generic(cat)


# class Animal:
#     def __init__(self, voice):
#         self.voice = voice
#
#     def talk(self):
#         print(self.voice)
#
# class Dog(Animal):
#     ...
# class Cat(Animal):
#     ...
#
#
# dog = Dog("WOOF!")
# cat = Cat("MEOW!")
# cat.talk()
# dog.talk()