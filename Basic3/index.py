numbers=[12,56,98,78,56,12,6,98]
for index,num in enumerate(numbers): #printing with index
    print(f'[Index->{index}][Value->{num}]')

# for negative index
print('------------------------------------------------------')

for index, num in enumerate(numbers[::-1]):
    print(f'[Index->{-index - 1}][Value->{num}]')