arr=[2,0,2,1,1,0]
n=len(arr)
for i in range(n):
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)