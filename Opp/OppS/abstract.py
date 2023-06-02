# abstract base class
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod #enforce all derived class to have all the method
    
    def eat(self):
        print('Need Food')
    # @abstractmethod
    def move(self):
        pass
    
class Goru(Animal):
    def __init__(self,name) -> None:
        self.category='Goru'
        self.name=name
        super().__init__()
    def eat(self):
        print('Eatting Banana')

lyka=Goru('Mon')
lyka.eat()