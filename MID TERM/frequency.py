def freq(n,m,a):
    frequency = [0]*(m+1)
    for i in a:
        frequency[i] += 1
    return frequency[1:]
    
n,m=map(int,input().split())
a=list(map(int,input().split()))

for size in freq(n,m,a):
    print(size)