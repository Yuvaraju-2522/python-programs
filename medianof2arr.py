a=[1,2]
b=[3,4,5,6,7]
for i in a:
    b.append(i)
c=sorted(b,reverse=True)
print(c)
n=len(c)
if n%2==0:
    median=(c[n//2]+c[n//2-1])/2
else:
    median=n//2
print(median)