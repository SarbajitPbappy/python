class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


class Bulldog(Dog):
    def guard(self):
        print(f"{self.name} is guarding the house.")


# instances of the classes
animal = Animal("Animal")
animal.eat()

dog = Dog("Dog")
dog.eat()
dog.bark()

bulldog = Bulldog("Bulldog")
bulldog.eat()
bulldog.bark()
bulldog.guard()
