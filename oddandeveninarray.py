arr=[10,20,33,45,50]
even=0
odd=0
for i in arr:
    if i %2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)



arr=[10,20,33,45,59]
even=0
odd=0
for i in range(len(arr)):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)