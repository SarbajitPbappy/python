import math
import time
def timer(func):
    def inner(*args, **kwargs):
        print('time started')
        start = time.time()
        func(*args, **kwargs)
        # lent= len(args)
        # print(lent)
        print('time ended')
        end = time.time()
        print(f'time taken {end-start}')
    return inner
# timer()

@timer  # decorator that is used to add extra functionality to a function
def get_factorial(n):
    print('factorial started')
    print(f'factorial of {n} is {math.factorial(n)}')

# get_factorial(5)
get_factorial(n=5500)