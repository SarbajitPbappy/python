arr=[100,200,300,400]
arr.append(45)
arr.append(55)
arr.append(65)
print(arr)
arr.insert(2,500)
print(arr)
arr.remove(300)
print(arr)
arr.pop()
print(arr)
arr.pop(2)
print(arr)
arr.reverse()
print(arr)
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)
print(arr.count(100))
print(arr.index(100))
# arr.clear()
# print(arr)
arr2=arr.copy()
print(arr2)
""" 
my_list = [1, 2, 3, 4, 5]

value_to_remove = 3
my_list.remove(value_to_remove)  # Removes the first occurrence of 3

print(my_list)  # Output: [1, 2, 4, 5]


my_list = [1, 2, 3, 4, 5, 3, 6, 3]
value_to_remove = 3

while value_to_remove in my_list:
    my_list.remove(value_to_remove) //remove all occurance

print(my_list)  # Output: [1, 2, 4, 5, 6]

 """