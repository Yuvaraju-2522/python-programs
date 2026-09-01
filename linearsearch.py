arr=[10,20,30,45,50]
search=30
found=0
for i in range(len(arr)):
    if arr[i]==search:
        found=i
        break
    else:
        found=0
print(found)