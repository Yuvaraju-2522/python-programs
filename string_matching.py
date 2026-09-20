words = ["mass","as","hero","superhero"]
a=[]
b=[]
for i in words:
    for j in words:
        if i!=j and j in i:
            a.append(j)

for i in a:
    if i not in b:
        b.append(i)
print(b)
