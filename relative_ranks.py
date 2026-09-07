score = [5,4,3,2,1]
ans=[]
for i in range(len(score)):
    rank=1
    for j in range(len(score)):
        if score[j]>score[i]:
                rank+=1
    if rank==1:
        ans.append("Gold Medal")
    elif rank==2:
        ans.append("Silver Medal")
    elif rank==3:
        ans.append("Bronze Medal")
    elif rank==4:
        ans.append("4")
    else:
        ans.append("5")
print(ans)
        