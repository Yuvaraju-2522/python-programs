s="snapchat"
dici={}
for i in s:
  if i not in dici:
    dici[i]=1
  else:
    dici[i]+=1
print(dici)
for i in range(len(dici)):
  if dici[s[i]]==1:
    print(i)
    ch=s[i]
    break
pos=ord(ch)-ord("a")+1
r_pos=27-pos
r_ch=chr(ord("a")+r_pos-1)
print(ch,r_ch)