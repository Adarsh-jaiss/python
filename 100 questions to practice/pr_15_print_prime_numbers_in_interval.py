# Python program to print all prime numbers within interval (900 to 1000)

# We can also take input from user
# lower = int(input("Enter the lower range"))
# upper = int(input("Enter the upperrange"))
lower = 900
upper = 1000

print("prime numbers between", lower ,"and",upper , "are :")

for num in range(lower,upper) :
    if num>1 :                         # all prime no's are greater than 1
        for i in range (2,num) :
            if (num%i) == 0 :
                break
        else:
            print(num)

