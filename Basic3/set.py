# set: unique items collection no duplicate
numbers=[12,56,98,78,56,12,6,98]
print(numbers)
number_set=set(numbers)
print(number_set)
number_set.add(55)
print(number_set)
number_set.remove(55)
print(number_set)
for j in number_set:
    print(j)

if 9 in number_set:
    print("yes")
else:
    print("no")

A={1,3,5}
B={2,4,6,5}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
print(A.issubset(B))
print(A.issuperset(B))
print(A.isdisjoint(B))
print(A.update(B))