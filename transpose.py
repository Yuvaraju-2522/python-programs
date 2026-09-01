matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose=list(map,list(zip(*matrix)))
print(transpose)

# using for loop
row=int(input())
matrix=[]
for i in range(row):
    r=list(map(int,input().split(" ")))
    matrix.append(r)
print(matrix)

rows=len(matrix)
cols=len(matrix[0])
transpose=[]
for i in range(cols):
    new_row=[]
    for j in  range(rows):
        new_row.append(matrix[j][i])
    transpose.append(new_row)
print(transpose)