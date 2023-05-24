things='pen','tripod','pencil','mobile','charger','watter bottol',"books" #tuple
print(things)
print(f'Type of things is {type(things)}')
print(things[-1])
print(things[1:4]) #slice
print(things[::-1])
print(things[1:4:2])
print(things[1:4:1])
print(things[1:4:3])
count=things.count('pen')
print(f'Count of p is {count}')
for item in things:
    print(item)

length=len(things)
print(f'Length of things is {length}')

mega=([2,3,4],[6,7,8,9])
# i can not change any elements of tuple but if there exist list then we can change it
# ex:
mega[0][1]=5555
print(mega)