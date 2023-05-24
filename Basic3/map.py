from lamda import doubled as db
numbers=[12,56,98,78,56,12,6,98]
print(numbers)
doubled_nums=map(db,numbers)
print(list(doubled_nums))

actors=[
    {'name':'John','age':45},
    {'name':'Brad','age':55},
    {'name':'Tom','age':35},
    {'name':'Jack','age':25},
    {'name':'Harry','age':15},
    {'name':'Ron','age':5},
    {'name':'Hermione','age':25},
    {'name':'Emma','age':35},
    {'name':'Watson','age':45},
]

juniors=filter(lambda actor : actor['age']<40,actors)
print(list(juniors))