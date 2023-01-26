a=int(input("enter the orgin of x:"))
b=int(input("enter the orgin of y:"))
if(a>=0 & b>=0):
    print("it lies in first quadrant")
elif(a<=0 & b>=0):
    print("it lies in second quadrant")
elif(a<=0 & b<=0):
    print("it lies in  third quadrant")
elif(a>=0 & b<=0):
    print("it lies in fourth quadrant")
else:
    print("it lies in orgin")    