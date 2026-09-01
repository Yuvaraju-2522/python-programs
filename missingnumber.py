n=[1,2,3,4,5,6,7,9,10]
a=n[-1]
total=a*(a+1)//2    #total=10*11//2
result=(total-sum(n))
print(result)

#using loop
n=[1,2,3,4,5,6,7,10]
for i in range(1,11):
    if i not in n:
        print(i)
        
