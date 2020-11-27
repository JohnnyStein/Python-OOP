class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'Dog name is {self.name}, and it is {self.age} years old!')