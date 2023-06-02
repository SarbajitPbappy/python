# parent class

# class BaseClass:
#     pass

# # child class
# class DerivedClass(BaseClass):
#     pass

""" 
1.Simple Inheritance : parent class--->child class
2.Multilevel Inheritance : parent class--->child class--->grandchild class
"""

# multilevel inheritance

class Vehicle:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
        
    def move(self):
        return f'{self.name} is moving'
    
class Bus(Vehicle):
    def __init__(self,name,price,seats) -> None:
        self.seats=seats
        super().__init__(name,price)
        
    def __repr__(self) -> str:
        return f'Bus {self.name} with {self.seats} seats'
    
class Car(Vehicle):
    def __init__(self,name,price,engine) -> None:
        self.engine=engine
        super().__init__(name,price)
        
    def __repr__(self) -> str:
        return f'Car {self.name} with {self.engine} engine'

class Truck(Car):
    def __init__(self,name,price,engine,load) -> None:
        self.load=load
        super().__init__(name,price,engine)
        
    def __repr__(self) -> str:
        return f'Truck {self.name} with {self.engine} engine and {self.load} load'
    
class Motorcycle(Vehicle):
    def __init__(self,name,price,engine) -> None:
        self.engine=engine
        super().__init__(name,price)
        
    def __repr__(self) -> str:
        return f'Motorcycle {self.name} with {self.engine} engine'

class ACBus(Bus):
    def __init__(self,name,price,seats,ac) -> None:
        self.ac=ac
        super().__init__(name,price,seats)
        
    def __repr__(self) -> str:
        return f'ACBus {self.name} with {self.seats} seats and {self.ac} ac'

green_line=ACBus('Green Line',1000000,50,'Central')
print(green_line)