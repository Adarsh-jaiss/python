# python program to find factorial of a number

# Taking input from the user
# num = int(input(" Enter the number :"))

num = 7
factorial = 1
# check if the number is negetive positive or zero
if num < 1:
    print(" Factorial of negetive numbers don't exist!")
elif num == 0 :
    print(" Factorial of zero is 1 ") 
else :
    for i in range (1 ,num+1) :
        factorial = factorial*i
    print("The factorial of ", num , "is", factorial)