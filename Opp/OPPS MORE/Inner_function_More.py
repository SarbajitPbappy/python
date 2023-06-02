# 1. Encapsulation:
class Calculator:
    def calculate(self,a,b):
        def add():
            return a+b
        def sub():
            return abs(a-b)
        def mul():
            return a*b
        def div():
            if b==0:
                return "Cannot divide by zero"
            else:
                return a/b
        return add(),sub(),mul(),div()
obj=Calculator()
print(obj.calculate(10,20))
"""
In this example, we have defined a class Calculator, with a method calculate and
four inner functions add, sub, mul and div. The inner functions are not accessible
outside, so the variables a and b are also not accessible outside. This improve the
security of our program. We can only access the inner functions by calling the outer
function calculate. 
"""

# 2. Closure and State Retention:
def outer_func(text):
    message=text
    def inner_func():
        print(message)
    return inner_func
my_func=outer_func('Hey!')
my_func()
"""
A Closure is a function object that remembers values in enclosing scopes
even if they are not present in memory. Closures assist in calling functions 
outside of their scope, as can be seen from the code above.
Only the outerFunction is inside the scope of the function innerFunction. 
However, we can simply increase its scope by calling a function outside of it by using closures.
 
"""
# 3. Decorators:
import math
import time
def timer(func):
    def inner(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f'time taken {end-start}')
        return result
    return inner
@timer  # decorator that is used to add extra functionality to a function
def get_factorial(n):
    print(f'factorial of {n} is {math.factorial(n)}')
get_factorial(n=12)
"""
Inner functions are commonly used when defining decorators in Python. 
Decorators allow you to modify the behavior of functions or methods by 
wrapping them with additional functionality. 
"""
