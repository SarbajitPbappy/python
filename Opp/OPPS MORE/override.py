class Person:
    def __init__(self, name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print(f"{self.name} is eating")
    def exercise(self):
        return NotImplementedError
# override
class Cricketer(Person):
    def __init__(self, name,age,height,weight,runs,wickets):
        super().__init__(name,age,height,weight)
        self.runs = runs
        self.wickets = wickets
    def eat(self):
        print(f"{self.name} is eating Banana")
    def exercise(self):
        print(f"{self.name} is running on gym")
    # overload
    def __add__(self,other):
        return self.runs+other.runs
    def __sub__(self,other):
        return self.runs-other.runs
    def __mul__(self,other):
        return self.runs*other.runs
    def __truediv__(self,other):
        return self.runs/other.runs
    def __len__(self):
        return self.runs
    def __gt__(self,other):
        return self.runs>other.runs
    
    
sakib= Cricketer("Sakib",35,5.7,60,8000,500)
musi=Cricketer("musi",35,5.7,60,8000,500)
# print(sakib.name)
# print(sakib.age)
# print(sakib.height)
# print(sakib.weight)
# print(sakib.runs)
# print(sakib.wickets)
# sakib.eat()
# sakib.exercise()

# overload
# print(45+47)
# print("45"+"47")
# print([45,47]+[1,2,3,4,5,6,7,8,9,10])
print(sakib+musi)
print(sakib-musi)
print(sakib*musi)
print(sakib/musi)
print(len(sakib))
print(sakib>musi)
