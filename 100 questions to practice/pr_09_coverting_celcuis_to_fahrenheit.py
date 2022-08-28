# Program to convert celcius to fahrenheit

def c_to_f(a) :
    return a*1.8 +32  #(farhenheit = celcius*1.8 +32)

a = float(input("Enter the value in celcius :"))
print("The value in Fahrenheit is ", c_to_f(a))

# NOTE: celcius = farhenheit - 32 / 1.8
