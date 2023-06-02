# poly-->many
# morph-->shape
from math import pi

class Shape:
    def __init__(self,name) -> None:
        self.name=name
    def area(self):
        pass
    def perimeter(self):
        pass
    def __str__(self) -> str:
        return self.name

class Rectangele(Shape):
    def __init__(self,name,length,breadth) -> None:
        super().__init__(name)
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def __str__(self) -> str:
        return f"{super().__str__()} {self.length} {self.breadth}"

class Circle(Shape):
    def __init__(self,name,radius) -> None:
        super().__init__(name)
        self.radius=radius
    def area(self):
        return pi*self.radius**2
    def perimeter(self):
        return 2*pi*self.radius
    def __str__(self) -> str:
        return f"{super().__str__()} {self.radius}"
class Triangle(Shape):
    def __init__(self,name,a,b,c) -> None:
        super().__init__(name)
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s=(self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    def perimeter(self):
        return self.a+self.b+self.c
    def __str__(self) -> str:
        return f"{super().__str__()} {self.a} {self.b} {self.c}"

s1=Rectangele("Rectangle",10,20)
print(s1)
print(s1.area())
print(s1.perimeter())
s2=Circle("Circle",5)
print(s2)
print(s2.area())
print(s2.perimeter())
s3=Triangle("Triangle",3,4,5)
print(s3)
print(s3.area())
print(s3.perimeter())

    