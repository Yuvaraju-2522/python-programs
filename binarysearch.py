nums=[10,20,30,45,50]
target=30
start=0
end=len(nums)-1
while start<=end:
    mid=(start+end)//2
    if nums[mid]==target:
        print(mid)
        break
    elif nums[mid]<target:
        start=mid+1
    else:
        end=mid-1
    print("-1")