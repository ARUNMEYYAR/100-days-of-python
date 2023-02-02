num=int(input("Enter a number: "))
fact=1
Sum=0
copy=num
if(num==0):
 Sum=Sum+fact
else:
 while(copy!=0):
    fact=1
    rem=copy%10
 for i in range(1,rem+1):
    fact=fact*i
    Sum=Sum+fact
    copy=copy//10
if(Sum==num):
  print("Strong number")
else:
 print("Not a strong number")