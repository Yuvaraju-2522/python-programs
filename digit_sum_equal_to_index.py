nums = [1,10,11]
for i in range(0,len(nums)):
    n=nums[i]
    a=0
    while n>0:
        temp=n%10
        a+=temp
        n=n//10
    if i==a:
        print(i)