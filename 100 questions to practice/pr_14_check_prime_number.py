# program to check whether a number is prime or composite

num= int(input("Enter the number :"))

flag =False

if num >1: #(prime no's are always greater than 1)
    #check for factors]
    for i in range(2,num):
        if (num % i) ==0 :
            #if factor is found set flag to true
            flag = True 
            break
if flag:
    print(num, "is not prime number")
else:
    print(num, "is a prime number ")
