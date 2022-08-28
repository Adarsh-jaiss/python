import re


# program to find the area of rigt angle traingle

def area(a,b) :
    return 0.5*a*b  #(where a is base and b is the height of the right angle triangle)

a= float(input("Enter the base of right angle triangle :"))
b= float(input("Enter the height of right angle triangle :"))

print("The area of right angle triangle is " , area(a,b))





# Program to find the area of Triangle


# we can either assign values to the sides of triangle a,b,c
# a=5, b=7, c=9

a = float(input("Enter the 1st side of the  triangle :"))
b = float(input("Enter the 2nd side of the  triangle :"))
c = float(input("Enter the 3rd side of the  triangle :"))

#  Now we will first find the semi perimeter of triangle

s = 0.5*(a+b+c)

area = s*(s-a)*(s-b)*(s-c) **0.5
print("The area of the triangle is ", area)




