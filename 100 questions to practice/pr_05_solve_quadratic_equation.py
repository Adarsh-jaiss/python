# Program to solve a quadratic equation

# Let q = ax**2 + b*x+ c (a quadratic equation)

#import complex math module
import cmath

a= 1
b= 5
c= 6
# let's first calculate the discriminant

d= (b**2)- (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/ (2*a)
sol2 = (-b+cmath.sqrt(d))/ (2*a)

print(" The solutions are ",sol1,sol2)
