# program to find square root of positive numbers

def num_sqrt(a) :
    return a** 0.5


a = 8
# Taking inputs from user 
# a= float(input("Enter the number :"))

print("square root of 8 is ", num_sqrt(a))






# program to find square root of complex numbers
# for this we need to import complex math module

import cmath
num = 1+2j

# To take input from users
# num = eval(input("Enter the number :"))

num_sqrt = cmath.sqrt(num)

print("The square root of complex no is ", num_sqrt)






