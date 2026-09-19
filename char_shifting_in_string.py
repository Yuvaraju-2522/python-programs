s="abcz"
a=""
for i in s:
    if i=="z":
        a+="a"
    else:
        x=ord(i)+1
        a+=chr(x)
print(a)