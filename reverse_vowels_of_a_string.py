s = "IceCreAm"
n=len(s)
a=list(s)
left=0
right=n-1
vowels="aeiou"
while left<right:
    if a[left].lower() not in vowels:
        left+=1
    elif a[right].lower() not in vowels:
        right-=1
    else:
        a[left],a[right]=a[right],a[left]
        left+=1
        right-=1
print("".join(a))