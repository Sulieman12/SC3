# Sulieman Project #3
# 04-06-2022

from math import *

NoRoot = True

while NoRoot:
    try:
        a = float(input("Enter the value of a: \n"))
        b = float(input("Enter the value of b: \n"))
        c = float(input("Enter the value of c: \n"))

        Value = (b**2)-(4 * a * c)
        s1 = (-b + sqrt(Value))/(2 * a)
        s2 = (-b - sqrt(Value))/(2 * a)

        print("Roots", (s1, s2))
        NoRoot = False

    except:
        print("There Are no roots \n")
