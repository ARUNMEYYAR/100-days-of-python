a=input("enter the character:")
if a=='a'or a=="e" or a=="i" or a=="o" or a=="u" or a=="A"  or a=="E" or a=="I" or a=="O" or a=="u":
    print("it is a vowel")
elif ((a >= 'A' and a <= 'Z') or (a >= 'a' and a<= 'z')):    
    print("it  is constant")
else:
    print("it is invalid")    