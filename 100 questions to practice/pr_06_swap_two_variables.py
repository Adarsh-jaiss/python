# program to swamp two variables

x = 5
y = 8

# code for taking inputs from user
# x = input("enter the value of x :")
# y = input("enter the value of y :") 

# Now create an another variable and swamp the values of x and y
a = x
b = y

print('The values of x after swamping is', b)
print('The value of y after swamping is' , a)


# MOST SIMPLE FORM TO DO THIS SAME STUFF
x = 5
y = 8
x,y =y,x

print('x =', y )
print('y =', x)