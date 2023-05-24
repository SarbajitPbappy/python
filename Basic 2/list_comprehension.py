numbers=[1,2,3,4,5,6]
# print(numbers)
odds=[]
# odds=[num for num in numbers if num%2!=0]
even=[]
# even=[num for num in numbers if num%2==0]
prime=[]
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
prime=[num for num in numbers if is_prime(num)]
for num in numbers:
    if num%2!=0:
        odds.append(num)
    elif num%2==0:
        even.append(num)
print(odds)
print(even)
print(prime)

""" 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
num = 17
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
 """