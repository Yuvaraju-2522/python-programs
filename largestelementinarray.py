arr=[10,20,83,45,50]
val=arr[0]
for i in arr:
    if i>val:
        val=i
print(val)


arr=[10,20,93,45,50]
val=arr[0]
for i in range(len(arr)):
    if arr[i]>val:
        val=arr[i]
print(val)