# Good Sequence
n=int(input())
a=list(map(int,input().split()))
d={}
for num in a:
    if num not in d:
        d[num]=1
    else:
        d[num]+=1
ans=0
for f,l in d.items():
    if f>l:
        ans+=l
    else:
        ans+=l-f
print(ans)