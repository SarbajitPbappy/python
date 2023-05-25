# MAX SPLIT

STR=input()
SPLIT=[]
L_count=0
R_count=0
for i in STR:
    if i=='L':
        L_count+=1
    else:
        R_count+=1
    if L_count==R_count:
        SPLIT.append(STR[:L_count+R_count])
        STR=STR[L_count+R_count:]
        L_count=0
        R_count=0
print(len(SPLIT))
for STRING in SPLIT:
    print(STRING)
        
