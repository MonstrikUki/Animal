class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Eat(self):
        pass

    def Sleep(self):
        pass

class Bird(Animal):
    def Fly(self):
        pass

class Fish(Animal):
    def Swim(self):
        pass

class Mammal(Animal):
    def Walk(self):
        pass

bird = Bird("Кеша", 2)
fish = Fish("Немо", 1)
mammal = Mammal("Шарик", 4)
