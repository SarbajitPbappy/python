# Minimize Number
flag=True
counter=0
size=int(input())
arr=[]
ele=input().split()
arr=[int(num) for num in ele]
for num in arr:
    if num % 2 != 0:
        flag = False
        break
while flag:
    for num in arr:
        if num % 2 != 0:
            flag = False
            break
        arr[arr.index(num)] = num / 2
    if flag:
        counter += 1
    else:
        break
print(counter)

