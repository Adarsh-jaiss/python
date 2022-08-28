# python program to check the leap year

''' A leap year is perfectly divisble by 4 except the century year.
    The century year is a leap year if it is perfectly divisible by 400 '''

year = int(input("Enter the year :"))

if year %400 ==0:
    print("This is a leap year!")
elif year %4 ==0:
    print("This is a leap year!")
else:
    print("This is not a leap year!")