# inheritance is a way to form new classes using classes that have already been defined. that means relation 

# class Animal:
#     pass

# # dog is an animal
# class Dog(Animal):
#     pass

# # cat is an animal
# class Cat(Animal):
#     pass

# # person is an object
# class Person:
#     pass

# # mary is a person
# mary = Person()
# mary.name = "Mary"
# print(mary.name)

class Engine:
    def __init__(self, capacity = 500):
        self.capacity = capacity

    def __str__(self):
        return f"Engine with a capacity of {self.capacity} cc"

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")
        
class Driver:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Driver's name is {self.name}"
    
# car has a relation with engine

class Car:
    def __init__(self)->None:
        self.engine = Engine()
        self.driver = Driver("Unknown")
        self.passengers = []
        
    def start(self):
        self.engine.start()
