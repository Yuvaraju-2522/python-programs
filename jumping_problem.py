arr = [1,3,5,8,9,2,6,7,8,9,1,1,1]
n=len(arr)
i=0
jumps=0
while i<n-1:
    i+=arr[i]
    jumps+=1
print(jumps)