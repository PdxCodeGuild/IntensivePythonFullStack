class Animal:
    def __init__(self, name, food):
        self.name = name
        self.favorite_food = food

    def print_me(self):
        print("this won't ever print unless you use super()")

    def example(self):
        print("Hello from the super class")

class Squirrel(Animal):
    def __init__(self, name, food):
        super().__init__(name, food)
        self.type_of_creature = "squirrel"
        self.legs = 4

    def print_me(self):
        print(s.name, s.favorite_food, s.type_of_creature, s.legs)
        # super().print_me()

class Anteater(Animal):
    def __init__(self, name, food):
        self.type_of_creature = "anteater"
        self.legs = 4

class Snake(Animal):
    def __init__(self, name, food):
        self.type_of_creature = "danger noodle"
        self.legs = 0

s = Squirrel("Clarance", "nuts")
s.print_me()
s.example()

a = Anteater("Jimmy", "ants")
a.example()
a.print_me()