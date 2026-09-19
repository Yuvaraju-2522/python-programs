arr=[16,17,9,3,5,2]
a=[]
n=len(arr)
for i in range(n):
    leader=True
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            leader=False
            break
    else:
        a.append(arr[i])
print(a)
