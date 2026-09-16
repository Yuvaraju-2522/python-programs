nums=[-4,-2,-1,-1,0,1,2,3,5]
k=3
arr=[[]]
a=[]
for i in nums:
    for j in arr.copy():
        arr.append(j+[i])
for i in arr:
    if len(i)==k and sum(i)==0:
        a.append(i)
b=set(tuple(i) for i in a)
# print([list(i) for i in b])
result=[]
for i in b:
    result.append(list(i))
print(result)
