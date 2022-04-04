
from math import sqrt

a = float(input("Enter the value of a "))
b = float(input("Enter the value of b "))
c = float(input("Enter the value of c "))

d = (b**2) - (4*a*c)


sol1 = (-b-sqrt(d))/(2*a)
sol2 = (-b+sqrt(d))/(2*a)

print("your two soloutions are: ", sol1,sol2)
