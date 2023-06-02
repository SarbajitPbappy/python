""" Write a class with three instance variables a,b and c.
Now add the following two methods in that class 
a)sum() to get the sum of a,b and c.
b)factorial() to get the factorial of b. """

import math

class MATH:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        result = self.a + self.b + self.c
        print(f'Sum of {self.a}, {self.b}, and {self.c} is--> {result}')
        return result

    def factorial(self):
        result = math.factorial(self.b)
        print(f'Factorial of b is--> {result}')
        return result

numbers = MATH(2, 3, 4)
numbers.sum()
numbers.factorial()
