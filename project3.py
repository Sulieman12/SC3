from math import sqrt


NoRoots = True


while NoRoots:
  try:
    a = float(input("Enter the value of a: \n"))
    b = float(input("Enter the value of b: \n"))
    c = float(input("Enter the value of c: \n"))

    Value = (b**2)-(4*a*c)
    s1 = (-b+sqrt(Value)/(2*a))
    s2 = (-b-sqrt(Value)/(2*a))

    print(s1,s2)
    NoRoots = False 

  except:
        print("There Are no roots \n")
