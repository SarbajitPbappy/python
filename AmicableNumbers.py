def factor(a):
    fact = []
    for i in range(1, a):
        if a % i == 0:
            fact.append(i)
    return sum(fact)

for i in range(1, 100000001):
    factorSum = factor(i)
    if factor(factorSum) == i and factorSum != i and i < factorSum:
        print(i, factorSum)
