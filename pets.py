class Pet():
    def show(self):
        print(f"It name is {self.name}, it is {self.age} years old. It is a {self.type}")
class Dog(Pet):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = "Dog"
class Fish(Pet):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = "Fish"
class Cat(Pet):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.type = "Cat"

a1 = Dog("Bob", 7)
a1.show()
a2 = Fish("Tim", 3)
a2.show()