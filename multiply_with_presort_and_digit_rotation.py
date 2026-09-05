a=123
b=45
z=str(a)
y=str(b)
c=str(z[::-1])
d=str(y[::-1])
e=int(c)*int(d)
print(e)
result=""
for i in str(e):
  result+=str(int(i)+2)
print(result)

  
