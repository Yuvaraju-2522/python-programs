nums = [1,2,1,3,2,5]
dici={}
for i in nums:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1
for i in dici:
    if dici[i]==1:
        print(i)