# Python program to find largest among the 3 

a= int(input("enter the 1st number :"))
b= int(input("enter the 2nd number :"))
c= int(input("enter the 3rd number :"))
print("The inputs are : ",(a,b,c))

if a>b and a>c :
    print (a , " is the greatest among three numbers")
elif b>a and b>c :
    print(b, "is the greatest among three numbers")
elif c>a and c>b :
    print(c, "is the greatest among three numbers")



