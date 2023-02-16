num=int(input("enter the number:"))
s=str(num)
new=[]
for i in s:
    if(i=='0'):
     new.append('1')
else:
     new.append(i)
newnum=""
for i in new:
 newnum+=i
print(int(newnum))