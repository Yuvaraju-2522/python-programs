arr = [2,2,2,3,3]
dici={}
a=[]
for i in arr:
    if i  not in dici:
        dici[i]=1
    else:
        dici[i]+=1
for i,j in dici.items():
    if i==j:
        a.append(i)
if len(a)==0:
    print(-1)
else:
    print(max(a))

        