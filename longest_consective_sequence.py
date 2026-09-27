nums = [100,4,200,1,3,2]
b=sorted(nums)
z=0
a=[[]]
for i in b:
    for j in a.copy():
        a.append(j+[i])
for i in a:
    c=len(i)
    if c==0:
        continue
    d=i[0]
    count=0
    for j in range(d,d+c):
        if j in i:
            count+=1
    if count==c:
        z=max(z,c)
print(z)

