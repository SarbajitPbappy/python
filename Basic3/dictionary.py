numbers=[12,56,98,78,56,12,6,98] #index is fixed

person=['Sarbajit','Dhaka',23,'Student']
# key value pair
# dictionary
# object
# hash table
# overlap with set
# mutable
# keys:value
person1={'name': 'Sarbajit','Address':'Dhaka','Age':23,'job':'student'}
print(person1)
print(person1['name'])
print(person1['Address'])
print(person1['Age'])
print(person1['job'])
print(person1.keys())
print(person1.values())
print(person1.items())
for key,value in person1.items():
    print(f'{key} : {value}')
person1['name']='Bappy'
print(person1)
person1['name']='Sarbajit'
print(person1)
person1['name']='Bappy'
print(person1)
print(list(person1))
print(tuple(person1))
print(set(person1))
print(dict(person1))
print(sorted(person1))
del person1['Address']
print(person1)