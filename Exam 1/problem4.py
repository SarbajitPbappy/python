# args:
def SUM(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(SUM(1,2,3,4,5,6,7,8,9,10))

# kwargs:
def KWARGS(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")
KWARGS(name='Sakib',age=23,roll=123,dist='Dhaka',country='Bangladesh',phone=1234567890,profession='Student')
