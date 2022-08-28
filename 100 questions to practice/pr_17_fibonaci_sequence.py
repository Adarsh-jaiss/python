# program to print fibonaci sequence
''' A fibonaci sequence is the integer sequence of 0,1,1,2,3,5,8 
        The first two terms are 0,1 ,. all other terms are obtained by adding the preceding two terms.
        This means to say the nth term is the sum of (n-1) and (n-2)th term. '''


nterms =int (input(" How many terms ?"))
n1,n2 = 0,1
count = 0
# check either the number of terms is valid
if nterms <= 0:
    print(" Please enter a positive number")

# if there is only one term
elif nterms == 1 :
    print("Fibonic's term upto", nterms,":")
    print (n1)
# if there is nth terms
else :
    print("Fibonic sequence")
    
