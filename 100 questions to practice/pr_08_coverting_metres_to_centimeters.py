# program to convert m to cm

# a = input("Enter the number :")



def convert_m_to_cm(a) :
    return a*100          #(1m = 100cm)

a= 5
print("The value in cm is " , convert_m_to_cm(a))


# program to convert kms to miles

# Taking kms input from user
kilometeres = float(input("Enter values in kms :"))

#conversion factor 
conv_fac = 0.621371
# conerting kms to miles
Miles = kilometeres* 0.621371

print("The value in miles is ", Miles)

# NOTE : for converting miles to km : miles / conv_fac