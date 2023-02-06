num=int(input("enter the number"))
if num>1:
    for i in range(2,num):#(2,23)
        if(num%i==0):
            print("it is not a prime number")
            break
    else:
        print("its a prime number")
