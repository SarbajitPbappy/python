# def full_name(first,last):
#     return f'Full name is: {first}{last}'
# print(full_name('John','Smith'))

from typing import Tuple

# def big_name(first,last,title,**addition):
#     name= f'Full name is:  {first} {title} {last}'
#     # print(addition['title'])
#     for key,value in addition.items():
#         print(f'{key} : {value}')
#     return name
# name = big_name(first='Sarbajit',last='Bappy',title='Paul',addition='Mr')
# print(name)


#return multiple arguments

def sum_sub(num1,num2):
    # return num1+num2,num1-num2,num1*num2,num1/num2; //tupple
    if num2>num1:
        num1,num2=num2,num1
    return [num1+num2,num1-num2,num1*num2,num1/num2] #list
print(sum_sub(10,20))