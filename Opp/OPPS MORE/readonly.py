# read only property--> can be accessed as attribute
# gretter --> can be accessed as attribute privet
# setter --> can be accessed as attribute privet and set the value
class User:
    def __init__(self,name,age,money):
        self._name = name
        self._age = age
        self._money = money
    @property # if we use property then we can access the method as attribute
    def age(self):
        return self._age
    def name(self):
        return self._name
    @property
    def money(self):
        return self._money
    @money.setter
    def money(self,amount):
        self._money+= amount
    
sam=User("Sam",23,1000)
# print(sam.__name)
print(sam.name())
# print(sam.age())
print(sam.age)
print(sam.money)
sam.money=5000
print(sam.money)
